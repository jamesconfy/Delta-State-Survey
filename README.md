# Delta State Survey Application

## This is a application that deals with surveyed land

To get the app up and running. [Clone it using this link](https://github.com/jamesconfy/Delta-State-Survey.git). You can do this by opening up a terminal on your system and typing `git clone https://github.com/jamesconfy/Delta-State-Survey.git`.

After it is done cloning, you create a virtual environment and activate it with this command `python3 -m venv .venv && source .venv/bin/activate`. This is assuming you have the latest version of Python (3.11 as of the writing of this documentation), if not you can download it using this link: [python](https://www.python.org/downloads/).

The next step is to upgrade pip, this can be done with the command `pip install --upgrade pip`.
After pip is done upgrading, you install the requirements.txt file using `pip install -r requirements.txt`

After going through all those set-ups, you are ready to start the app, but do not forget to create an app.env file using the app-sample.env provided for you, copy the variables and provide what is required (in this case it is just your database configuration and a secret key).

You can finally run `python3 run.py` to start the app in development mode, or `gunicorn run:app` for production mode.
