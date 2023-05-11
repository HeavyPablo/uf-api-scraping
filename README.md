# Flask API UF SCRAPING

API en Flask para obtener el valor de la UF por medio de Query Params adoptando técnicas de scraping hacia la web del SII.

## Instalación

Instalar las dependencias:
```shell
$ pip install -r requirements.txt
```

## Arrancar proyeto

```shell
$ flask run
```

## Uso

Contiene un endpoint ``/uf`` el cuál traerá el valor de la UF del día.

``/uf`` :
````json
{
  "data": {
    "uf": "<valor de la UF del día>"
  },
  "code": 200
}
````

El cuál permite el Query Params ``date`` con formato ``Y%-m%-d%`` para retornar el valor de la UF según el día especificado.

``/uf?date=2022-05-32`` :

````json
{
  "data": {
    "uf": "<valor de la UF de la fecha>"
  },
  "code": 200
}
````

En caso de error del formato o error en el scraper, este devolverá una respuesta personalizada dependiendo del tipo.

Error de formato en ``date``:

````json
{
  "error": "Validation Error",
  "code": 422,
  "description": [
    "Mensaje específico del error",
    "..."
  ]
}
````

Error en scraper:
````json
{
  "error": "Scraper Error",
  "code": 400,
  "description": [
    "Mensaje específico del error",
    "...."
  ]
}
````

