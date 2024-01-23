import unittest
import logging
from ruc_natural import RucNatural

test_data = [
    ["0AV-0-0", "10"],
    ["8AV-1-196", "90"],
    ["2AV-1234-12345", "26"],
    ["2AV-1234-123", "33"],
    ["2AV-123-123456", "28"],
    ["8AV-123-123456", "78"],
    ["2AV-1234-1234", "02"],
]

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logging level to INFO

# Create a console handler and set its level to INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Add the console handler to the logger
logger.addHandler(ch)


# RUC Persona Natural Antes de Vigencia (AV)
class TestRucNaturalAV(unittest.TestCase):
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
