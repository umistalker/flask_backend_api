import http
import json
from unittest.mock import patch

from src import app


class TestFilms:
    uuid = []

    def test_get_films_with_db(self):
        client = app.test_client()
        resp = client.get('/films')

        assert resp.status_code == http.HTTPStatus.OK

    @patch('src.services.film_services.FilmServices.get_all_film', autospec=True)
    def test_get_film_mock_db(self, mock):
        client = app.test_client()
        resp = client.get('/films')
        mock.assert_called_once()

        assert resp.status_code == http.HTTPStatus.OK
        assert len(resp.json) == 0

    def test_create_film_with_db(self):
        client = app.test_client()
        data = {
            'title': 'Test',
            'distributed_by': "Test",
            'release_date': '2010-04-01',
            'description': '',
            'length': 100,
            'rating': 0.0

        }
        resp = client.post('/films', data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.CREATED
        assert resp.json['title'] == 'Test'
        self.uuid.append(resp.json['uuid'])

    def test_update_film_with_db(self):
        client = app.test_client()
        url = f'/films/{self.uuid[0]}'
        data = {
            'title': 'Update',
            'distributed_by': "Update",
            'release_date': '2011-04-01',
            'description': 'Update'
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.OK
        assert resp.json['title'] == 'Update'

    def test_update_film_with_mock_db(self):
        with patch('src.services.film_services.FilmServices.get_film_by_uuid') as mock_uuid, \
                patch('src.db.session.add', autospec=True) as mock_add, \
                patch('src.db.session.commit', autospec=True) as mock_commit:
            client = app.test_client()
            url = f'/films/{self.uuid[0]}'
            data = {
                'title': 'Update',
                'distributed_by': "Update",
                'release_date': '2011-04-01',
                'description': 'Update'
            }
            resp = client.put(url, data=json.dumps(data), content_type='application/json')
            mock_add.assert_called_once()
            mock_commit.assert_called_once()
            mock_uuid.assert_called_once()

    def test_delete_films_with_db(self):
        client = app.test_client()
        url = f'/films/{self.uuid[0]}'
        resp = client.delete(url)
        assert resp.status_code == http.HTTPStatus.NO_CONTENT