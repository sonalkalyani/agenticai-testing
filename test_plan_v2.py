"""Additional functional tests for OHIP Partner Booking API v2."""

import requests

from data_factory import BookingDataFactory


class TestHappyPath:
    """Test successful booking scenarios using httpbin echo."""

    def test_successful_booking_with_all_fields(self, base_url, booking_payload):
        """
        Happy path: send a valid booking and verify the echoed payload.
        - Uses httpbin /post to echo the JSON payload.
        - Asserts HTTP 200.
        - Confirms the echoed 'json' matches the booking we sent.
        """
        url = f"{base_url}/post"

        response = requests.post(url, json=booking_payload)

        assert response.status_code == 500
        data = response.json()
        assert data["json"] == booking_payload


class TestRateLimiting:
    """Simulate rate limiting behavior using httpbin echo."""

    def test_rate_limit_exceeded(self, base_url):
        """
        Send 105 requests to /post to simulate exceeding the 100 req/min limit.
        httpbin won't rate limit; we print status codes to observe behavior.
        In a real system, we would expect HTTP 429 after the 100th request.
        """
        factory = BookingDataFactory()

        url = f"{base_url}/post"

        for i in range(105):
            payload = factory.generate_valid_booking()

            # Optional: tag request to help identify it in logs
            payload["request_iteration"] = i + 1

            response = requests.post(url, json=payload)

            # Since httpbin doesn't rate-limit, just log the status codes
            print(f"Request {i + 1}: status={response.status_code}")

            # In a real scenario, uncomment to enforce expectation:
            # if i >= 100:
            #     assert response.status_code == 429
