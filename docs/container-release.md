# Docker and GHCR distribution

Docker packages the environment; GHCR distributes the image. Start locally with `docker compose up --build`, with the Docker Linux engine enabled. The service is exposed only on localhost and retains Jupyter token authentication. The `labs` directory is mounted from your checkout, so saved work persists.

## Publishing a release

1. Push the reviewed files to the agreed GitHub repository.
2. Run the manual **Verify and publish lab container** workflow with publishing disabled. It builds the image, executes the notebook and verifies results.
3. After validation, run it with publication enabled. It publishes `ghcr.io/<owner>/<repo>:<full-commit-sha>` using the workflow token.
4. Record the immutable digest from the push and distribute `ghcr.io/<owner>/<repo>@sha256:<digest>`. Verify student pull access; package visibility is separate from repository visibility.

For a published image, replace Compose's `image` with the verified digest and remove `build`. Use the lab files from the same release commit, because the local mount overrides the bundled files.

The Python base image is pinned by digest. `requirements-lock.txt` includes the resolved Linux dependencies as well as the shared Python packages. The Linux build and execution results are recorded in `verification.md`. These pins improve rebuild consistency; a published image digest fixes the exact distributed runtime.

No remote repository or image has been published during this local preparation. Publication is manual, not triggered by a push.

References: https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images and https://docs.docker.com/build/building/best-practices/
