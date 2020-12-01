from liuyanban import db
from datetime import datetime


class Tips(db.Model):
    __tablename__ = 'tips'
    id = db.Column(db.Integer,primary_key=True)
    poster = db.Column(db.String(20))
    body = db.Column(db.String(200))
    posttime = db.Column(db.DateTime,default=datetime.now,index=True)

    def __repr__(self):
        return '<Tips {} by {}>'.format(self.id,self.poster)