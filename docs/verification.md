# Verification record

## Published release — 21 September 2026

- Public repository: https://github.com/bozdogalex/big-data-cloud-iot-upt.
- Image source commit: `3063f1f30fbb89304b667a65c309833373cf408b`.
- Successful build, notebook execution and publication:
  https://github.com/bozdogalex/big-data-cloud-iot-upt/actions/runs/35595342430.
- Verified anonymous pull using an empty Docker client configuration.
- Published image digest: `sha256:aa5b901a9f6c484d4da4a9f1022ba7705ee9b34fcfc3272bcbee9fa41821bcee`.
- Ran the published image via `compose.release.yaml` with a new persistent volume.
  Notebook execution, data checksums, duplicate removal, coverage, reference
  agreement and plot generation passed. `pip check` passed.
- Authenticated Jupyter notebook API access and volume write/read/delete checks passed.
- Original code uses MIT; original teaching text uses CC BY 4.0. BIDMC data
  retain the source licence and attribution.
- Prepared 21 Moodle Markdown sources with HTML fragments and an offline preview.
  Visually checked the Lab 03 learning-sequence page. These are manual-upload
  materials; deployment to Campus Virtual is pending service availability.
- Execution was verified on linux/amd64. Native ARM execution is not verified.

## Earlier local preparation

15 September 2026.

- Executed every cell of `03_data_quality.ipynb` successfully using a project-local Python 3.12 environment with the specified dependencies. Outputs are saved in the notebook.
- Verified checksums of all three CSVs.
- Verified received row counts of 70, 45 and 60 per minute; cleaned available counts of 60, 45 and 60; coverage of 100%, 75% and 100%.
- Verified reference agreement in the complete minutes after duplicate removal and generation of the comparison figure. The averages change only slightly; this example deliberately teaches that plausible averages can hide incomplete data.
- Inspected the generated comparison figure.
- `docker compose config --quiet` passed.
- Docker Linux image build passed after the engine became available. The final Dockerfile pins the Python base digest and the dependency snapshot includes pexpect and ptyprocess.
- Executed the notebook and result checks inside the standalone Linux image, then again using the final Compose image with the local lab folder mounted. Both passed. `pip check` found no broken requirements.
- Authenticated Jupyter API access to the notebook and a temporary write/read/delete check in the mounted lab folder passed. The host login endpoint returned HTTP 200. Jupyter is bound to 127.0.0.1:8888 with token authentication enabled.
- Final local image ID: `sha256:cbbc9c78bf7dd9af6e6013e0e1fb4cfbe89e622bcba90cafe0bb5b9c18a9f6fa`. This is a local image ID, not a published GHCR reference.
- No GitHub repository or GHCR image was published.

Recheck after any notebook, data or dependency changes. The generator rebuilds a clean notebook and overwrites its saved outputs; execute the notebook again after regeneration.
