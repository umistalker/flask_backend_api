import datetime
import uuid

from werkzeug.security import generate_password_hash

from src import db

movies_actors = db.Table(
    'movies_actors',
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'), primary_key=True),
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True)
)

contacts_actors = db.Table(
    'contact_actors',
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id')),
    db.Column('contact_id', db.Integer, db.ForeignKey('contacts.id'))
)


class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Date, index=True, nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.Text)
    distributed_by = db.Column(db.String(128), nullable=False)
    length = db.Column(db.Float)
    rating = db.Column(db.Float)
    is_released = db.Column(db.Boolean)
    actors = db.relationship('Actor', secondary=movies_actors, lazy='subquery', backref=db.backref('films', lazy=True))

    def __init__(self, title, release_date, description, distributed_by, length, rating, actors=None):
        self.title = title
        self.release_date = release_date
        self.uuid = str(uuid.uuid4())
        self.description = description
        self.distributed_by = distributed_by
        self.length = length
        self.rating = rating
        if not actors:
            self.actors = []
        else:
            self.actors = actors
        if datetime.date.today() >= self.release_date:
            self.is_released = True
        else:
            self.is_released = False

    def __repr__(self):
        return f'Film({self.title}, {self.release_date}, {self.uuid}, {self.distributed_by}, {self.actors})'


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    birthday = db.Column(db.Date, index=True, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    contacts = db.relationship('Contact', secondary=contacts_actors, backref=db.backref('actors', lazy='dynamic'))

    def __init__(self, name, birthday, is_active, contacts):
        self.name = name
        self.birthday = birthday
        self.is_active = is_active
        if contacts:
            self.contacts = contacts
        else:
            self.contacts = []

    def __repr__(self):
        return f"Actor({self.name}, {self.birthday})"


class Cascadeur(db.Model):
    __tablename__ = 'cascadeur'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    is_active = db.Column(db.Boolean, index=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))
    actor = db.relationship('Actor', backref=db.backref('cascadeur', uselist=False))

    def __init__(self, name, is_active):
        self.name = name
        self.is_active = is_active

    def __repr__(self):
        return f"Cascadeur({self.name}, {self.is_active})"


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String)
    address = db.Column(db.String)

    def __init__(self, phone_number, address):
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return f"Contact({self.phone_number}, {self.address})"


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(254), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    uuid = db.Column(db.String(36), unique=True)

    def __init__(self, username, email, password, is_admin):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.uuid})'

    @classmethod
    def find_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_user_by_uuid(cls, uuid):
        return cls.query.filter_by(uuid=uuid).first()