from server import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

user_region_assoc = db.Table("association", db.Model.metadata,
                             db.Column("user_id", db.Integer,
                                       db.ForeignKey("user.id")),
                             db.Column("region_id", db.Integer,
                                       db.ForeignKey("region.id"))
                             )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))


class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(140))
    date = db.Column(db.String(140))
    location_type = db.Column(db.String(140))
    data_field = db.Column(db.String(140))
    data_field_code = db.Column(db.String(140))
    time_period = db.Column(db.String(140))
    time_period_type = db.Column(db.String(140))
    value = db.Column(db.String(140))
    unit = db.Column(db.String(140))
    geometry = db.Column(db.String(140))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
