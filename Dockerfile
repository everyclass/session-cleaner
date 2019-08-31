FROM python:3.7.4-slim
ENV PIPENV_VENV_IN_PROJECT 1
ENV MONGODB_LINK localhost
ENV MONGODB_PORT 27017
ENV MONGODB_USER root
ENV MONGODB_PASSWORD root
ENV DB Test
RUN pip3 install pipenv
WORKDIR /clean_sessions
COPY . /clean_sessions
RUN pipenv install
RUN pipenv lock
CMD ["pipenv","run","python","clean_expired_sessions.py"]