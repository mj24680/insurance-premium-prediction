# python 3.11 base imahge / operating system in which a version of python already running
FROM python:3.12-slim

# set working directory
WORKDIR /app

# copy requirements to working dir and install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of the application code
COPY . .

# Expose the appliation port depending on what type of application
EXPOSE 8000

# command to start FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]