# Import db from app factory
from app import create_app
from flask_script import Manager,Server

app = create_app('development')

# Create manager instance 
manager = Manager(app)

# Create migrate instance
# migrate = Migrate(app,db)

manager.add_command('server',Server)
# manager.add_command('db',MigrateCommand)

# @manager.command
# def test():
#     '''
#     Run the unit tests
#     '''
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)


# @manager.shell
# def make_shell_context():
#     return dict( app=app, db=db, User=User, Review=Review, Role=Role)


if __name__ == '__main__':
    manager.run()
