FROM sequenceiq/hadoop-docker
COPY . .
WORKDIR .
RUN sh install.sh
CMD python runner.py
