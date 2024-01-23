import unittest
import logging
from ruc_natural import RucNatural

test_data = [
    ["0PI-0-0", "57"],
    ["13PI-1-196", "58"],
    ["8PI-1-80", "05"],
    ["8PI-23-65", "91"],
    ["2PI-23-65", "41"],
    ["2PI-123-1234", "41"],
    ["2PI-1234-12345", "26"],
    ["2PI-1234-123", "33"],
    ["2PI-123-123456", "65"],
    ["2PI-1234-1234", "02"],
    ["8PI-1234-1234", "02"],
    ["8PI-1234-12345", "26"],
]

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logging level to INFO

# Create a console handler and set its level to INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Add the console handler to the logger
logger.addHandler(ch)


# RUC Natural Panameño Indigena (PI)
class TestRucNaturalPI(unittest.TestCase):
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
