#!/usr/bin/python3
""" TP2 para ejercitar sincronizacion y sus problemas"""
import threading
import time
import random

lugares_bote = []
viajes = 0
gallinas = []
bosteros = []   
def hincha_river():
    """ Implementar funcion para subir al bote ....si es que se puede ..."""
    global viajes
    global lugares_bote
    global gallinas
    global bosteros
    while viajes < 20:
      mutex.acquire()
      if (len(lugares_bote) == 0) and ((len(bosteros)) < (len(gallinas))):
         lugares_bote.append("R")
         gallinas.pop(0)
         print("R subio al bote")  
         print("BOTE: ",lugares_bote) 
      elif (len(lugares_bote) == 1) and (1 < len(gallinas)):
         lugares_bote.append("R")
         gallinas.pop(0)
         print("R subio al bote")
         print("BOTE: ",lugares_bote)
      elif (len(lugares_bote) ==2) and (lugares_bote.count("R")==1) and (1 < len(gallinas)):
         lugares_bote.append("R")
         gallinas.pop(0)
         print("R subio al bote")
         print("BOTE: ",lugares_bote)  
      elif (len(lugares_bote) ==2) and (lugares_bote.count("R")==2) and (1 < len(gallinas)):
         lugares_bote.append("R")
         gallinas.pop(0)
         print("R subio al bote")
         print("BOTE: ",lugares_bote)     
      elif (len(lugares_bote) ==3) and ((lugares_bote.count("R")==1) or ((lugares_bote.count("R")==3) and (lugares_bote.count("B")==0))) and (1 < len(gallinas)):
         lugares_bote.append("R")
         gallinas.pop(0)
         a_remar("R")          
      mutex.release() 


def hincha_boca():
    """ Implementar funcion para subir al bote ....si es que se puede ..."""
    global viajes
    global lugares_bote
    global bosteros
    global gallinas
    while viajes < 20:
      mutex.acquire()     
      if (len(lugares_bote) == 0) and ((len(gallinas)) < (len(bosteros))):
         lugares_bote.append("B")
         bosteros.pop(0)
         print("B subio al bote")
         print("BOTE: ",lugares_bote)   
      elif (len(lugares_bote) == 1) and (1 < len(bosteros)): 
         lugares_bote.append("B")
         bosteros.pop(0)
         print("B subio al bote")
         print("BOTE: ",lugares_bote) 
      elif (len(lugares_bote) ==2) and (lugares_bote.count("B")==1) and (1 < len(bosteros)):
         lugares_bote.append("B")
         bosteros.pop(0)
         print("B subio al bote")
         print("BOTE: ",lugares_bote)  
      elif (len(lugares_bote) ==2) and (lugares_bote.count("B")==2) and (1 < len(bosteros)):
         lugares_bote.append("B")
         bosteros.pop(0)
         print("B subio al bote")
         print("BOTE: ",lugares_bote)         
      elif (len(lugares_bote) ==3) and ((lugares_bote.count("B")==1) or ((lugares_bote.count("B")==3) and (lugares_bote.count("R")==0))) and (1 < len(bosteros)):
         lugares_bote.append("B")
         bosteros.pop(0)
         a_remar("B")        
      mutex.release()

def barra_brava_river():
    """ Generacion de hinchas de River"""
    global viajes
    global lugares_bote
    while viajes < 20:
       gallinas.append("R")
       print("River: ",len(gallinas)) 
       time.sleep(random.randrange(0, 5))
       r = threading.Thread(target=hincha_river)
       r.start()    
   
def barra_brava_boca():
    """ Generacion de hinchas de Boca"""
    global viajes
    global lugares_bote
    while viajes < 20: 
       bosteros.append("B") 
       print("boca: ",len(bosteros))
       time.sleep(random.randrange(0, 5))         
       r = threading.Thread(target=hincha_boca)
       r.start()

def a_remar(h):
    global viajes
    global lugares_bote
    if h == "R":
       print("Soy el capitan R, hora de remar")
    elif h == "B":
       print("Soy el capitan B, hora de remar")
    viajes=viajes+1
    print("EL NUMERO DE VIAJES ES: ",viajes)
    print("BOTE que zarpo: ",lugares_bote)
    lugares_bote = [] 
          

mutex=threading.Lock()
t1 = threading.Thread(target=barra_brava_river)
t2 = threading.Thread(target=barra_brava_boca)
t1.start()
t2.start()
t1.join()
t2.join()
"""t1 = threading.Thread(target=barra_brava_river, arg= viajes)
t2 = threading.Thread()
"""
print("Listo")
"""print("terminaron los viajes ")"""
