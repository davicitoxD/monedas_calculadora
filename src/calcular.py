import sys
import requests

def obtener_cotizacion():
    try:
        # Obtener la cotización del USD desde alguna página web
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        cotizacion_usd = {
            "ARS": data["rates"]["ARS"],
            "UYU": data["rates"]["UYU"]
        }
        return cotizacion_usd
    except Exception as e:
        print("Error al obtener la cotización del USD:", e)
        sys.exit(1)

def convertir_a_usd(monto, moneda, cotizacion_usd):
    def ars():
        equivalente_usd = monto / cotizacion_usd["ARS"]
        print(f"Monto ingresado en ARS: {monto} ARS")
        print(f"Cotización del USD: 1 USD = {cotizacion_usd['ARS']} ARS")
        print(f"Equivalente en USD: {equivalente_usd:.2f} USD")

    def uyu():
        equivalente_usd = monto / cotizacion_usd["UYU"]
        print(f"Monto ingresado en UYU: {monto} UYU")
        print(f"Cotización del USD: 1 USD = {cotizacion_usd['UYU']} UYU")
        print(f"Equivalente en USD: {equivalente_usd:.2f} USD")

    switch_case = {
        "ARS": ars,
        "UYU": uyu
    }

    try:
        switch_case[moneda.upper()]()
    except KeyError:
        print("Moneda no soportada. Por favor, ingrese ARS o UYU.")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Uso: python calculadora.py <monto> <moneda> , Monedas aceptadas <ARS> <UYU> ")
        print("<ARS> corresponde a pesos Argentinos y <UYU> coreesponde a pesos Uruguayos")
        sys.exit(1)
    
    monto = float(sys.argv[1])
    moneda = sys.argv[2]

    cotizacion_usd = obtener_cotizacion()
    convertir_a_usd(monto, moneda, cotizacion_usd)

if __name__ == "__main__":
    main()
