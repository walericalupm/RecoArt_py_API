from peewee import Model, CharField, IntegerField, TextField, ForeignKeyField
from app import db


class BaseModel(Model):
    class Meta:
        database = db


class Paint(BaseModel):
    Code = CharField(max_length=10)
    Artist = CharField(max_length=300)
    Year = CharField(max_length=4)
    Location = CharField(max_length=200)
    Image = TextField()
    Link = CharField(max_length=500)


class Description(BaseModel):
    Language = IntegerField()
    Name = CharField(max_length=300)
    Pseoudoname = CharField(max_length=300)
    Medium = CharField(max_length=300)
    Description = TextField()
    Paint = ForeignKeyField(Paint, backref='Descriptions')
