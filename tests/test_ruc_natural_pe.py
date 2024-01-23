import unittest
import logging
from ruc_natural import RucNatural

test_data = [
    ["PE-0-0", "14"],
    ["PE-1-19", "60"],
    ["PE-123-12345", "42"],
    ["PE-842-3681", "51"],
    ["PE-712-5789", "82"],
    ["PE-523-8262", "37"],
]

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logging level to INFO

# Create a console handler and set its level to INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Add the console handler to the logger
logger.addHandler(ch)


# RUC Persona Natural Panameño Extranjero (PE)
class TestRucNaturalPE(unittest.TestCase):
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
