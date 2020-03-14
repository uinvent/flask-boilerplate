from subprocess import Popen
from flask_migrate import MigrateCommand
from flask_script import Manager
from infra import app

config = app.config
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def init():
    init_db()


def init_db():
    from sqlalchemy_utils.functions import database_exists, create_database
    engin_uri = app.config.get('SQLALCHEMY_DATABASE_URI')
    if not database_exists(engin_uri):
        create_database(engin_uri)


@manager.option(
    '-d', '--debug', action='store_true',
    help="Start the web server in debug mode")
@manager.option(
    '-n', '--no-reload', action='store_false', dest='no_reload',
    default=config.get("FLASK_USE_RELOAD"),
    help="Don't use the reloader in debug mode")
@manager.option(
    '-a', '--address', default=config.get("FLASK_WEBSERVER_ADDRESS"),
    help="Specify the address to which to bind the web server")
@manager.option(
    '-p', '--port', default=config.get("FLASK_WEBSERVER_PORT"),
    help="Specify the port on which to run the web server")
@manager.option(
    '-w', '--workers',
    default=config.get("GUNICORN_WORKERS", 2),
    help="Number of gunicorn web server workers to fire up")
@manager.option(
    '-t', '--timeout', default=config.get("GUNICORN_WEBSERVER_TIMEOUT"),
    help="Specify the timeout (seconds) for the gunicorn web server")
@manager.option(
    '-k', '--worker_type', default=config.get("GUNICORN_WEBSERVER_WORKER_TYPE"),
    help="Select the gunicorn worker type")
def runserver(debug, no_reload, address, port, timeout, workers, worker_type):
    debug = debug or config.get("DEBUG")
    if debug:
        app.run(
            host=address,
            port=int(port),
            debug=True,
            use_reloader=no_reload)
    else:
        addr_str = " {address}:{port} "
        cmd = (
            "gunicorn "
            "-w {workers} "
            "-k {worker_type} "
            "--timeout {timeout} "
            "-b {address}:{port} "
            "--limit-request-line 0 "
            "--limit-request-field_size 0 "
            "--log-level debug "
            "manage:app").format(**locals())
        Popen(cmd, shell=True).wait()


if __name__ == "__main__":
    manager.run()