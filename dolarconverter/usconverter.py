import sys  # Importamos el módulo sys para acceder a variables y funciones relacionadas con el sistema.
import os   # Importamos el módulo os para acceder a funcionalidades dependientes del sistema operativo.
import requests  # Importamos el módulo requests para realizar solicitudes HTTP.

def obtener_cotizacion():
    # Intentamos obtener algún resultado de la API; en caso contrario, devolvemos un error.
    try:
        # Obtener la cotización del USD desde alguna página web usando la API de ExchangeRate-API.
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()  # Convertimos la respuesta en formato JSON a un diccionario.
        # Extraemos las cotizaciones del ARS y UYU con respecto al USD.
        cotizacion_usd = {
            "ARS": data["rates"]["ARS"],
            "UYU": data["rates"]["UYU"]
        }
        return cotizacion_usd  # Devolvemos las cotizaciones obtenidas.
    except Exception as e:
        print("Error al obtener la cotización del USD:", e)  # En caso de error, mostramos un mensaje.
        sys.exit(1)  # Salimos del programa con un código de error.

def convertir_a_usd(monto, moneda, cotizacion_usd):
    # Función interna para convertir de ARS a USD.
    def ars():
        # Calculamos el equivalente en USD del monto ingresado en ARS.
        equivalente_usd = monto / cotizacion_usd["ARS"]
        # Mostramos información sobre la conversión.
        print(f"Monto ingresado en ARS: {monto} ARS")
        print(f"Cotización del USD: 1 USD = {cotizacion_usd['ARS']} ARS")
        print(f"Equivalente en USD: {equivalente_usd:.2f} USD")

    # Función interna para convertir de UYU a USD.
    def uyu():
        # Calculamos el equivalente en USD del monto ingresado en UYU.
        equivalente_usd = monto / cotizacion_usd["UYU"]
        # Mostramos información sobre la conversión.
        print(f"Monto ingresado en UYU: {monto} UYU")
        print(f"Cotización del USD: 1 USD = {cotizacion_usd['UYU']} UYU")
        print(f"Equivalente en USD: {equivalente_usd:.2f} USD")

    # Diccionario que mapea cada moneda con su función correspondiente de conversión.
    switch_case = {
        "ARS": ars,
        "UYU": uyu
    }

    try:
        switch_case[moneda.upper()]()  # Ejecutamos la función correspondiente a la moneda ingresada.
    except KeyError:
        print("Moneda no soportada. Por favor, ingrese ARS o UYU.")  # Mensaje de error para monedas no soportadas.
        sys.exit(1)  # Salimos del programa con un código de error.

def main():
    # Verificamos si se están utilizando variables de entorno.
    if os.environ.get("SDE"):
        # Si se están utilizando variables de entorno, obtenemos el monto y la moneda de ellas.
        monto = float(os.environ["AMOUNT"])
        moneda = os.environ["CURRENCY"]
    else:
        # Si no se están utilizando variables de entorno, verificamos los argumentos de línea de comandos.
        if len(sys.argv) == 3:
            monto = float(sys.argv[1])  # Convertimos el primer argumento en un número de punto flotante.
            moneda = sys.argv[2]  # Obtenemos la segunda argumento.
        else:
            # Si no se proporcionan los argumentos adecuados, mostramos un mensaje de uso y salimos del programa.
            print("Uso: python calculadora.py <monto> <moneda>, Monedas aceptadas <ARS> <UYU>")
            print("<ARS> corresponde a pesos Argentinos y <UYU> corresponde a pesos Uruguayos")
            sys.exit(1)  # Salimos del programa con un código de error.

    cotizacion_usd = obtener_cotizacion()  # Obtenemos las cotizaciones del USD.
    convertir_a_usd(monto, moneda, cotizacion_usd)  # Realizamos la conversión.

if __name__ == "__main__":
    main()  # Llamamos a la función principal si el script se ejecuta directamente.
