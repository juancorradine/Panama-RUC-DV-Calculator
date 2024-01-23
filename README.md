# Panama RUC DV Calculator

Documentación en español [aquí](./README_ES.md).

For questions and issues, please open an issue on the GitHub repository
at https://github.com/juancorradine/panama-ruc-dv-calculator.

### Description

Checksum (DV) calculator for RUCs (Unique Taxpayer Registry) in Panama.

You need to know the type of RUC in order to initialize the correct class since it's not always possible to determine
the type just by having the RUC number. The algorithm to calculate the DV varies depending on the RUC type.

If the RUC does not have the correct format, a __ValueError__ exception is raised.

### Supported RUC Types:

* Persona Natural
* Persona Natural Extranjera (E)
* Persona Natural Naturalizada (N)
* Persona Natural Panameño Extranjero (PE)
* Persona Natural Antes de Vigencia (AV)
* Persona Natural Panameño Indigena (PI)
* Persona Natural NT
* Persona Juridica
* Persona Juridica Antigua
* Persona Juridica NT

#### Python classes:

* RucNatural (Supports E, N, PE, AV y PI)
* RUCNaturalNT
* RUCJuridica (Supports RUC Juridica Antiguo)
* RUCJuridicaNT

### Installation:

`pip install panama-ruc-dv-calculator`

### Usage examples:

More xamples in the __examples__ directory.

#### #1 - Persona Natural

```
from ruc_natural import RucNatural

try:
    ruc = RucNatural("1-184-921")

    print(f"RUC:           {ruc.ruc}")
    print(f"DV:            {ruc.dv}")
    print(f"Provincia:     {ruc.provincia.nombre}")
    print(f"Letra:         {ruc.letra.letra}")
    print(f"Letra Desc:    {ruc.letra.nombre}")
    print(f"Folio/Imagen:  {ruc.folio_imagen}")
    print(f"Asiento/Ficha: {ruc.asiento_ficha}")
    
except ValueError as e:
    print(str(e))
```

Results:

```
RUC:           1-184-921
DV:            49
Provincia:     Bocas Del Toro
Letra:         
Letra Desc:    Sin Letra
Folio/Imagen:  184
Asiento/Ficha: 921
```

#### #2 - Persona Juridica

```
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
```

Results:

```
RUC:             2588017-1-831938
DV:              20
Rollo/Tomo:      2588017
Folio/Imagen:    1
Asiento/Ficha:   831938
Es RUC Antiguo?: False
```

### DV Calculation Testing and Validation:

DV calculation tests in the tests directory.

To validate other generated DVs, you can use the DGI page > [ETax 2.0](https://etax2.mef.gob.pa/etax2web) > Digit
Verifier.

### Documentación DGI

The file __[Calculo Digito Verificador RUC](./dgi/Calculo_Digito_Verificador_RUC.pdf)__ issued by the DGI, located in
the dgi folder, explains the algorithm for generating the DV.

### Pending tasks

* DV generation for properties.
* On the [página](https://etax2.mef.gob.pa/etax2web) of the DGI for DV validation, there are the letters SB and EE.
  There is no documentation on what these letters mean or the algorithm to calculate their DV.

### Disclaimer

I do not work for the DGI. This code may contain errors. It is your responsibility to perform the relevant tests.

