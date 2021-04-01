## [Insurance Agency Management System](#) - [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/working-with-git/) 
###### The service that handles everything user manipulations; from user authentication to account management
### Technology Stack
[Flask](https://flask.palletsprojects.com/en/1.1.x/) 1.1.2, [Python](https://www.python.org/downloads/release/python-376) 3.7.6, [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) 2.4.4 - Object Relational Mapper, [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) 2.7.0 - Database migrations handling, [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) 0.14.3 - Form validations & rendering, [PyJWT](https://pyjwt.readthedocs.io/en/latest) to encode & decode JWTs token which are Base64Url encoded, and [Pipenv](https://pipenv-fork.readthedocs.io/en/latest) to declares and manage all dependencies (and sub-dependencies)

### Running
###### For Local Development
1. Run `git clone https://bitbucket.org/kbsaasplatform/authentication-svc/src/master/ kb-authentication-svc`
2. From the projects root run `cp .env.example .env`
3. Configure your `.env` file
4. Run `sh scripts/service_destroy_local.sh` if you're running the application for the first time.
5. Run `sh scripts/service_destroy_local.sh && sh scripts/service_deploy_local.sh` from the project root folder to build the images and run the containers
6. Test it out at http://service_host:${SVC_PORT}. The "app" folder is mounted into the container and your code changes apply automatically.

###### For Development Deployment
1. Run `git clone https://bitbucket.org/kbsaasplatform/authentication-svc/src/master/ kb-authentication-svc`
2. From the projects root run `cp .env.example .env`
3. Configure your `.env` file
4. Run `sh scripts/service_destroy_local.sh` if you're running the application for the first time.
5. Run `sh scripts/service_destroy_dev.sh && sh scripts/service_deploy_dev.sh` from the project root folder to build the images and run the containers
6. Test it out at http://service_host:${SVC_PORT}. The "app" folder is mounted into the container and your code changes apply automatically.

###### For Staging Deployment
1. Run `git clone https://bitbucket.org/kbsaasplatform/authentication-svc/src/master/ kb-authentication-svc`
2. From the projects root run `cp .env.example .env`
3. Configure your `.env` file
4. Run `sh scripts/service_destroy_local.sh` if you're running the application for the first time.
5. Run `sh scripts/service_destroy_stage.sh && sh scripts/service_deploy_stage.sh` from the project root folder to build the images and run the containers
6. Test it out at http://service_host:${SVC_PORT}. The "app" folder is mounted into the container and your code changes apply automatically.

###### For Production Deployment
1. Run `git clone https://bitbucket.org/kbsaasplatform/authentication-svc/src/master/ kb-authentication-svc`
2. From the projects root run `cp .env.example .env`
3. Configure your `.env` file
4. Run `sh scripts/service_destroy_local.sh` if you're running the application for the first time.
5. Run `sh scripts/service_destroy_prod.sh && sh scripts/service_deploy_prod.sh` from the project root folder to build the images and run the containers
6. Test it out at http://service_host:${SVC_PORT}. The "app" folder is mounted into the container and your code changes apply automatically.

###### And that's it with the caveat of setting up, configuring and getting the application running.

### Rules of engagement
1. Do not hardcode any environment variables in the source code; use the .env file for this

### Contributing workflow

Here's how we suggest you go about proposing a change to this project:

###### Option 1
1. Clone the repository to your local system
2. Create a branch from develop; based on the change to be made, following the [gitflow branching model](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
3. Make a change to the branch
4. Push the changes to the Git repository
5. Create a pull request from the branch repository (source) back to the develop branch (destination).

###### Option 2
1. Create a fork on Bitbucket.
2. Clone the forked repository your local system.
3. Modify the local repository.
4. Commit your changes.
5. Push changes back to the remote fork on Bitbucket.
6. Create a pull request from the forked repository (source) back to the original (destination).

#### Useful Resources
[Clone and make a change on a new branch](https://confluence.atlassian.com/bitbucket/clone-and-make-a-change-on-a-new-branch-774243398.html) - For Git, Sourcetree or Mercurial users