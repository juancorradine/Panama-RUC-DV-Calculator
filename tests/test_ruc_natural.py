import unittest
import logging
from ruc_natural import RucNatural

test_data = [
    ["0-0-0", "7C"],
    ["8-769-1080", "56"],
    ["5-257-218", "09"],
    ["6-108-289", "79"],
    ["8-28-1284", "33"],
    ["2-7-89", "20"],
    ["2-1234-123456789", "01"],
]

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logging level to INFO

# Create a console handler and set its level to INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Add the console handler to the logger
logger.addHandler(ch)


# RUC Persona Natural
class TestRucNatural(unittest.TestCase):
    def test_dv_calculation(self):
        for item in test_data:
            with self.subTest():
                try:
                    self.assertEqual(RucNatural(item[0]).dv, item[1])
                    logger.info(f"✔ {item[0]}")
                except AssertionError:
                    logger.error(f"✖ {item[0]} → {RucNatural(item[0]).dv} vs {item[1]}")


if __name__ == "__main__":
    unittest.main()
