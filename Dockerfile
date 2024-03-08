#pulling base image 
FROM python:3.10

#environment variables
#dont give me pyc and dont buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#my directory
WORKDIR /petadoption

#installing my dependancies
COPY Pipfile Pipfile.lock /petadoption/
RUN pip install pipenv && pipenv install --system

#Copying my project code
COPY  . /petadoption/

