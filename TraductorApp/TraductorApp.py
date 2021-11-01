import tkinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import deepl
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
import shutil

def traducir():
    if main_window.archivo != "" and idioma != "":
        print(main_window.archivo)
        
        deepl_auth_key = 'API_KEY' #AQUI VA LA API DE DEEPL PRO

        traductor = deepl.Translator(deepl_auth_key)

        #IDIOMA DE ENTRADA DEL TEXTO
        idioma_origen = 'EN'

        #CANTIDAD DE IDIOMAS A LOS QUE LO QUIERES TRADUCIR
        contador = 1 #(int)(input("¿Cuantos idiomas quieres? "))


        while contador != 0:
            #ESCRIBIR CADA IDIOMA EN UNA LINEA NUEVA SIN ESPACIOS
            #idioma = input("Escribe una extension de idioma: ")
            archivo_xml = "strings-" + idioma.get() + ".xml"
            #archivo_txt = "strings-" + idioma + ".txt"
            
            #CREA EL ARCHIVO XML CON LA EXTENSION DEL IDIOMA SELECCIONADO
            shutil.copy("strings.xml", archivo_xml)
            
            #NOMBRE DEL ARCHIVO QUE QUIERES COPIAR
            with open('strings.xml') as f:
                tree = ElementTree.parse(f)
            
            texto_traducido = []
            
            for node in tree.iter('string'):
                name = node.attrib.get('name')
                texto_a_traducir = node.text
                traducido = traductor.translate_text(texto_a_traducir, source_lang=idioma_origen, target_lang=idioma.get())
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

def buscarArchivo():
    main_window.archivo =  filedialog.askopenfilename(initialdir = "./",title = "Elige un Archivo XML",filetypes = (("archivos XML","*.xml"),("all files","*.*")))
        


main_window = tk.Tk()
main_window.title('Traducir XML')


b_archivo = Button(main_window, text='Insertar archivo', fg='#fff', bg='#005AB9', command=buscarArchivo)
b_archivo.grid(columnspan=2)

lista_opciones = ["BG","CS","DA","DE","EL","EN-GB","EN-US","ES","ET","FI","FR","HU","IT","JA","LT","LV","NL","PL","PR-BR","PT-PT","RO","RU","SK","SL","SV","ZH"]

idioma = tkinter.StringVar(main_window)
  
idioma.set("Selecciona un idioma")

menu_idioma = tkinter.OptionMenu(main_window, idioma, *lista_opciones)
menu_idioma.grid(columnspan=1)


b_traducir = Button(main_window, text='Traducir', fg='#fff', bg='#005AB9', command=traducir)
b_traducir.grid(row=1, column=2)



main_window.mainloop()
