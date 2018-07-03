from .. import db


class User(db.Document):
    email = db.StringField(db_field="email", unique=True, nullable=False)
    registered_on = db.DateTimeField(db_field="registered_on", nullable=False)
    admin = db.BooleanField(db_field="admin", nullable=False, default=False)
    public_id = db.StringField(db_field="public_id", unique=True)
    username = db.StringField(db_field="username", unique=True)
    password = db.StringField(db_field="password")

    meta = {
        'strict': False,
        'collection': 'users',
        'indexes': ['-registered_on']
    }

    def __repr__(self):
        return "<User '{}'>".format(self.username)
