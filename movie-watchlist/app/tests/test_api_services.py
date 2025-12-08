import pytest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException

from app.services.api_service import APIService


class TestAPIService:
    """Test cases for APIService class."""

    def test_fetch_movie_data_no_api_key(self):
        """Test that HTTPException is raised when API key is not provided."""
        service = APIService(api_key="")
        
        with pytest.raises(HTTPException) as exc_info:
            service.fetch_movie_data("Inception")
        
        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "API key is not provided."

    def test_fetch_movie_data_none_api_key(self):
        """Test that HTTPException is raised when API key is None."""
        service = APIService(api_key=None)
        
        with pytest.raises(HTTPException) as exc_info:
            service.fetch_movie_data("Inception")
        
        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "API key is not provided."

    @patch("app.services.api_service.save_movie_data")
    @patch("app.services.api_service.requests.get")
    def test_fetch_movie_data_success(self, mock_get, mock_save):
        """Test successful movie data fetch."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "title": "Inception",
            "year": 2010,
            "director": "Christopher Nolan"
        }
        mock_get.return_value = mock_response
        
        service = APIService(api_key="test_api_key")
        result = service.fetch_movie_data("Inception")
        
        assert result["title"] == "Inception"
        assert result["year"] == 2010
        mock_get.assert_called_once()
        mock_save.assert_called_once_with(result)

    @patch("app.services.api_service.requests.get")
    def test_fetch_movie_data_api_error(self, mock_get):
        """Test HTTPException is raised when API returns error status."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        service = APIService(api_key="test_api_key")
        
        with pytest.raises(HTTPException) as exc_info:
            service.fetch_movie_data("NonExistentMovie")
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Error fetching movie data."

    @patch("app.services.api_service.requests.get")
    def test_fetch_movie_data_server_error(self, mock_get):
        """Test HTTPException is raised when API returns 500 error."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        service = APIService(api_key="test_api_key")
        
        with pytest.raises(HTTPException) as exc_info:
            service.fetch_movie_data("Inception")
        
        assert exc_info.value.status_code == 500

    @patch("app.services.api_service.requests.get")
    def test_fetch_movie_data_correct_url(self, mock_get):
        """Test that the correct URL is constructed."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response
        
        with patch("app.services.api_service.save_movie_data"):
            service = APIService(api_key="my_secret_key")
            service.fetch_movie_data("The Matrix")
        
        expected_url = "https://api.example.com/movies?title=The Matrix&api_key=my_secret_key"
        mock_get.assert_called_once_with(expected_url)