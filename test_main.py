from fastapi.testclient import TestClient
from pydantic import ValidationError

from main import app, Translation

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_translation_model():
    # Valid data
    data = {
        "text": "Hello",
        "translated_text": "Bonjour",
        "source_language": "English",
        "target_language": "French"
    }
    translation = Translation(**data)
    assert translation.text == "Hello"
    assert translation.translated_text == "Bonjour"
    assert translation.source_language == "English"
    assert translation.target_language == "French"

    # Invalid data - missing required fields
    invalid_data = {
        "text": "Hello",
        "translated_text": "Bonjour"
    }
    try:
        invalid_translation = Translation(**invalid_data)
    except ValidationError as e:
        assert "source_language" in str(e)
        assert "target_language" in str(e)