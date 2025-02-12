#pulling base image 
FROM python:3.10

#environment variables
#dont give me pyc and dont buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#my directory
WORKDIR /petadoption

#installing my dependancies
COPY requirements.txt /petadoption/
RUN pip install  --upgrade pip && pip install  -r requirements.txt 

#Copying my project code
COPY  . /petadoption/

EXPOSE 8000
