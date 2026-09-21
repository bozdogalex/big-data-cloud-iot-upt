# Moodle setup guide

Use [COURSE_STRUCTURE.md](COURSE_STRUCTURE.md) as the ordered setup checklist.
The two assignment description files are hidden instructor drafts pending the
final project brief. Existing lab pages and the Lab 03 activity are retained.

For paste-ready HTML and an offline preview, run
`python scripts/package_moodle.py` in the notebook environment (uses its installed
Mistune renderer). The package is written to `artifacts/moodle-upload.zip`.
HTML fragments can be pasted into the Page editor's HTML/source view; Markdown
can be used where the course editor exposes that format. This is manual page
content, not an automatic course restore/import archive.

## Recommended structure

1. **Start here:** one Page containing `00-start-here.md`; add the repository/environment link when ready.
2. **Projects:** `projects-overview.md`, the eventual detailed project brief, and two proposed milestone Assignment activities for one project. One project with milestones was the latest assessment model discussed; the exact submission boundaries remain open. Leave deadlines, grading and group settings unset until agreed.
3. **Labs 01–14:** one section per lab, containing the corresponding `lab-NN.md` as a Page or section description. Add presentations as File resources in that section when available.
4. **Selected lab sections:** separate optional exercise activities. Lab 03 has `exercise-03-data-quality.md`. Use a Page unless submission/feedback is needed; create an Assignment only when students actually need to submit there.

Keep project submissions in one predictable place. Link to them from relevant labs rather than duplicating submission activities. Avoid creating 13 empty assignment slots.

## Using the Markdown files

Uploading a `.md` file as a File resource may simply provide a download. For an inline readable page, use Moodle's Markdown text format if your editor exposes it, or paste the rendered content into a Page's rich-text editor. These files are content sources, not a Moodle backup/import package.

Attach the notebook as a downloadable file or link the repository; its relative data folder is required to run it, so distribute the whole lab folder or repository rather than the notebook alone.

## Visibility and recording

Publish pages when ready for students. In the submission video, show the semester structure and the actual Lab 03 activity/result. A course outline establishes structure, not completion of all technical materials. No student records or fictional submissions are needed.
