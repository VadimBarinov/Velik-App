FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt