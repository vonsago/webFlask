#FROM python:3.6.3 as backend
#
#RUN mkdir /myApp
#WORKDIR /myApp
#
#ENV PYTHONPATH /myApp
#COPY Pipfile /myApp/Pipfile
#COPY Pipfile.lock /myApp/Pipfile.lock 
#RUN pip install --upgrade pip ; pip install pipenv ; pipenv install
#
#COPY . /myApp
#
#CMD ["python3", "app/flaskr.py"]


FROM mysql:5.7.19 as mydb

ENV MYSQL_ROOT_PASSWORD fengyufei123

