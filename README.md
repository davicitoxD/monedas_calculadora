# monedas_calculadora
app simple escrita en python que convierte pesos ARS y UYU en dolares con la cotización Real consumida por  API

@startuml
title Conversión de Moneda

actor Usuario as user
participant "Script" as script
participant "API Externa" as api

user -> script: Ejecuta el script\ncon monto y moneda
activate script

script -> api: Solicita cotización USD
activate api
api --> script: Devuelve cotización USD
deactivate api

script -> script: Convierte monto a USD\nsegún cotización obtenida
script --> user: Muestra cotización USD y equivalente
deactivate script
@enduml
