from liuyanban.views import app
from liuyanban.models import db

command = input(">>>")


if command == "runserver":
    app.run(debug=True)
elif command == "migrate":
    db.create_all()