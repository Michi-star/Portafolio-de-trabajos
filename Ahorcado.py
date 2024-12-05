import random
import os

Animacion = [
    ''' 
     /\\_____/\\ 

    ''', 

    '''  
     /\\_____/\\             
    /  /\\ /\\  \\      
    

    ''', 

    '''  
     /\\_____/\\             
    /  /\\ /\\  \\ 
   /    -0-    \\
    ''', 

    '''  
     /\\_____/\\             
    /  /\\ /\\  \\ 
   /    -0-    \\
   \\     U     /
    ''',
     '''  
     /\\_____/\\             
    /  /\\ /\\  \\ 
   /    -0-    \\
   \\     U     /
    \\         /

 ''' ,
    '''
     /\\_____/\\             
    /  /\\ /\\  \\ 
   /    -0-    \\
   \\     U     /
    \\         /
     \\_______/
     
     '''

    ]
    
        
Lenguajes=["PYTHON","DELFI","JAVA","JAVASCRIPT","RUBY","CSS","DARK"]


Aleatorio=random.choice(Lenguajes)
espacios=["_"]*len(Aleatorio)
#print(Aleatorio)*len(Aleatorio)


intentos=5


while True:
    os.system("cls")
    for caracter in espacios:
        print(caracter, end=" ")
    print()
    print(Animacion[intentos])
    letra=input("Ingresa una letra: ").upper()

    encontrar=True
    for indice,caracter in enumerate(Aleatorio):
        if caracter==letra:
            espacios[indice]=letra
            encontrar=False
    if encontrar:
        intentos-=1
        
    if "_" not in espacios:
        os.system("cls")
        print(Aleatorio)
        print("Ganaste!")
        
        break
    
    if intentos<0:
        print("Perdiste :(")
        break
            
"""var=0
while (var <= 5):
    os.system("cls")
    print(Animacion[var])
    #os.system("pause")
    var += 1"""


    


    