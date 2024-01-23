from ruc_natural import RucNatural

try:
    ruc = RucNatural("PE-712-5789")

    print(f"RUC:           {ruc.ruc}")
    print(f"DV:            {ruc.dv}")
    print(f"Provincia:     {ruc.provincia.nombre}")
    print(f"Letra:         {ruc.letra.letra}")
    print(f"Letra Desc:    {ruc.letra.nombre}")
    print(f"Folio/Imagen:  {ruc.folio_imagen}")
    print(f"Asiento/Ficha: {ruc.asiento_ficha}")
except ValueError as e:
    print(str(e))
