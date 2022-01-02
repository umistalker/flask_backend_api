from flask_restful import Resource
from sqlalchemy import func

from src import db
from src.database.models import Film


class AggregationApi(Resource):
    def get(self):
        films_count = db.session.query(func.count(Film.id)).scalar()
        films_rating_max = db.session.query(func.max(Film.rating)).scalar()
        films_rating_min = db.session.query(func.min(Film.rating)).scalar()
        films_rating_avg = db.session.query(func.avg(Film.rating)).scalar()
        return {
            'count': films_count,
            'max': films_rating_max,
            'min': films_rating_min,
            'avg': films_rating_avg
        }
