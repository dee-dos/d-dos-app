import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import ( create_author, create_publication, delete_publication, get_all_authors_json, get_all_authors, get_author )

from App.models import *

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

'''
Publication Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask author <command>
pub_cli = AppGroup('pub', help='Publication object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@pub_cli.command("create", help="Creates a publication.")
@click.argument("name", default="A random fact about Software Engineering.")
@click.argument("author", default="1")
@click.argument("content", default="Something random about Software Engineering I chose to share randomly!")
@click.argument("citation", default="https://nicholasmendez.dev/")
def create_publication_command(name, author, content, citation):
    create_publication(name, author, content, citation)
    p = Publication(
        name=name,
        author=author,
        content=content,
        citation=citation
    )
    a = get_author(author)

    a.publications.append(p)

    print(f'Publication {name} created!')

# this command will be : flask user create bob bobpass
@pub_cli.command("delete", help="Removes a publication from the database")
@click.argument("id")
def delete_publication_command(id):
    delete_publication(id)
    print(f'Publication ID {id} deleted!')


@pub_cli.command("list", help="Lists publications in the database")
@click.argument("format", default="string")
def list_publication_command(format):
    if format == 'string':
        print(get_all_authors())
    else:
        print(get_all_authors_json())

app.cli.add_command(pub_cli) # add the group to the cli