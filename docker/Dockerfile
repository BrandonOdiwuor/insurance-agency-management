FROM python:3.6-buster

# create the project's root directory
RUN mkdir -p /app

# Set the working directory to /app
WORKDIR /app

# Copy files to the container's /app directory
COPY .  /app

# Install and upgrade pip
RUN pip install --upgrade pip

# Install the pipenv package manager
RUN pip install pipenv

# Install all the needed packages specified in the Pipfile
RUN pipenv update -r "requirements.txt"

# Install all the needed packages specified in the Pipfile
RUN pipenv install --system --deploy --ignore-pipfile


# Run the command to start the service
CMD ["/bin/bash", "scripts/entrypoint.sh"]
