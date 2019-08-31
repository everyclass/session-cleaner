FROM python:3.7.4-slim
RUN pip3 install pymongo
WORKDIR /clean_sessions
COPY . /clean_sessions
ENV MONGODB_LINK localhost
ENV MONGODB_PORT 27017
ENV MONGODB_USER root
ENV MONGODB_PASSWORD root
ENV DB test
CMD ["python3", "clean_expired_sessions.py"]
