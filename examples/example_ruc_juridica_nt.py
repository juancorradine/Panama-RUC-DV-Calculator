from panama_ruc_dv_calculator.ruc_juridica_nt import RucJuridicaNT

try:
    ruc = RucJuridicaNT("5-NT-478-2351")

    print(f"RUC:             {ruc.ruc}")
    print(f"DV:              {ruc.dv}")
    print(f"Provincia:       {ruc.provincia.nombre}")
    print(f"Folio/Imagen:    {ruc.folio_imagen}")
    print(f"Asiento/Ficha:   {ruc.asiento_ficha}")
except ValueError as e:
    print(str(e))
