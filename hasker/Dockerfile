FROM centos:latest

RUN mkdir hasker

RUN yum clean all
RUN yum install -y epel-release
RUN yum install -y python python-pip

ADD ./requirements.txt /hasker
RUN pip install -r /hasker/requirements.txt
ADD . /hasker/
