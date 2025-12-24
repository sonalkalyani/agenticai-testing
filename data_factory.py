"""Data factory for generating booking payloads using Faker."""

from datetime import date
import random

from faker import Faker


class BookingDataFactory:
    """Factory to generate valid booking payloads that respect business rules."""

    def __init__(self, seed: int | None = None) -> None:
        self.faker = Faker()
        if seed is not None:
            # Allow deterministic data generation for reproducible tests.
            self.faker.seed_instance(seed)
            random.seed(seed)

    def generate_valid_booking(self) -> dict:
        """Create a booking payload with valid values and proper formats."""
        check_in = self.faker.date_between(start_date="+1d", end_date="+30d")
        return {
            "guest_name": self.faker.name(),
            "guest_count": random.randint(1, 4),
            # Ensure date formatted as YYYY-MM-DD
            "check_in_date": check_in.strftime("%Y-%m-%d")
            if isinstance(check_in, date)
            else str(check_in),
            "room_type": random.choice(["DELUXE", "STANDARD", "SUITE"]),
            # Include type and simulated valid credit card number
            "payment_method": {
                "type": "CREDIT_CARD",
                "card_number": self.faker.credit_card_number(),
            },
        }
