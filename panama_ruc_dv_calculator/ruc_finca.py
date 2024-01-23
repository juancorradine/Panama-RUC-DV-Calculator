from panama_ruc_dv_calculator import calculate_dv_digit
from dataclasses import dataclass


# TODO: DV Calculation not working
@dataclass
class RucFinca:
    ruc: str

    def __post_init__(self):
        self._validate_input()
        self._calculate_dv()

    def _validate_input(self):
        ruc = self.ruc.replace(' ', '').upper()

        ruc_parts = ruc.split("-")

        if len(ruc_parts) != 2:
            raise ValueError("Formato de RUC Finca incorrecto.")

        finca = ruc_parts[0]
        codigo_ubicacion = ruc_parts[1]

        if not finca.isnumeric() or len(finca) > 10:
            raise ValueError("Formato de RUC Finca incorrecto - Finca: " + finca)
        if not codigo_ubicacion.isnumeric() or len(codigo_ubicacion) > 4:
            raise ValueError("Formato de RUC Finca incorrecto - Codigo de Ubicacion: " + codigo_ubicacion)

        self.ruc = ruc
        self.finca = finca
        self.codigo_ubicacion = codigo_ubicacion

    def _calculate_dv(self):
        ructb = "0".zfill(6) + self.finca.zfill(10) + self.codigo_ubicacion.zfill(4)

        dv1 = calculate_dv_digit.calculate(old_ruc=False, ructb=ructb)
        dv2 = calculate_dv_digit.calculate(old_ruc=False, ructb=ructb + dv1)

        self._ructb = ructb
        self._dv1 = dv1
        self._dv2 = dv2
        self.dv = dv1 + dv2
