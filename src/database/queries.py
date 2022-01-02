from src import db
from src.database import models

join_tables = db.session.query(models.Film).join(models.Film.actors).all()

print(join_tables)