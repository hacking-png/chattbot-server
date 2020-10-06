#QUE ESTAS VIENDO MI CODIGO?
#Librerias
import pandas as pan
import wikipedia
import datetime
import smtplib
import getpass
import random
from textblob import TextBlob
def monitor():
        #Si esta guardado
        try:
            
            sistema = pan.read_csv('cerebro.csv')
            
            sistema.set_index('user',inplace=True)
            print("server: "+sistema.loc[user,'bot'])
         #Si no esta guardado
        except KeyError:
            archivo = 'cerebro.csv'
            csv = open(archivo,"a")
            a = user
            #Hora actual        
            if " hora" in a:
                fecha = datetime.datetime.now()
                print("server: ",fecha.strftime('%I %p'),"con",fecha.strftime('%M')," minutos")
           #Guardar un secreto
            elif 'guardame un secreto' in a:
            	print("server: Los secretos estan para guardarse\nTe escucho")
            	secret = input("server: ..... ")
            	guardar = input("Quieres que te guarde ese secreto?Y/N: ")
            	
            	if guardar == "y":
            		csv.write("\n"+"secreto"+","+secret)
            		print('Tu secreto esta a salvo conmigo')
            		clave = ("Quieres que pongamos una clave?Y/N: ")
            		if clave == "y":
            		  	passw = input("Clave: ")
            	  		csv.write("\n"+"passworsecret"+passw)
            		  	print("Tu clave a sido guardada con exito")
            #Si hay un secreto
            elif 'dato curioso' in a:
            	curioso = ["server: Sabias que el sabado 19 de Septiembre alas 15:20 en Nueva York inicio la cuenta regresiva de que será el fin del mundo segun el relog nos quedaria 7 años y bajando","server: en cuarentena se han escuchado trompetas y sonidos en el cielo mucha gente pensaba que era las trompetas del fin del mundo,Lo que enrealidad es,es un terremotos en el cielo llamado cielomoto que produce sonidos tal cual una trompeta u otros sonidos","server: Sabias que en las fuerzas armadas de Estados Unidos implementaron perros robots llamados ABMS"]
            	ets = random.randrange(len(curioso))
            	print("server: ",curioso[ets])
            elif ' creador' in a:
            	print("Mi creador es Jostin..Jostin Orbe")
            elif ' secreto' in a:
            	try:
            	     clav = getpass("clave: ")
            	     paft = sistema.loc['passworsecret','bot']
            	     if clav == paft:
            	        	 secrett = sistema.loc['secreto','bot']
            	        	 print(secrett)
            	             
            	except KeyError:
            	  print("No tienes ningun secreto")
               #Dividir
            
            elif ' dividir' in a:
            	print("server: Dime los numeros")
            	numero1 = int(input('numero: '))
            	print("          ",numero1,"÷")
            	numero2 = int(input('numero: '))
            	print("          ",numero1,"÷",numero2)
            	result = numero1 / numero2
            	print("        = ",result)
            #Multiplicacion
            elif "preguntame algo" in a:
            	print("ok te preguntare")
            	preguntas = ["cual es tu nombre","Cual es tu color favorito","Cual es tu cantante favorito"]
            	indice = random.randrange(len(preguntas))
            	print("server: ",preguntas[indice])
            	if indice == 0:
                 	name = input("---->  ")
                 	csv.write("\n"+'nombre'+","+name)
                 	print("server: ",name)
            	if indice == 1:
                  	color = input("---->  ")
                  	csv.write('\n'+'color'+','+color)
                  	print("server: Que bonito color")	 	
            	if indice == 2:
                       cantante = input("---->  ")
                       csv.write('\n'+'cantante'+','+cantante)
                       print("server: Canta bien")
            elif 'nombre' in a:
                  nam = sistema.loc['nombre','bot']
                  print("server: ",nam)
            elif 'color favorito' in a:
                     fav = sistema.loc['color','bot']
                     print("server: ",fav)
            elif 'cantante favorito' in a:
            		       can = sistema.loc['cantante','bot']
            		       print("server: ",can)
            		       
            elif 'adivinanza' in a:
            	adivinanza = ["server: No muerde ni ladra,pero tiene dientes y la casa guarda¿Que es?","server: No es mas grande que una nuez,sube al monte y no tiene pies¿Que es?","server: Es tan largo como un camino,y gruñe como un cochino","server: Veinte patos caminaban,todos al mismo compas,y los veinte caminaban con una pata no más","server: Puedes aserlo, pero nunca verlo"]
            	rane = random.randrange(len(adivinanza))
            	print("server: ",adivinanza[rane])
            	if rane == 0:
                    	llave = input("---->  ")
                    	if 'llave' in llave:
                          	print("server: Sii es una llave")
                    	else:
                          	print("Ufff nop")
            	if rane == 1:
            		 caracol = input("---->  ")
            		 if 'caracol' in caracol:
            		 	print("server: Sii es un caracol")
            		 else:
            		 	print("server: Ufff nop")
            	if rane == 2:
            		 rio = input("---->")
            		 if "rio" in rio:
            		 	print("server: Sii es un rio")
            		 else:
            		 	print("nop")
            	if rane == 3:
            		 patos = input("---->  ")
            		 if '20 patos' in patos:
            		 	print("server: jajaj si 20 patos")
            		 else:
            		 	print("server: mm no")
            	if rane == 4:
            			ruido = input("---->  ")
            			if 'ruido' in ruido:
            				print('server: Exacto!!')
            			else:
            				print("nada que ver con tu respuesta")
            			
            #Multiplicacion
            elif 'chiste' in a:
            	chistes = ['server: Que le dice un espagueti a otro\nserver: mi cuerpo pide salsa','Sabes por que no se puede discutir con un dj?\nserver: Por que siempre esta cambiando de tema','server: Doctor, soy asmásmatico,¿Es grave?\nserver: No es esdrujula','server: De que se quejan siempre los astronautas\nserver: De falata de Espacio']
            	ran = random.randrange(len(chistes))
            	print("server: ",chistes[ran])
            elif ' multiplica' in a:
            	print("server: Dime los numeros")
            	numero1 = int(input('numero: '))
            	print("          ",numero1,"×")
            	numero2 = int(input('numero: '))
            	print("          ",numero1,"×",numero2)
            	result= numero1 * numero2
            	print("       = ",result)
                
            #Resta
            elif ' restar' in a:
            	print("server: Dime los numeros")
            	numero1 = int(input("numero: "))
            	print("          ",numero1,"-")
            	numero2 = int(input("numero: "))
            	print("          ",numero1,"-",numero2)
            	result = numero1 - numero2
            	print("        = ",result)
           
            #Sumar
            elif ' sumar' in a:
            	print("server: Dime los numero")
            	numero1 = int(input("numero: "))
            	print("          ",numero1,"+")
            	numero2 = int(input("numero: "))
            	print("          ",numero1,"+",numero2)
            	result = numero1 + numero2
            	print("          = ",result)
            #Mes actual
            elif ' mes' in a:
                fecha= datetime.datetime.now()
                ing = fecha.strftime('%B')
                ingles = TextBlob(ing)
                print("server: ",ingles.translate(to='es'))	             #Año actual
            elif ' año' in a:
                    fecha= datetime.datetime.now()
                    print("server: ",fecha.strftime('%Y'))
            #Wikipedia
            elif 'buscame en wikipedia' in a:
                wiki = input('server: Que palabra deseas buscar en wikipedia: ')
                wikii = wikipedia.summary(wiki)
                inglis = TextBlob(wikii)
                print("server: ",inglis.translate(to='es'))
            #Envia Un correo
            elif 'envia un correo' in a:
                    #Si esta registrado 
                    try:
                        print("server: Escribe el correo del destinatario: ")
                        destinatario = input("correo: ")
                        subject= input("Asunto: ")
                        message= input("mensaje: ")
                        message= 'Subject: {}\n\n{}'.format(subject,message)
                        servidor = smtplib.SMTP('smtp.gmail.com',587)
                        servidor.starttls()
                        correo1 = sistema.loc['correo','bot']
                        contraseña2 = sistema.loc['contraseña','bot']
                        servidor.login(correo1,contraseña2)
                        servidor.sendmail(correo1,destinatario,message)
                        servidor.quit()
                        print("server: Tu mensaje a sido enviado con exito")
                     #Si No Esta Registrado
                    except KeyError:
                        print("server: Ups no tienes registrado tu cuenta de gmail")
                        register = input("server: Quieres registrarte?Y/N: ")
                        if register == "y":
                            print("server: Esto se ara solo una vez...Asi que escribe bien tu correo y contraseña")
                            correo = input("server: Escribe tu correo: ")
                            contraseña= input("server: Escribe tu contraseña: ")
                            csv.write("\n"+'contraseña'+","+str(contraseña))
                            csv.write("\n"+'correo'+","+str(correo))
             #Traducir al Español
            elif 'traduceme al español' in a:
                palabra = input("server: Ingles: ")      
                ex = TextBlob(palabra)      
                print("server: Español: ",ex.translate(to='es'))
             #Traducir al Ingles
            elif 'traduceme al ingles' in a:
                palabra2= input("server: Español: ")
                exx = TextBlob(palabra2)
                print("server: Ingles: ",exx.translate(to='en'))		 
            #Si ninguna es compatible 
            else:
                b=input("---->  ")
                csv.write("\n"+a+","+b)
                csv.close()
            #Desarrollando
while True:
          user = input("---->  ")
          monitor()