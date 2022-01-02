from resources.actors import ActorListApi
from resources.films import FilmListApi
from resources.smoke import Smoke


def create_routes(api):
    api.add_resource(Smoke, '/smoke', strict_slashes=False)
    api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
    api.add_resource(ActorListApi, '/actors', '/actors/<id>', strict_slashes=False)
