FROM rust:1.71.0-bookworm AS build-env
ARG TAG
WORKDIR /root
RUN git clone -b $TAG https://github.com/informalsystems/hermes.git
RUN cd hermes && cargo build --release --no-default-features --bin hermes

FROM debian:bookworm-slim

RUN useradd -m hermes -s /bin/bash && apt-get update && apt-get install -y libssl-dev python3 pip python3.11-venv jq && apt-get clean
WORKDIR /home/hermes
USER hermes:hermes
RUN mkdir .hermes

COPY --chown=0:0 --from=build-env /root/hermes/target/release/hermes /usr/bin/hermes

COPY . /home/hermes
RUN python3 -m venv venv
ENV PATH="/home/hermes/venv/bin:$PATH"
RUN pip install --no-cache-dir Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
