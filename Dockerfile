# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12

WORKDIR /app/flask_restful

# Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["flask", "run","--reload", "--host=0.0.0.0", "--port=5002"]
