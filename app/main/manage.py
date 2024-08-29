import os
import unittest
from flask import Flask
from flask_migrate import Migrate
from app.main import create_app, db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

migrate = Migrate(app, db)

@app.cli.command('run')
def run():
    """Run the Flask development server."""
    app.run()

@app.cli.command('test')
def test():
    """Run unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    app.run()
