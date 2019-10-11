FROM python:3.7.3
RUN mkdir /save_name
COPY .. /save_name
RUN pip install -r /save_name/requirements.txt
WORKDIR /save_name

CMD ["python", "name_add_get.py"]