from ruc_natural_nt import RucNaturalNT

try:
    ruc = RucNaturalNT("8-NT-1-24")

    print(f"RUC:           {ruc.ruc}")
    print(f"DV:            {ruc.dv}")
    print(f"Provincia:     {ruc.provincia.nombre}")
    print(f"Folio/Imagen:  {ruc.folio_imagen}")
    print(f"Asiento/Ficha: {ruc.asiento_ficha}")
except ValueError as e:
    print(str(e))
