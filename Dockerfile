FROM python:3.12.10-slim-bookworm@sha256:fd95fa221297a88e1cf49c55ec1828edd7c5a428187e67b5d1805692d11588db
LABEL org.opencontainers.image.source="https://github.com/bozdogalex/big-data-cloud-iot-upt"
LABEL org.opencontainers.image.description="Reproducible BDCIOT teaching environment with the Lab 03 physiological data-quality notebook."
LABEL org.opencontainers.image.licenses="MIT AND CC-BY-4.0"
WORKDIR /workspace
COPY requirements-lock.txt ./requirements-lock.txt
RUN pip install --no-cache-dir -r requirements-lock.txt
RUN useradd --create-home --uid 1000 student && chown student:student /workspace
COPY --chown=student:student labs ./labs
COPY --chown=student:student LICENSE LICENSE-CONTENT.md THIRD_PARTY_NOTICES.md README.md ./
COPY --chown=student:student moodle ./moodle
COPY --chown=student:student docs ./docs
USER student
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--ServerApp.root_dir=/workspace"]
