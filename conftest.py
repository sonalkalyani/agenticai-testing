"""
Pytest configuration and shared fixtures for OHIP Partner Booking API v2 tests
"""

import pytest

from data_factory import BookingDataFactory


@pytest.fixture
def base_url():
    """
    Base URL for the OHIP Partner Booking API v2.
    For these tests we use httpbin as a demo endpoint.
    """
    return "https://httpbin.org"


@pytest.fixture
def valid_oauth_token():
    """
    Valid OAuth 2.0 Bearer Token for testing
    Update this with actual token or token generation logic
    """
    return "valid_oauth_token_here"


@pytest.fixture
def invalid_oauth_token():
    """
    Invalid OAuth 2.0 Bearer Token for negative testing
    """
    return "invalid_token_12345"


@pytest.fixture
def expired_oauth_token():
    """
    Expired OAuth 2.0 Bearer Token for testing
    """
    return "expired_token_here"


@pytest.fixture
def test_partner_id():
    """
    Test partner ID for booking requests
    """
    return "TEST_PARTNER_001"


@pytest.fixture
def valid_booking_payload():
    """
    Static valid booking payload for happy path tests
    (kept for backward compatibility with existing tests).
    """
    return {
        "guest_count": 2,
        "check_in_date": "2024-12-25",
        "check_out_date": "2024-12-27",
        "room_type": "STANDARD",
        "payment_method": "CREDIT_CARD",
        "guest_name": "John Doe",
        "guest_email": "john.doe@example.com",
    }


@pytest.fixture
def booking_payload():
    """
    Dynamic booking payload using BookingDataFactory.
    Returns a single dictionary from generate_valid_booking().
    """
    factory = BookingDataFactory()
    return factory.generate_valid_booking()


@pytest.fixture
def database_connection():
    """
    Database connection fixture for database verification tests
    Update with actual database connection logic
    """
    # Example: return database connection object
    # import mysql.connector
    # return mysql.connector.connect(...)
    pass


@pytest.fixture
def rate_limit_threshold():
    """
    Rate limit threshold (100 requests per minute)
    """
    return 100


@pytest.fixture
def rate_limit_window_seconds():
    """
    Rate limit time window in seconds (60 seconds = 1 minute)
    """
    return 60

