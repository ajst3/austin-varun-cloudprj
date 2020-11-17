FROM bitnami/spark
COPY . /sparktest
WORKDIR /sparktest
USER root
RUN sh install.sh
USER 1001
CMD python runner.py
