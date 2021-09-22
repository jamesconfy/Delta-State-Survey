# Delta-State-Survey
Codes to take, validate and store a user using:
- Python(Flask)
- Flask-SQLALCHEMY(Database)
- Bootstrap CSS

### Setting up workspace
You need a text editor with a python extention to startup. If you don't have python extention, you can download from [Python](www.python.org) official page. And set it up in the editor you decide to use be it [VSCode](code.visualstudio.com), [Atom](atom.io), [Sublime Text](www.sublimetext.com) e.t.c.

### Python Modules Required
- Flask
- flask_bcrypt
- flask wtforms
- flask login
- flask-sqlalchemy

### Installation
You can either use pip to install each individual module or download from source codes which can be gotten from [Python Website](www.python.org). But it is advisable to use pip on the command line.
You can do this by using the process below on your command line:
```sh
$ pip install flask
$ pip install flask-bcrypt
$ pip install flask-wtf
$ pip install flask-login
$ pip install flask-sqlalchemy
$ pip install email_validator
$ pip install datetime(used for setting cookie time and also to verify the date of survey input)
```

### How To Run Code
To set up the server, make sure all your packages above are installed or else you could be faced with a lot of errors.

To start it up, pull up the terminal in text editor(or command line) you are currently using, the directory should be set to the directory where the code is located at, and run the code below:
```sh
python app.py
```
This should start up the server in debug mode but in a lazy environment(not good in production).

Preview of what to expect after successfully running the code:

![Image showing preview of code to see](https://github.com/jamesconfy/Login_Validation/blob/main/static/assests/login_validation.PNG?raw=true)
