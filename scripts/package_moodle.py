"""Package existing Moodle sources as Markdown, HTML fragments and a local preview."""
from pathlib import Path
from html import escape
from zipfile import ZipFile, ZIP_DEFLATED
import mistune

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'artifacts/moodle-upload'
OUT.mkdir(parents=True, exist_ok=True)
render = mistune.create_markdown(escape=True, plugins=['table'])
style = 'body{font:17px/1.6 system-ui,sans-serif;max-width:1050px;margin:48px auto;padding:0 28px;color:#17212b}a{color:#075ca8}h1,h2{line-height:1.25}table{border-collapse:collapse;width:100%;font-size:15px}td,th{border:1px solid #ccd4db;padding:8px;text-align:left}code{background:#edf1f4;padding:2px 4px}nav{padding:16px;background:#eef4f8}section{border-top:1px solid #ccd4db;margin-top:32px;padding-top:16px}'
items = []
order = ['00-start-here', 'projects-overview', 'assignment-intermediate', 'assignment-final']
for number in range(1,15):
    matches = list((ROOT / 'moodle').glob(f'lab-{number:02d}-*.md'))
    if len(matches) != 1:
        raise ValueError(f'Expected one page for lab {number:02d}, found {len(matches)}')
    order.append(matches[0].stem)
    if number == 3:
        order.append('exercise-03-data-quality')
generated = []
for name in order:
    source = ROOT / 'moodle' / f'{name}.md'
    value = source.read_text(encoding='utf-8')
    title = value.splitlines()[0].removeprefix('# ')
    body = render(value)
    (OUT / source.name).write_text(value, encoding='utf-8')
    (OUT / f'{source.stem}.fragment.html').write_text(body, encoding='utf-8')
    generated.extend([OUT / source.name, OUT / f'{source.stem}.fragment.html'])
    # Page links refer to other source pages. Point those to GitHub in the preview.
    for target in (ROOT / 'moodle').glob('*.md'):
        body = body.replace(f'href="{target.name}"', f'href="https://github.com/bozdogalex/big-data-cloud-iot-upt/blob/main/moodle/{target.name}"')
    items.append((source.stem, title, body))
nav = ''.join(f'<li><a href="#{escape(key)}">{escape(title)}</a></li>' for key,title,_ in items)
sections = ''.join(f'<section id="{escape(key)}">{body}</section>' for key,_,body in items)
preview = f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>BDCIOT — laboratory notes</title><style>{style}</style><body><h1>BDCIOT — laboratory notes</h1><p>Offline copy of the lab descriptions and exercises.</p><nav><ul>{nav}</ul></nav>{sections}</body></html>'
(OUT / 'index.html').write_text(preview, encoding='utf-8')
generated.append(OUT / 'index.html')
for name in ['LICENSE-CONTENT.md', 'THIRD_PARTY_NOTICES.md']:
    (OUT / name).write_text((ROOT / name).read_text(encoding='utf-8'), encoding='utf-8')
    generated.append(OUT / name)
with ZipFile(ROOT / 'artifacts/moodle-upload.zip', 'w', ZIP_DEFLATED) as archive:
    for path in sorted(generated):
        archive.write(path, path.name)
print(f'Packaged {len(items)} Moodle sources and HTML fragments: {OUT}')
