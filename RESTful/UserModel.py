from main import db
from main import ma

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

class UserShema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'surname', 'email', 'hash', 'admin')
