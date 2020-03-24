# flask_boilerplate
A repository with goal to make a flask API developer life easier, thus not only integrates libraries but also covered a simple API implementation.

It utilizes below libraries,
1. Flask SqlAlchemy (Wrapper on SqlAlchemy)
2. Flask Migrate (Wrapper on Alembic)
3. Flask Manager (Wrapper on Flask Scripts)
4. Gunicorn (Web Server)
5. Psycopg2 to interact with Postgres instance

**Features**
- Complete end to end implementation of a CRUD user story.
- It supports environment specific configuration using .env file.
- Keeps isolation of concern to some extent using layered architecture, thus provides place to write new migrations, new data base models and API.
- Gives brief example of serializing SqlAlchemy object to JSON.
- Logging of web request and exceptions.

**Future Plans**
- Unit test case library integration.
- Test coverage status pre-commit hook
- Integration with pylint as a pre-commit hook
- Release management e.g. version update
- Docker based setup [Docker and Docker Compose]
- Flask CORS integration
- Flask CSRF integration
- Authentication and authorization setup using any oauth server e.g. keycloak
- Integration with swagger
- Standardized Api request and response formats

## Layered Architecure
Application is divided in 6 layers.

1. Root
    - Holds infrastructure files, that runs whole application.
2. APIs 
    - Provides routing to API
    - Responsible to serialize request
    - Direct request to service layer
    - Deserialize service response
    - Send it back to the API client.
3. Services
    - Responsible to drive business logic
    - Use repository layer to interact with database
4. Repositories
    - Responsible to make queries to database 
5. Models
    - It holds definition of database models
6. Migrations
    - Responsible for database migrations.

### Steps to Configure

#### Dependencies
Postgresql instance is up and running
Python 3+ is installed

#### Step1 - Clone repository
Clone the repository,

```git clone https://github.com/uinvent/flask_boilerplate.git```

#### Step2 - Setup environment configurations
Create a copy of .env.sample and name it as .env. Fill it with your machine configurations.

APP_DB_* configurations are must as they lead to your database. 

#### Step3 - Install project dependencies
Install libraries used in project,

```
virtualenv --python=python3 venv --no-site-packages
source venv/bin/activate
pip install -r requirements.txt
```


#### Step4 - Run database migrations
 
 `python manage.py init`  
 
It will create database on the server configured in .env file. 
  
Then run, 
 
`python manage.py db upgrade`

This will run two migrations,
 1. First will create two sample tables person and address. Where each person can have multiple addresses.
 2. Second will insert records in these tables.

#### Step5 - Start server

`python manage.py runserver -d`

This will start your app server and now APIs are ready to be consumed for debugging.

To start a production ready server (gunicorn server) `python manage.py runserver`

Now APIs are ready to be consumed on default URL `http://0.0.0.0:8088` 

#### Step6 - Run Code Test

`pytest`

Above command will find all test cases and runs them. Tests are available in /tests/ folder

`pytest --cov=./src/ tests/`

Above command will show the test coverage report.

`pylint src --errors-only`

Above command will run pylint on src folder and will check errors only.  It is using .pylintrc for linting rules.

`tox -e py37`

Above command will run test cases using tox library. 

`tox -e pylint`

Above command will run pylint on all py files including files manage.py, infra.py and conf.py


##### Sample APIs are,
###### GET
1. Get all persons entities.

        http://0.0.0.0:8088/person/
2. Get person entity with id 1.
    
        http://0.0.0.0:8088/person/1
3. Get person entity with its address entities.

        http://0.0.0.0:8088/person/1/address/

###### POST
Save person entity.

    http://0.0.0.0:8088/person/


*Input*

`{
    "date_of_birth": "1996-05-20 00:00:00+05:00",
    "first_name": "umair",
    "gender": "M",
    "last_name": "",
    "middle_name": "",
    "national_identifier": "1110-22-1"
}`

###### PUT
Update person entity.
        
    http://0.0.0.0:8088/person/1/

**Input**

`{
    "date_of_birth": "1996-05-20 00:00:00+05:00",
    "first_name": "umair",
    "gender": "M",
    "last_name": "khan",
    "middle_name": "",
    "national_identifier": "1110-22-1"
}`

###### DELETE
To delete a person entity.
        
    http://0.0.0.0:8088/person/1/

