import click
from faker import Faker
from liuyanban.models import Tips,db
from liuyanban import app


@app.cli.command()
def initdb():
    db.create_all()
    click.echo("Initialized database.")


@app.cli.command()
@click.option('--count',default=20,help="Quantity of tips,default is 20.")
def fakerdata(count):
    db.drop_all()
    db.create_all()
    fake = Faker()
    click.echo("working...")

    for i in range(count):
        tip = Tips(poster=fake.name(),body=fake.sentence(),posttime=fake.date_time_this_year())
        db.session.add(tip)
    db.session.commit()
    click.echo("Created {} fake tips.".format(count))


def fakerdatafun(count):
    fake = Faker('zh-CN')
    print("working...")

    for i in range(count):
        tip = Tips(poster=fake.name(),body=fake.sentence(),posttime=fake.date_time_this_year())
        db.session.add(tip)
    db.session.commit()
    print("Created {} fake tips.".format(count))
