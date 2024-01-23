from panama_ruc_dv_calculator.ruc_juridica import RucJuridica

from ruc_juridica import RucJuridica

try:
    ruc = RucJuridica("2588017-1-831938")

    print(f"RUC:             {ruc.ruc}")
    print(f"DV:              {ruc.dv}")
    print(f"Rollo/Tomo:      {ruc.rollo_tomo}")
    print(f"Folio/Imagen:    {ruc.folio_imagen}")
    print(f"Asiento/Ficha:   {ruc.asiento_ficha}")
    print(f"Es RUC Antiguo?: {str(ruc.is_ruc_antiguo)}")
except ValueError as e:
    print(str(e))
