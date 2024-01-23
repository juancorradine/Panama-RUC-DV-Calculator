import calculate_dv_digit
from provincia import Provincia
from dataclasses import dataclass


@dataclass
class RucNaturalNT:
    ruc: str

    def __post_init__(self):
        self._validate_input()
        self._calculate_dv()

    def _validate_input(self):
        ruc = self.ruc.replace(' ', '').upper()

        if ruc.count('-') != 3:
            raise ValueError("Formato de RUC Natural NT incorrecto.")

        ruc_parts = ruc.split("-")

        if len(ruc_parts) != 4 or ruc_parts[1] != "NT":
            raise ValueError("Formato de RUC Natural NT incorrecto.")

        provincia = Provincia.from_code(ruc_parts[0])
        folio_imagen = ruc_parts[2]
        asiento_ficha = ruc_parts[3]

        if not folio_imagen.isnumeric() or len(folio_imagen) > 3:
            raise ValueError("Formato de RUC Natural NT incorrecto - Folio/Imagen: " + folio_imagen)
        if not asiento_ficha.isnumeric() or len(asiento_ficha) > 6:
            raise ValueError("Formato de RUC Natural NT incorrecto - Asiento/Ficha: " + asiento_ficha)

        self.ruc = ruc
        self.provincia = provincia
        self.folio_imagen = folio_imagen
        self.asiento_ficha = asiento_ficha

    def _calculate_dv(self):
        if len(self.asiento_ficha) <= 5:
            ructb = "0".zfill(7) + "5" + self.provincia.codigo.zfill(2) + "43" + \
                    self.folio_imagen.zfill(3) + self.asiento_ficha.zfill(5)
        else:
            ructb = "0".zfill(6) + "5" + self.provincia.codigo.zfill(2) + "43" + \
                    self.folio_imagen.zfill(3) + self.asiento_ficha.zfill(6)
        dv1 = calculate_dv_digit.calculate(old_ruc=False, ructb=ructb)
        dv2 = calculate_dv_digit.calculate(old_ruc=False, ructb=ructb + dv1)


        self._ructb = ructb
        self._dv1 = dv1
        self._dv2 = dv2
        self.dv = dv1 + dv2
