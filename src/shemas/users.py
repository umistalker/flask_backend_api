from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.database.models import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('id',)
        load_instance = True
        load_only = ('password',)
