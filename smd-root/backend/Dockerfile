# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy the entire application to the container
COPY . .

# which port the app will use
EXPOSE 8000

CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]

# for production use gunicorn
# CMD ["gunicorn", "your_project_name.wsgi:application", "-b", "0.0.0.0:8000"]
