import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import ( create_author, get_all_authors_json, get_all_authors )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')


'''
Generic Commands
'''

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)

'''
Author Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask author <command>
author_cli = AppGroup('author', help='Author object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@author_cli.command("create", help="Creates an author.")
@click.argument("fname", default="Nicholas")
@click.argument("lname", default="Mendez")
@click.argument("email", default="nmendez@gmail.com")
@click.argument("password", default="mendez15cool!")
def create_author_command(fname, lname, email, password):
    create_author(fname, lname, email, password)
    print(f'Author {fname} {lname} created with email {email}!')

# this command will be : flask user create bob bobpass

@author_cli.command("list", help="Lists authors in the database")
@click.argument("format", default="string")
def list_author_command(format):
    if format == 'string':
        print(get_all_authors())
    else:
        print(get_all_authors_json())

app.cli.add_command(author_cli) # add the group to the cli