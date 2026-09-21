# Big Data in Cloud and IoT — UPT

Laboratory materials under development for the Cloud Computing and Internet of Things master's programme at Universitatea Politehnica Timișoara, academic year 2026–2027.

## What you will investigate

How do data-handling choices affect an analytical result? This laboratory follows recorded physiological telemetry through ingestion, storage, batch and stream processing, quality checks, feature construction and evaluation. Supporting technical documents introduce retrieval, source attribution and updates.

The emphasis is on explaining results, comparing alternatives and reproducing the processing steps.

## Start here

- [Semester laboratory map](docs/lab-map.md)
- [Runnable data-quality notebook](labs/03-data-quality/03_data_quality.ipynb)
- [Moodle setup and pages](moodle/INSTRUCTOR_SETUP.md)
- [Container and GHCR instructions](docs/container-release.md)
- [Preparation roadmap](docs/roadmap.md)

## Current status

This repository contains the semester map, 14 Moodle lab page sources and a runnable introductory data-quality notebook with an attributed public heart-rate excerpt. The remaining lab pages describe their learning scope. See [verification status](docs/verification.md) for execution results and container limitations.

## Run the notebook

### Published environment

The container package is distributed through [GHCR](https://github.com/bozdogalex/big-data-cloud-iot-upt/pkgs/container/big-data-cloud-iot-upt).
See [release instructions](docs/container-release.md) for the verified release and immutable digest.

```sh
git clone https://github.com/bozdogalex/big-data-cloud-iot-upt.git
cd big-data-cloud-iot-upt
docker compose -f compose.release.yaml up -d
docker compose -f compose.release.yaml logs lab
```

Open the localhost Jupyter URL from the logs. The notebook is under
`labs/03-data-quality/03_data_quality.ipynb`. The release uses a persistent Docker
volume for your work and targets linux/amd64.

### Build from source

With Docker Desktop's Linux engine running, execute `docker compose up --build` from this directory. Open `http://127.0.0.1:8888/lab?token=...` using the token printed in the logs, and navigate to `labs/03-data-quality/03_data_quality.ipynb`. Select **Run → Run All Cells**. Authentication remains enabled. The local `labs` folder is mounted so saved work persists. Stop with `docker compose down`.

Alternatively, create and activate a Python 3.12 virtual environment, run `python -m pip install -r requirements.txt`, then `python -m jupyter lab`.

The planned core exercises use recorded data and locally executable tools. Paid cloud accounts and physical sensor hardware are not planned prerequisites.

## Assessment

The laboratory contributes 40% of the discipline grade; the examination contributes 60%. The approved discipline sheet and published Campus Virtual requirements govern assessment. Detailed laboratory grading is being finalised.

## Data and reuse

Original code is available under [MIT](LICENSE), and original teaching text under [CC BY 4.0](LICENSE-CONTENT.md). You can reuse and adapt the educational materials with attribution. The editable notebooks, source files and container recipe are included.

The example includes BIDMC data; its separate licence, attribution and teaching modifications are documented in [data provenance](labs/03-data-quality/data/README.md). See [third-party notices](THIRD_PARTY_NOTICES.md) for the scope of these licences.
