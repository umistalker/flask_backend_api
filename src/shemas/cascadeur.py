from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from src.database.models import Actor, Cascadeur


class CascadeurSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cascadeur
        load_instance = True
        include_fk = True
