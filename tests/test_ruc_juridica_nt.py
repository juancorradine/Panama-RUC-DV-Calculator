import unittest
import logging
from panama_ruc_dv_calculator.ruc_juridica_nt import RucJuridicaNT

test_data = [
    ["0-NT-0-0", "31"],
    ["8-NT-1-13656", "43"],
    ["1-NT-45-56544", "03"],
    ["5-NT-478-2351", "94"],
    ["7-NT-102-33575", "03"],
    ["11-NT-958-2182101", "82"],
    ["8-NT-1-1234567", "49"],
    ["11-NT-958-218210", "73"],
    ["11-NT-958-2182104", "82"],
    ["8-NT-1-123456", "52"],
]

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logging level to INFO

# Create a console handler and set its level to INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Add the console handler to the logger
logger.addHandler(ch)


# RUC Persona Juridica
class TestRucJuridicaNT(unittest.TestCase):
    def test_dv_calculation(self):
        for item in test_data:
            with self.subTest():
                try:
                    self.assertEqual(RucJuridicaNT(item[0]).dv, item[1])
                    logger.info(f"✔ {item[0]}")
                except AssertionError:
                    logger.error(f"✖ {item[0]} → {RucJuridicaNT(item[0]).dv} vs {item[1]}")


if __name__ == "__main__":
    unittest.main()
