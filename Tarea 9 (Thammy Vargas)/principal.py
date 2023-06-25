import os 
from contenido import *

menu = True

#Nombre del usuario
nombre = input(audio(">>>Bienvenido a nuestro programa, inserta tu nombre: ")) 

while menu: 
    os.system('cls')
    print("""
     ______               _                            _             ______       _   
    |  ___|             | |                          | |            | ___ \     | |  
    | |_ _   _ _ __   __| | __ _ _ __ ___   ___ _ __ | |_ ___ ______| |_/ / ___ | |_ 
    |  _| | | | '_ \ / _` |/ _` | '_ ` _ \ / _ \ '_ \| __/ _ \______| ___ \/ _ \| __|
    | | | |_| | | | | (_| | (_| | | | | | |  __/ | | | || (_) |     | |_/ / (_) | |_ 
    \_|  \__,_|_| |_|\__,_|\__,_|_| |_| |_|\___|_| |_|\__\___/      \____/ \___/ \__|

         ¡Bienvenido al bot del Instituto Tecnologico de las Americas (ITLA)!

    """)

    question = input(audio("━Hola "+nombre+" ¿Qué deseas preguntar? [DE LO CONTRARIO, ESCRIBA 'salir'] >>> "))

    if question in dias:
         answer(audio(nombre + dia_actual()))
    elif question in carreras:
         answer(audio(especific()))
    elif question in rector:
         answer(audio(nombre +", " + rec()))
    elif question in profe:
         answer(audio(nombre +", "+Amadis()))
    elif question in mimi:
         answer(audio(nombre+", "+Thammy()))
    elif question in hora:
         answer(audio(nombre+" Son las "+hora_actual()))
    elif question in localidad:
         answer(audio(direccion_itla()))
    elif question in how:
         answer(audio(como_llegar()))
    elif question in nota:
         answer(audio(nombre+", "+notes()))
    elif question == "salir":
         programa = False
         answer(audio(">>>GRACIAS POR UTILIZAR NUESTROS SERVICIOS"))
         break
    else:
        answer(audio("ERROR EN SU PREGUNTA, vuelva a intentarlo."))