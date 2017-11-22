FROM centos:7

# https://stlong0521.github.io/20161023%20-%20Airflow.html
# https://groups.google.com/forum/#!topic/airbnb_airflow/lzAqI1D9wsg

#
# install mandatory dependencies
#
RUN yum -y install \
        epel-release \
    && yum -y install \
        python \
        python-devel \
        python-pip \
        supervisor \
        gcc \
        glibc-devel \
        glibc-headers \
        kernel-headers \
        libgomp \
        libmpc \
        mpfr \
        which \
    && pip install --upgrade pip

#
# perform clean airflow setup
#
RUN pip install apache-airflow==1.8.2 \
    && pip install apache-airflow[celery] \
    && pip install apache-airflow[postgres] \
    && pip install redis

COPY compose-config/ /etc/compose-config
