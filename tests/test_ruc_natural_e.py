import unittest
import logging
from panama_ruc_dv_calculator.ruc_natural import RucNatural

test_data = [
    ["E-0-0", "75"],
    ["E-8-127702", "16"],
    ["E-8-127703", "05"],
    ["E-8-127702", "16"],
    ["E-8-12770", "72"],
    ["E-1234-12770", "98"],
    ["E-1235-12770", "23"],
    ["E-1-11", "63"],
    ["E-7824-53189", "90"],
    ["E-9624-41065", "80"],
    ["E-6521-53249", "99"],
    ["E-5056-27219", "16"],
    ["E-123-1277012", "65"],
    ["E-8-96407", "29"],
    ["E-1234-123456789", "26"]
]

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logging level to INFO

# Create a console handler and set its level to INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Add the console handler to the logger
logger.addHandler(ch)


# RUC Persona Natural Extranjero (E)
class TestRucNaturalE(unittest.TestCase):
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
