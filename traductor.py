import deepl
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
import shutil

deepl_auth_key = 'API_KEY' #AQUI VA LA API DE DEEPL PRO

traductor = deepl.Translator(deepl_auth_key)

#IDIOMA DE ENTRADA DEL TEXTO
idioma_origen = 'EN'

#CANTIDAD DE IDIOMAS A LOS QUE LO QUIERES TRADUCIR
contador = (int)(input("¿Cuantos idiomas quieres? "))


while contador != 0:
    #ESCRIBIR CADA IDIOMA EN UNA LINEA NUEVA SIN ESPACIOS
    idioma = input("Escribe una extension de idioma: ")
    archivo_xml = "./xml/" + "strings-" + idioma + ".xml"
    #archivo_txt = "./txt/" + "strings-" + idioma + ".txt"
    
    #CREA EL ARCHIVO XML CON LA EXTENSION DEL IDIOMA SELECCIONADO
    shutil.copy("strings.xml", archivo_xml)
    
    #NOMBRE DEL ARCHIVO QUE QUIERES COPIAR
    with open('strings.xml') as f:
        tree = ElementTree.parse(f)
    
    texto_traducido = []
    
    for node in tree.iter('string'):
        name = node.attrib.get('name')
        texto_a_traducir = node.text
        traducido = traductor.translate_text(texto_a_traducir, source_lang=idioma_origen, target_lang=idioma)
        texto_traducido.append(traducido)
    
    cont_indice = 0
    
    arbol = ET.parse(archivo_xml)
    root = arbol.getroot()
        
    for cadena in root.iter('string'):
        cadena.text = (str)(texto_traducido[cont_indice])
        print((str)(texto_traducido[cont_indice]))
        cont_indice = cont_indice + 1
                    
    arbol.write(archivo_xml,encoding="UTF-8",xml_declaration=True)
            
    #SI QUIERES CREAR UN TXT CON LAS TRADUCCIONES DESCOMENTA ESTO
    '''with open(archivo_txt, 'w') as j:
        for item in texto_traducido:
            j.write((str)(item))
            j.write('\n')'''
        
    contador = contador - 1



'''
Source languages available:
BG: Bulgarian
CS: Czech
DA: Danish
DE: German
EL: Greek
EN: English
ES: Spanish
ET: Estonian
FI: Finnish
FR: French
HU: Hungarian
IT: Italian
JA: Japanese
LT: Lithuanian
LV: Latvian
NL: Dutch
PL: Polish
PT: Portuguese
RO: Romanian
RU: Russian
SK: Slovak
SL: Slovenian
SV: Swedish
ZH: Chinese
Target languages available:
BG: Bulgarian
CS: Czech
DA: Danish
DE: German (supports formality)
EL: Greek
EN-GB: English (British)
EN-US: English (American)
ES: Spanish (supports formality)
ET: Estonian
FI: Finnish
FR: French (supports formality)
HU: Hungarian
IT: Italian (supports formality)
JA: Japanese
LT: Lithuanian
LV: Latvian
NL: Dutch (supports formality)
PL: Polish (supports formality)
PT-BR: Portuguese (Brazilian) (supports formality)
PT-PT: Portuguese (European) (supports formality)
RO: Romanian
RU: Russian (supports formality)
SK: Slovak
SL: Slovenian
SV: Swedish
ZH: Chinese
'''