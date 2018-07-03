from .. import db, flask_bcrypt


class User(db.Document):
    email = db.StringField(db_field="email", unique=True, nullable=False)
    registered_on = db.DateTimeField(db_field="registered_on", nullable=False)
    admin = db.BooleanField(db_field="admin", nullable=False, default=False)
    public_id = db.StringField(db_field="public_id", unique=True)
    username = db.StringField(db_field="username", unique=True)
    password_hash = db.StringField(db_field="password_hash")

    meta = {
        'collection': 'users',
        'indexes': ['-registered_on']
    }

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)