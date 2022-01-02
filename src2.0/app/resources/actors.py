from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.database.models import Actor
from src.shemas.actors import ActorSchema


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, id=None):
        if not id:
            actor = db.session.query(Actor).all()
            return self.actor_schema.dump(actor, many=True), 200
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return "", 400
        return self.actor_schema.dump(actor), 200

    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    def put(self, id):
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return '', 400
        try:
            actor = self.actor_schema.load(request.json, instance=True, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 400

    def delete(self, id):
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return '', 400
        db.session.delete(actor)
        db.session.commit()
        return '', 204