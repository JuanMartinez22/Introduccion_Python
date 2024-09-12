import json

with open("MOCK_DATA.json") as datos:
    personas = json.load(datos)
    for persona in personas:
        # print(persona)
        print(f"Nombre: {persona.get('Nombre')}")
        print(f"Apellio: {persona.get('Apellido')}")
        print(f"Correo: {persona.get('Email')}")
        print(f"Genero: {persona.get('Genero')}")
        print("------------------------------------------")