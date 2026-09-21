# Docker and GHCR distribution

Docker packages the environment; GHCR distributes the image. The public package is
https://github.com/bozdogalex/big-data-cloud-iot-upt/pkgs/container/big-data-cloud-iot-upt.

## Run the published environment

From a checkout of this repository, with Docker Desktop's Linux engine running:

```sh
docker compose -f compose.release.yaml up -d
docker compose -f compose.release.yaml logs lab
```

Open the localhost Jupyter URL shown in the logs, including its login token.
Do not include that token or terminal logs in a recording. Navigate to
`labs/03-data-quality/03_data_quality.ipynb` and use **Run → Run All Cells**.

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

## Publishing a release

1. Push the reviewed files to the agreed GitHub repository.
2. Run the manual **Verify and publish lab container** workflow with publishing disabled. It builds the image, executes the notebook and verifies results.
3. After validation, run it with publication enabled. It publishes `ghcr.io/<owner>/<repo>:<full-commit-sha>` using the workflow token.
4. Record the immutable digest from the push and distribute `ghcr.io/<owner>/<repo>@sha256:<digest>`. Verify student pull access; package visibility is separate from repository visibility.

The published release configuration is kept separately in `compose.release.yaml`.
The `latest` tag is a convenience alias; use the pinned digest for repeatable teaching sessions.

The Python base image is pinned by digest. `requirements-lock.txt` includes the resolved Linux dependencies as well as the shared Python packages. The Linux build and execution results are recorded in `verification.md`. These pins improve rebuild consistency; a published image digest fixes the exact distributed runtime.

The image from source commit `3063f1f30fbb89304b667a65c309833373cf408b` was published
on 21 September 2026 after the notebook checks passed in GitHub Actions.
Publication is manual, not triggered by a push. Subsequent documentation-only
commits can record a release digest without rebuilding that image.

References: https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images and https://docs.docker.com/build/building/best-practices/
