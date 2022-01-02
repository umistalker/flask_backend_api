from src.database.models import Film


class FilmServices:
    @staticmethod
    def get_all_film(session):
        return session.query(Film)

    @classmethod
    def get_film_by_uuid(cls, session, uuid):
        return cls.get_all_film(session).filter_by(
            uuid=uuid
        ).first()