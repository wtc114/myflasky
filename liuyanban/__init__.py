from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app = Flask('liuyanban')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)



from liuyanban.views import app
from liuyanban.models import db

if __name__ == '__main__':
    app.run(debug=True)

