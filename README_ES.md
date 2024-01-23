# Panama RUC DV Calculator

English documentation [here](./README.md).

Para preguntas y problemas, por favor abra un issue en el repositorio de GitHub
en https://github.com/juancorradine/panama-ruc-dv-calculator.

### Descripción

Calculadora de Dígito Verificador (DV) para RUCs (Registro Único de Contribuyente) de Panamá.

Se debe saber el tipo de RUC, para poder inicializar la clase correcta, ya que no siempre se puede determinar el tipo
solo teniendo el # de RUC. El algoritmo para calcular el DV varía por tipo de RUC.

Si el RUC no tiene el formato correcto, se genera una excepción de tipo __ValueError__.

### Tipos de RUCs soportados:

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

#### Clases Python:

* RucNatural (Soporta E, N, PE, AV y PI)
* RUCNaturalNT
* RUCJuridica (Soporta RUC Juridica Antiguo)
* RUCJuridicaNT

### Instalación:

`pip install panama-ruc-dv-calculator`

### Ejemplos de Uso:

Mas ejemplos en el directorio __examples__.

#### #1 - Persona Natural

```
from panama_ruc_dv_calculator.ruc_natural import RucNatural

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

Resultado:

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
from panama_ruc_dv_calculator.ruc_juridica import RucJuridica

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

Resultado:

```
RUC:             2588017-1-831938
DV:              20
Rollo/Tomo:      2588017
Folio/Imagen:    1
Asiento/Ficha:   831938
Es RUC Antiguo?: False
```

### Pruebas y validación de DV's Generados:

Pruebas de cálculo de DVs en el directorio tests.

Para validar otros DVs generados, se puede usar la página de la DGI > [ETax 2.0](https://etax2.mef.gob.pa/etax2web) >
Digito Verificador.

### Documentación DGI

El archivo __[Calculo Digito Verificador RUC](./dgi/Calculo_Digito_Verificador_RUC.pdf)__ emitido por la DGI que se
encuentra en la carpeta dgi, explica el
algoritmo para generar el DV.

### Pendientes

* Generación de DV para fincas.
* En la [página](https://etax2.mef.gob.pa/etax2web) de la DGI de validación de DV, aparecen las letras SB y EE. No hay
  documentación sobre estas letras que significan, ni el algorimo para calcular su DV.

### Descargo de Responsabilidad

No trabajo en la DGI. Este código puede tener errores. Es tu responsabilidad hacer las pruebas pertinentes.

