"""Verify the running Compose service without displaying its login token."""
import json
import tempfile
import urllib.request
from pathlib import Path
from jupyter_server.serverapp import list_running_servers

server = next(list_running_servers())
request = urllib.request.Request(
    server['url'].rstrip('/') + '/api/contents/labs/03-data-quality/03_data_quality.ipynb',
    headers={'Authorization': 'token ' + server['token']},
)
with urllib.request.urlopen(request, timeout=10) as response:
    notebook = json.load(response)
assert notebook['type'] == 'notebook'
assert notebook['writable']
with tempfile.NamedTemporaryFile(dir='/workspace/labs', prefix='bdciot-write-check-', delete=False) as handle:
    path = Path(handle.name)
    handle.write(b'write check')
try:
    assert path.read_bytes() == b'write check'
finally:
    path.unlink()
print('Authenticated notebook access and mounted-folder writes passed.')
