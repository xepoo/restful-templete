FROM python:3.7.3
RUN mkdir /save_name
COPY . /save_name
RUN pip install -r /save_name/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
WORKDIR /save_name

CMD ["python", "name_add_get.py"]