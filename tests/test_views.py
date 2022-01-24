import pytest
from rest_framework.test import APIClient

class TestGamesView:
    @pytest.mark.django_db
    def test_games_views_if_request_is_correct(self):
        client = APIClient()
        response = client.get(path='/games/', format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_games_views_if_search_request_has_no_key_and_value(self):
        client = APIClient()
        response = client.get(path='/games/search/', format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_games_views_if_search_request_has_incorrect_key(self):
        client = APIClient()
        response = client.get(path='/games/search/?key=incorrect_key_name&value=some_value', format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_games_views_if_search_result_is_empty(self):
        client = APIClient()
        response = client.get(path='/games/search/?key=platform&value=some_value', format='json')
        assert response.status_code == 204


class TestBooksView:
    @pytest.mark.django_db
    def test_books_views_if_request_is_correct(self):
        client = APIClient()
        response = client.get(path='/books/', format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_books_views_if_search_request_has_no_key_and_value(self):
        client = APIClient()
        response = client.get(path='/books/search/', format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_books_views_if_search_request_has_incorrect_key(self):
        client = APIClient()
        response = client.get(path='/books/search/?key=incorrect_key_name&value=some_value', format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_books_views_if_search_result_is_empty(self):
        client = APIClient()
        response = client.get(path='/books/search/?key=type&value=some_value', format='json')
        assert response.status_code == 204


class TestVideosView:
    @pytest.mark.django_db
    def test_videos_views_if_request_is_correct(self):
        client = APIClient()
        response = client.get(path='/videos/', format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_videos_views_if_search_request_has_no_key_and_value(self):
        client = APIClient()
        response = client.get(path='/videos/search/', format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_videos_views_if_search_request_has_incorrect_key(self):
        client = APIClient()
        response = client.get(path='/videos/search/?key=incorrect_key_name&value=some_value', format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_videos_views_if_search_result_is_empty(self):
        client = APIClient()
        response = client.get(path='/videos/search/?key=type&value=some_value', format='json')
        assert response.status_code == 204
