# cp_class_project

firstly setup an virtual enviornment using fallowing command in terminal while making shure that you are in correct directory

> virtualenv venv -p python 

to activate venv enter fallowing command

>.\venv\Scripts\activate.bat

now install pandas ,google_genrativeai ,flask ,flask_sqlalchemy

>pip install pandas

>pip install google -q -U google-genrativeai

>pip install flask

>pip install flask_sqlalchemy

now after installing all the libs add a database file

> from app import app, db
> app.app_context().push()
> db.create_all()

now run the app.py file now open link mostlikely  'http://127.0.0.1:5000'

