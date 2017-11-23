# airflow 1.8.2

Containers:

* airflow-master (webserver, scheduler)
* airflow-worker (worker)
* redis - broker for celery
* postgresql - data storage for airflow and celery reports


## starting up

```bash
$ docker-compose build
$ docker-compose up
```

## DAG a-la CRON

> DAG definition is [located here](airflow-data/dags/cronlike_dag.py)

1. Navigate: `http://127.0.0.1:8080/admin/`
1. Switch on `cronlike_dag`
1. Navigate `http://127.0.0.1:8080/admin/dagrun/`
1. Watch the results..

