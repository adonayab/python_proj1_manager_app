FROM ubuntu
# install python3 pip3 and requirements
RUN apt-get update && \
  apt-get install -y \
  python3 \
  python3-pip \
  sqlite

COPY . /app

RUN pip3 install -r /app/project-layout/requirements.txt

RUN cd /app && ./initialize_dummy_data.sh

EXPOSE 5000

CMD ["python3", "/app/run.py"]
