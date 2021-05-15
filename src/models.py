from peewee import Model, CharField, TextField, BooleanField, ForeignKeyField, MySQLDatabase

remote_db = MySQLDatabase(None)


class BaseModel(Model):
    class Meta:
        database = remote_db


class Paint(BaseModel):
    Code = CharField(max_length=10)
    Artist = CharField(max_length=300)
    Year = CharField(max_length=4)
    Location = CharField(max_length=200)
    Image = TextField()
    Link = CharField(max_length=500)
    ExistWikiDescription = BooleanField(default=False)


class Description(BaseModel):
    Language = CharField(max_length=2)
    Name = CharField(max_length=300)
    Pseudonym = CharField(max_length=300)
    Medium = CharField(max_length=300)
    Description = TextField()
    Paint = ForeignKeyField(Paint, backref='Descriptions')
