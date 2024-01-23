from enum import Enum


class Provincia(Enum):
    EN_BLANCO = ("", "En Blanco")
    NO_ASIGNADA = ("00", "No Asignada")
    BOCAS_DEL_TORO = ("01", "Bocas Del Toro")
    COCLE = ("02", "Cocle")
    COLON = ("03", "Colon")
    CHIRIQUI = ("04", "Chiriqui")
    DARIEN = ("05", "Darien")
    HERRERA = ("06", "Herrera")
    LOS_SANTOS = ("07", "Los Santos")
    PANAMA = ("08", "Panama")
    VERAGUAS = ("09", "Veraguas")
    GUNA_YALA = ("10", "Guna Yala, Madugandí y Wargandí")
    EMBER_WOUNAAN = ("11", "Embera Wounaan")
    NGABE_BUGLE = ("12", "Ngabe Bugle")
    PANAMA_OESTE = ("13", "Panama Oeste")

    def __init__(self, code, description):
        self.codigo = code
        self.nombre = description

    @classmethod
    def from_code(cls, code):
        for member in cls:
            if member.codigo == code.zfill(2):
                return member
        raise ValueError(f"Codigo de provincia invalido: {code}")
