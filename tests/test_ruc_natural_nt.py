import unittest
import logging
from ruc_natural_nt import RucNaturalNT

test_data = [
    ["0-NT-0-0", "09"],
    ["8-NT-1-24", "33"],
    ["3-NT-465-45624", "03"],
    ["9-NT-2-421578", "50"],
    ["6-NT-227-888555", "09"],
    ["12-NT-45-2154", "17"],
]

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logging level to INFO

# Create a console handler and set its level to INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Add the console handler to the logger
logger.addHandler(ch)


# RUC Persona Natural NT
class TestRucNaturalNT(unittest.TestCase):
    def test_dv_calculation(self):
        for item in test_data:
            with self.subTest():
                try:
                    self.assertEqual(RucNaturalNT(item[0]).dv, item[1])
                    logger.info(f"✔ {item[0]}")
                except AssertionError:
                    logger.error(f"✖ {item[0]} → {RucNaturalNT(item[0]).dv} vs {item[1]}")


if __name__ == "__main__":
    unittest.main()
