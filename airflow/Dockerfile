FROM python:3.7

# supervisord setup                       
RUN apt-get update && apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN pip install apache-airflow==1.10.3

# Airflow setup                       
ARG AIRFLOW_HOME="/app/airflow"
ARG AIRFLOW_CONFIG_FILE="./airflow_config_files/airflow_config.cfg"
ARG AIRFLOW_REQUIREMENTS_FILE="./airflow_config_files/requirements.txt"
ENV AIRFLOW_HOME=${AIRFLOW_HOME}
COPY ${AIRFLOW_REQUIREMENTS_FILE} ${AIRFLOW_HOME}/requirements.txt
COPY ${AIRFLOW_CONFIG_FILE} ${AIRFLOW_HOME}/airflow.cfg
COPY /dags/ ${AIRFLOW_HOME}/dags/

RUN pip install -r ${AIRFLOW_HOME}/requirements.txt
RUN airflow initdb
EXPOSE 8080
CMD ["/usr/bin/supervisord"]
