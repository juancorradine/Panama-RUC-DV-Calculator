import unittest
import logging
from ruc_natural import RucNatural

test_data = [
    ["N-0-0", "76"],
    ["N-19-1821", "11"],
    ["N-1-24", "89"],
    ["N-1234-12345", "00"],
    ["N-7824-53189", "73"],
    ["N-9624-41065", "63"],
    ["N-6521-53249", "72"],
]

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logging level to INFO

# Create a console handler and set its level to INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Add the console handler to the logger
logger.addHandler(ch)


# RUC Persona Natural Naturalizado (N)
class TestRucNaturalN(unittest.TestCase):
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
