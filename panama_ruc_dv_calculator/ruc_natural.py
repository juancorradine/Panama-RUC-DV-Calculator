import calculate_dv_digit
from provincia import Provincia
from enum import Enum
from dataclasses import dataclass


class LetraRucNatural(Enum):
    SIN_LETRA = ("", "00", "00", "Sin Letra")
    EXTRANJERO = ("E", "5", "66", "Extranjero")
    PANAMENO_EXTRANJERO = ("PE", "75", "82", "Panameño Extranjero")
    NATURALIZADO = ("N", "4", "92", "Naturalizado")
    AV = ("AV", "15", "9595", "Antes de la Vigencia")
    PI = ("PI", "79", "9595", "Panameño Indigena")

    def __init__(self, letter, code, validation_code, name):
        self.letra = letter
        self.codigo = code
        self.codigo_validacion = validation_code
        self.nombre = name

    @classmethod
    def from_code(cls, letra: str):
        for member in cls:
            if member.letra == letra.upper():
                return member
        raise ValueError(f"Letra de RUC Natural invalido: {letra}")


@dataclass
class RucNatural:
    ruc: str

    def __post_init__(self):
        self._validate_ruc_input()
        self._calculate_dv()

    def _validate_ruc_input(self):
        ruc = self.ruc.replace(' ', '').upper()

        if ruc.count('-') != 2:
            raise ValueError("Formato de RUC Natural incorrecto.")

        ruc_parts = ruc.split("-")

        if ruc_parts[0] in (LetraRucNatural.EXTRANJERO.letra,
                            LetraRucNatural.PANAMENO_EXTRANJERO.letra,
                            LetraRucNatural.NATURALIZADO.letra):
            provincia = Provincia.EN_BLANCO
            letra = LetraRucNatural.from_code(ruc_parts[0])
            folio_imagen = ruc_parts[1]
            asiento_ficha = ruc_parts[2]
            folio_max_len = 4
            asiento_max_len = 9
        elif any(substring in ruc_parts[0] for substring in (LetraRucNatural.AV.letra,
                                                             LetraRucNatural.PI.letra)):
            provincia = Provincia.from_code(ruc_parts[0][:len(ruc_parts[0]) - 2])
            letra = LetraRucNatural.from_code(ruc_parts[0][-2:])
            folio_imagen = ruc_parts[1]
            asiento_ficha = ruc_parts[2]
            folio_max_len = 4
            asiento_max_len = 8
        elif ruc_parts[0].isdigit() or 0 < len(ruc_parts[0]) <= 2:
            provincia = Provincia.from_code(ruc_parts[0])
            letra = LetraRucNatural.from_code("")
            folio_imagen = ruc_parts[1]
            asiento_ficha = ruc_parts[2]
            folio_max_len = 4
            asiento_max_len = 9
        else:
            raise ValueError("Formato de RUC Natural incorrecto.")

        if not folio_imagen.isdigit() or len(folio_imagen) > folio_max_len:
            raise ValueError(f"Formato de RUC Natural incorrecto - Folio/Imagen: {folio_imagen}")
        if not asiento_ficha.isdigit() or len(asiento_ficha) > asiento_max_len:
            raise ValueError(f"Formato de RUC Natural incorrecto - Asiento/Ficha: {asiento_ficha}")

        self.ruc = ruc
        self.provincia = provincia
        self.letra = letra
        self.folio_imagen = folio_imagen
        self.asiento_ficha = asiento_ficha

    def _calculate_dv(self):
        if self.letra in (LetraRucNatural.AV, LetraRucNatural.PI):
            if 0 < len(self.folio_imagen) < 4:
                ructb = ("5" + self.provincia.codigo.zfill(2) + self.letra.codigo + self.folio_imagen.zfill(3) +
                         self.asiento_ficha[:5].zfill(5)).zfill(20)
            else:
                ructb = ("5" + self.letra.codigo_validacion + self.folio_imagen.zfill(4) +
                         self.asiento_ficha[:5].zfill(5)).zfill(20)
        elif self.letra in (
                LetraRucNatural.EXTRANJERO, LetraRucNatural.PANAMENO_EXTRANJERO, LetraRucNatural.NATURALIZADO):
            if 0 < len(self.folio_imagen) < 4:
                if len(self.asiento_ficha) == 6 and self.letra in (
                        LetraRucNatural.EXTRANJERO, LetraRucNatural.NATURALIZADO):
                    ructb = ("5" + "00" + self.letra.codigo.ljust(2, "0") +
                             self.folio_imagen.zfill(3) + self.asiento_ficha).zfill(20)
                else:
                    ructb = ("5" + "00" + self.letra.codigo.ljust(2, "0") +
                             self.folio_imagen.zfill(3) + self.asiento_ficha[:5].zfill(5)).zfill(20)
            else:
                if len(self.asiento_ficha) == 6 and self.letra in (
                        LetraRucNatural.EXTRANJERO, LetraRucNatural.NATURALIZADO):
                    ructb = ("5" + self.letra.codigo_validacion + self.letra.codigo.ljust(2, "0") +
                             self.folio_imagen.zfill(4) + self.asiento_ficha).zfill(20)
                else:

                    ructb = ("5" + self.letra.codigo_validacion + self.letra.codigo +
                             self.folio_imagen.zfill(4) + self.asiento_ficha[:5].zfill(5)).zfill(20)
        elif self.letra == LetraRucNatural.SIN_LETRA:
            ructb = ("5" + self.provincia.codigo.zfill(2) +
                     "00" + self.folio_imagen.zfill(3) +
                     self.asiento_ficha[:5].zfill(5)).zfill(20)
        else:
            raise ValueError("Formato de RUC Natural incorrecto.")

        dv1 = calculate_dv_digit.calculate(old_ruc=False, ructb=ructb)
        dv2 = calculate_dv_digit.calculate(old_ruc=False, ructb=ructb + dv1)

        self._ructb = ructb
        self._dv1 = dv1
        self._dv2 = dv2
        self.dv = dv1 + dv2
