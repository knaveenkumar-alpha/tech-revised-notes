FROM python:3.8.13-buster

#RUN wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb && \
#    dpkg -i packages-microsoft-prod.deb && \
#    apt-get update && \
#    apt-get -y install sudo && \
#    apt-get update && \
#    apt-get install azure-functions-core-tool-3

WORKDIR /App-Service
# set company proxis
COPY . .
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

EXPOSE 5000
CMD ["python", "run.py"]