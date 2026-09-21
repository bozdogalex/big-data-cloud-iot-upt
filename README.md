# Big Data in Cloud and IoT — UPT

Laboratory materials for **Big Data in Cloud and IoT**, part of the Cloud Computing and Internet of Things master's programme at Universitatea Politehnica Timișoara, 2026–2027.

## About the lab

The laboratory uses physiological recordings to study data ingestion, storage, quality assessment, processing and machine-learning evaluation. Further topics include document retrieval, retrieval-augmented generation (RAG) and pipeline troubleshooting.

Practical work includes implementing processing steps, validating results and explaining the choices made. Reproducibility is part of each analysis.

## Start here

- [Lab topics](docs/lab-map.md)
- [Lab 03: data quality](labs/03-data-quality/03_data_quality.ipynb)
- [Lab descriptions and exercises](moodle/)
- [Docker setup](docs/container-release.md)

## Contents

The repository currently includes the 14 lab descriptions and the complete Lab 03 notebook, with its data and exercises. Other notebooks will be added as they are ready.

## Run the notebook

### Published environment

The container package is distributed through [GHCR](https://github.com/bozdogalex/big-data-cloud-iot-upt/pkgs/container/big-data-cloud-iot-upt).
See [Docker setup](docs/container-release.md) for instructions.

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

Lab 03 runs locally. You do not need a cloud account or a sensor kit for it.

## Assessment

The final grade is **60% exam and 40% laboratory**. The lab project has an intermediate submission and a final presentation in Lab 14. The project brief will give the detailed requirements and grading criteria.

## Data and reuse

Original code is licensed under [MIT](LICENSE); teaching notes and explanations are licensed under [CC BY 4.0](LICENSE-CONTENT.md). The materials may be reused and adapted under these terms.

The example includes BIDMC data; its separate licence, attribution and teaching modifications are documented in [data provenance](labs/03-data-quality/data/README.md). See [third-party notices](THIRD_PARTY_NOTICES.md) for the scope of these licences.
