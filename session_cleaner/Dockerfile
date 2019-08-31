FROM python:3.7.4-slim
ENV PIPENV_VENV_IN_PROJECT 1
ENV MONGODB_HOST localhost
ENV MONGODB_PORT 27017
ENV MONGODB_USER root
ENV MONGODB_PASSWORD root
ENV DB Test
WORKDIR /session_cleaner
COPY . /session_cleaner
RUN pip3 install pipenv \
	&& pipenv sync
CMD ["pipenv","run","python","clean_expired_sessions.py"]
