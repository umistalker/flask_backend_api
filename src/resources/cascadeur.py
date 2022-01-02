from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.database.models import Cascadeur
from src.shemas.cascadeur import CascadeurSchema


class CascadeurListApi(Resource):
    cascadeur_schema = CascadeurSchema()

    def get(self, id=None):
        if not id:
            cascadeur = db.session.query(Cascadeur).all()
            return self.cascadeur_schema.dump(cascadeur, many=True), 200
        cascadeur = db.session.query(Cascadeur).filter_by(id=id).first()
        if not cascadeur:
            return "", 400
        return self.cascadeur_schema.dump(cascadeur), 200

    def post(self):
        try:
            cascadeur = self.cascadeur_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(cascadeur)
        db.session.commit()
        return self.cascadeur_schema.dump(cascadeur), 200

    def put(self, id):
        cascadeur = db.session.query(Cascadeur).filter_by(id=id).first()
        if not cascadeur:
            return '', 400
        try:
            cascadeur = self.cascadeur_schema.load(request.json, instance=True, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(cascadeur)
        db.session.commit()
        return self.cascadeur_schema.dump(cascadeur), 400

    def delete(self, id):
        actor = db.session.query(Cascadeur).filter_by(id=id).first()
        if not actor:
            return '', 400
        db.session.delete(actor)
        db.session.commit()
        return '', 204