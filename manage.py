import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import app, db
from models import Unigram


app.config.from_object(os.environ['APP_SETTINGS'])

from models import *
migrate = Migrate(app, db)
manager = Manager(app)

def make_shell_context():
	return dict(app=app, db=db, Unigram=Unigram)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
