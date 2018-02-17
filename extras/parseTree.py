import xml.etree.ElementTree as ET

def cataloga(archivo):
    tree = ET.parse(archivo)
    root = tree.getroot()

    for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get('name')
        print(name, rank)
#cataloga('prueba.html')