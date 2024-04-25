# Dolarconverter
- App simple escrita en python que convierte pesos ARS y UYU en dolares con la cotización Real consumida por  API.
- Los valores aceptados son dos parametros separados por espacio en primer lugar la cantidad de dinero a convertir y en segundo la moneda , que puede ser ARS o UYU.

## Diagrama de Secuencia
### Caso python interpreter
```
- $ virtaulenv env
- $ . env/bin/activate 
- $ python dolarconverter/usconverter.py 5000 ARS 

```
![image](https://github.com/davicitoxD/monedas_calculadora/assets/8561970/da5275f3-fcf6-4163-89e0-1ae5fe91adfd)
### Caso docker
```
- $ docker build  --no-cache -f dockerfile -t usconverter-sde . 
- $ docker run -e AMOUNT=1000 -e CURRENCY=UYU usconverter-sde

```
![image](https://github.com/davicitoxD/monedas_calculadora/assets/8561970/be36a49f-3a9f-4c1a-abdc-5ab5003e9d0f)
## Caso utilizar la app en modo libreria

```
- $ python -m build .
- $ pip install dist/dolarconverter-0.1.0-py3-none-any.whl

```


