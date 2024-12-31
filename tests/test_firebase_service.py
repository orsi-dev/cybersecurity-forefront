import pytest

from src.core.services.authentication.firebase_service import FirebaseService


@pytest.fixture
def mock_adapter():
    class MockAdapter:
        def create_user(self, email, password, display_name):
            return {"uid": "123", "email": email, "display_name": display_name}

    return MockAdapter()


@pytest.mark.asyncio
async def test_register_user(mock_adapter):
    service = FirebaseService(mock_adapter)
    result = await service.register_user("test@example.com", "password", "Test User")
    assert result["email"] == "test@example.com"
    assert result["display_name"] == "Test User"
