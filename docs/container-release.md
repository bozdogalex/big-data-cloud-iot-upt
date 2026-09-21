# Running the lab with Docker

The lab image is available on GHCR:
https://github.com/bozdogalex/big-data-cloud-iot-upt/pkgs/container/big-data-cloud-iot-upt.

## Run the published environment

From a checkout of this repository, with Docker Desktop's Linux engine running:

```sh
docker compose -f compose.release.yaml up -d
docker compose -f compose.release.yaml logs lab
```

Open the localhost Jupyter URL shown in the logs, including its login token.
Keep the token private. Navigate to
`labs/03-Data quality and integration/03_data_quality.ipynb` and use **Run → Run All Cells**.

The release configuration pins an immutable image digest and stores notebooks
in a named Docker volume, initially populated from the image. Stop with:

```sh
docker compose -f compose.release.yaml down
```

The volume persists after this command. Do not add `-v` unless you intend to
delete that volume's saved work. When changing to a future release, existing
volume contents take precedence over bundled notebooks; export your work first
and use a fresh volume name for that release.

The current published image targets **linux/amd64**. ARM machines require Docker's
amd64 emulation; native ARM execution has not been verified.

## Build from source

Use `docker compose up --build`. This development configuration mounts the local
`labs` directory, so edits persist directly in the checkout. Both configurations
bind Jupyter only to `127.0.0.1:8888` and keep token authentication enabled.
Run one configuration at a time because they share the same port.

## Versions

`compose.release.yaml` selects an exact image version by its SHA-256 digest.
This keeps the environment the same between runs. The `latest` tag can change;
use the Compose file for the lab.

The Dockerfile fixes the Python base image version, and `requirements-lock.txt`
lists the Python package versions used to build the environment.
