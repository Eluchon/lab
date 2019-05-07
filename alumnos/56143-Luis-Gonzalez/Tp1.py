#!/usr/bin/python
import re
import sys
import os
import getopt
import multiprocessing
print sys.argv
print len(sys.argv)

try:
    if len (sys.argv) > 7:
        sys.exit()
    if sys.argv[1] == "-a":
        print "Sistema de ayuda"
        print "* Para informacion sobre la aplicacion agruegue la opcion -i"+ sys.argv[0] + " -a -i"
        print "* Para informacion sobre el formato agregue la opcion -j" + sys.argv[0] + " -a -j"
        print "* Para informacion sobre las funciones que se utilizaron agregue la opcion -k." + sys.argv[0] + " -a -k"
      
        opc ,argus = getopt.getopt(sys.argv[2:],'ijk:')

        for o in opc:

            if o[0] == "-i":
                print "El objetivo del programa es contar la cantidad de palabras que posee un archivo determinado. El tamanho de bloque es utilizado para contar las palabras con el uso de dos procesos hijos del principal."
                I = True 
            elif o[0] == "-j":
                print "El formato a usar es: " + sys.argv[0] + " -f <archivo> -n <tamanho_bloque>."
                J = True
            elif o[0] == "-k":
                print "Se utilizaron cuatro funciones. La primer funcion es partir(lista), la cual es la encargada de partir la lista que posee las palabras para asi generar dos listas y entregarsela a un proceso hijo distinta. La segunda funcion es countWords(lista), esta funcion es utilizada por los procesos hijos y sirve para contar las palabras dentro de su lista correspondiente. Las funciones hijo1 e hijo2 son los procesos hijos."
                K = True
        print I,J,K
    else:
        if sys.argv[1] != "-f":
            sys.exit()
        try:
            if os.path.isfile(sys.argv[2]) != True:
                sys.exit()
            else:
                archivo = sys.argv[2]
        except:
            print "ERROR"
            print "EL ARCHIVO NO EXISTE."
        if  sys.argv[3] != "-n":
            sys.exit()
        try:
            if  sys.argv[4].isdigit() != True or int (sys.argv[4]) == 0:    
                sys.exit()
            else:
                Tbloques = int (sys.argv[4])
        except:
            print "ERROR"
            print "EL TAMANHO DE BLOQUES COLOCADO NO ES UN NUMERO VALIDO."
         
        print "Archivo: ", archivo
        print "Tamanho de bloques: ", Tbloques

        def partir(lista):
            lista_a=[]
            lista_b=[]
            a=str(float(len(lista))/float(2))
            if a[len(str(a))-1]!='0':
	            for i in range(0,(len(lista)/2)+1,1):
		            lista_a.append(lista[i])
	            for i in range((len(lista)/2)+1,len(lista),1):
		            lista_b.append(lista[i])
            if a[len(str(a))-1]=='0':
	            for i in range(0,(len(lista)/2),1):
		            lista_a.append(lista[i])
	            for i in range((len(lista)/2),len(lista),1):
		            lista_b.append(lista[i])
            return lista_a, lista_b

        def countWords(lista):
            cont = 0
            for lines in lista:
                found = re.findall("([a-z\']+)", lines.strip(), re.I)
                if found:
                   cont += len(found)
            return cont
 
           
        def hijo1(textoa,q):
                  num=countWords(textoa)
                  q.put(num)
      
        def hijo2(textob,q):
                  num=countWords(textob)
                  q.put(num)

        f=open(archivo)
        sizefile = os.stat(archivo).st_size
        texto=[]
        vueltadar= ((sizefile/int(Tbloques))+1)
        vuelta=0
        while vuelta < vueltadar:
            dato=f.read(int(Tbloques))
            texto.append(dato)
            vuelta=vuelta+1

        q = multiprocessing.Queue()

        textoa,textob = partir(texto)

        h1 = multiprocessing.Process(target=hijo1,  args=(textoa,q))
        h2 = multiprocessing.Process(target=hijo2,  args=(textob,q))

        h1.start()
        h2.start()

        h2.join()
        h1.join()

        total=0
        while q.empty() is False:
             total=total+(q.get())
        print "El total de palabras es: ", total   
        sys.stdout.write("El total de palabras es: %s" % total)
  
except:
     print "El formato a usar es: " + sys.argv[0] + " -f <archivo> -n <tamanho_bloque>. Para mas ayuda use:" + sys.argv[0] + " -a"


