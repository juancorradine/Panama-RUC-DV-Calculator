import unittest
import logging
from panama_ruc_dv_calculator.ruc_juridica import RucJuridica

test_data = [
    ["10102-64-103462", "30"],
    ["1102-85-117211", "95"],
    ["41425-516-58123", "41"],
    ["32425-254-85621", "68"],
    ["12388-184-921", "62"],
]

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logging level to INFO

# Create a console handler and set its level to INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Add the console handler to the logger
logger.addHandler(ch)


# RUC Persona Juridica Antiguo
class TestRucJuridicaAntiguo(unittest.TestCase):
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
