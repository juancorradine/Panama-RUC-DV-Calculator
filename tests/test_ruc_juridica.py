import unittest
import logging
from panama_ruc_dv_calculator.ruc_juridica import RucJuridica

test_data = [
    ["0-0-0", "19"],  # Error
    ["2588017-1-831938", "20"],
    ["1489806-1-645353", "68"],
    ["1956569-1-732877", "00"],
    ["797609-1-493865", "12"],
    ["15565624-2-2017", "63"],
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
class TestRucJuridica(unittest.TestCase):
    def test_dv_calculation(self):
        for item in test_data:
            with self.subTest():
                try:
                    self.assertEqual(RucJuridica(item[0]).dv, item[1])
                    logger.info(f"✔ {item[0]}")
                except AssertionError:
                    logger.error(f"✖ {item[0]} → {RucJuridica(item[0]).dv} vs {item[1]}")


if __name__ == "__main__":
    unittest.main()
