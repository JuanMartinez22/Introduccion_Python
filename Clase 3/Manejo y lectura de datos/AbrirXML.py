import xml.etree.ElementTree as ET

try:
    xml_file = open("dataset.xml")
    # print(xml_file.read())
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        lst_personas = xml_data.findall("record")
        for persona in lst_personas:
            print(f"Nombre: {persona.find('Nombre').text}")
            print(f"Apellido: {persona.find('Apellido').text}")
            print(f"Correo: {persona.find('Email').text}")
            print(f"Genero: {persona.find('Genero').text}")
            print("-------------------------------------")

except Exception as err:
    print("Error: ", err)
finally:
    xml_file.close()