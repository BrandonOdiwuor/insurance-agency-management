# Insurance Agency Management System - [Demo](https://youtu.be/AImwltgnr0k)

Web service used by an insurance agency to manage Insurance quotations, policies, customers, invoices, and payments

## Features
- Quotations Management
- Policies Management
- Invoices and Payments Management
- Customer Management

## Technology Stack
[Flask](https://flask.palletsprojects.com/en/1.1.x/) 1.1.2, [Python](https://www.python.org/downloads/release/python-376) 3.7.6, [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) 2.4.4 - Object Relational Mapper, [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) 2.7.0 - Database migrations handling, [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) 0.14.3 - Form validations & rendering, [PyJWT](https://pyjwt.readthedocs.io/en/latest) to encode & decode JWTs token which are Base64Url encoded, and [Pipenv](https://pipenv-fork.readthedocs.io/en/latest) to declares and manage all dependencies (and sub-dependencies)

## Running
1. Run `git clone https://github.com/BrandonOdiwuor/insurance-agency-management`
2. From the projects root run `cp .env.example .env`
3. Configure your `.env` file
4. Run `sh scripts/destroy.sh` if you're not running the application for the first time.
5. Run `sh scripts/build.sh` from the project root folder to build the images and run the containers
6. Test it out at http://${APP_HOST}:${APP_PORT}. The application folder is mounted into the container and your code changes apply automatically.

## Contributing
Here's how we suggest you go about proposing a change to this project:

1. Create a fork on Github.
2. Clone the forked repository your local system.
3. Modify the local repository.
4. Commit your changes.
5. Push changes back to the remote fork on Github.
6. Create a pull request from the forked repository (source) back to the original (destination).

## Rules of engagement
1. Do not hardcode any environment variables in the source code; use the .env file for this
