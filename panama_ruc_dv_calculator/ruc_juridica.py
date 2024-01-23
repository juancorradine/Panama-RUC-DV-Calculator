import calculate_dv_digit
from dataclasses import dataclass


@dataclass
class RucJuridica:
    ruc: str

    def __post_init__(self):
        self._validate_ruc_input()
        self._calculate_dv()

    def _validate_ruc_input(self):
        ruc = self.ruc.replace(' ', '').upper()

        if ruc.count('-') > 3 or ruc.count('-') < 2 or len(ruc) < 5:
            raise ValueError("Formato de RUC Juridica incorrecto.")

        ruc_parts = ruc.split("-")

        if len(ruc_parts) != 3:
            raise ValueError("Formato de RUC Juridica incorrecto.")

        rollo_tomo = ruc_parts[0]
        folio_imagen = ruc_parts[1]
        asiento_ficha = ruc_parts[2]

        if not rollo_tomo.isnumeric() or len(rollo_tomo) > 8:
            raise ValueError("Formato de RUC Juridica incorrecto - Rollo/Tomo: " + rollo_tomo)
        if not folio_imagen.isnumeric() or len(folio_imagen) > 4:
            raise ValueError("Formato de RUC Juridica incorrecto - Folio/Imagen: " + folio_imagen)
        if not asiento_ficha.isnumeric() or len(asiento_ficha) > 6:
            raise ValueError("Formato de RUC Juridica incorrecto - Asiento/Ficha: " + asiento_ficha)

        self.ruc = ruc
        self.rollo_tomo = rollo_tomo
        self.folio_imagen = folio_imagen
        self.asiento_ficha = asiento_ficha

    def _calculate_dv(self):
        ructb = self.rollo_tomo.zfill(10) + self.folio_imagen.zfill(4) + self.asiento_ficha.zfill(6)
        if ructb[3] == "0" and ructb[4] == "0" and ructb[5] < "5":
            self.is_ruc_antiguo = True
            # Referencia cruzada requerida para RUCs Antiguos
            ructb = ructb[:5] + old_ruc_cross_ref.get(ructb[5:7], ructb[5:7]) + ructb[7:]
        else:
            self.is_ruc_antiguo = False

        dv1 = calculate_dv_digit.calculate(old_ruc=self.is_ruc_antiguo, ructb=ructb)
        dv2 = calculate_dv_digit.calculate(old_ruc=self.is_ruc_antiguo, ructb=ructb + dv1)

        self._ructb = ructb
        self._dv1 = dv1
        self._dv2 = dv2
        self.dv = dv1 + dv2


old_ruc_cross_ref = {
    "00": "00",
    "10": "01",
    "11": "02",
    "12": "03",
    "13": "04",
    "14": "05",
    "15": "06",
    "16": "07",
    "17": "08",
    "18": "09",
    "19": "01",
    "20": "02",
    "21": "03",
    "22": "04",
    "23": "07",
    "24": "08",
    "25": "09",
    "26": "02",
    "27": "03",
    "28": "04",
    "29": "05",
    "30": "06",
    "31": "07",
    "32": "08",
    "33": "09",
    "34": "01",
    "35": "02",
    "36": "03",
    "37": "04",
    "38": "05",
    "39": "06",
    "40": "07",
    "41": "08",
    "42": "09",
    "43": "01",
    "44": "02",
    "45": "03",
    "46": "04",
    "47": "05",
    "48": "06",
    "49": "07"
}
