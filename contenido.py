import os 
from datetime import *
import pyttsx3

def LimpiarPantalla():
    os.system('cls')

def audio(question):
    prueba = pyttsx3.init()
    prueba.setProperty('rate', 130)
    prueba.setProperty('voice', 'es-es')

    prueba.say(question)
    prueba.runAndWait()

    return question

def answer(respuesta):
    print(respuesta)
    input(audio(">>>PRESIONA ENTER PARA CONTINUAR: "))


#Carreras del ITLA 

carreras = ["Que carreras imparten el ITLA?", "Que carreras dan el ITLA?", "Carreras del ITLA"]

def tecnologos():
    return """

                                            >>>> Carreras del ITLA <<<<

    1. Simulacion interactiva y videojuegos     6. Redes de Informacion                         11. Multimedia
    2. Telecomunicacion                         7. Mecatronica                                  12. Sonido
    3. Inteligencia Artificial                  8. Manufactura automatica                       13. Desarrollo de Software
    4. Informatica forense                      9. Manufactura de dispositivos medicos          14. Analitica y ciencia de los Datos
    5. Energia renovables                       10. Diseño industrial                           15. Seguridad Informatica
    """

#Detalle carrera especifica

def especific():
    print(tecnologos())

    tecno = input(audio(">>>Selecciona la carrera para ver su información: "))

    if tecno == "1":
        return """Simulacion interactiva y videojuegos: Se obtendrá todo lo necesario para llevar los proyectos desde
         el borrador inicial hasta su concreción final, listos para ser distribuidos."""
   
    elif tecno == "2":
        return """Telecomunicacion: esta carrera está orientada a la resolución de problemas contemporáneos, adaptándose 
        a escenarios cambiantes, con alto sentido innovador y apegándose a los principios éticos y legales de la profesión."""
    
    elif tecno == "3":
        return """Inteligencia Artificial: tendrás la capacidad de modelar, diseñar y desarrollar sistemas de comportamiento inteligente,
         a fin de resolver problemas reales y retos que se puedan presentar en tus ámbitos laborales y de desarrollo profesional, guiados por la curiosidad, la pasión, la integridad, el trabajo en equipo y el mejoramiento continuo."""
    
    elif tecno == "4":
        return """Informatica forense: Planificar, gestionar y ejecutar investigaciones forenses que permitan identificar, preservar y presentar datos electrónicos válidos dentro de un proceso legal, ejerciendo su profesión con una 
        fuerte orientación a la resolución de problemas complejos; adaptándose a los constantes cambios, con actitud emprendedora y ética. """
   
    elif tecno == "5":
        return """Energia renovables: obtendrás conocimiento sobre la instalación, operación y mantenimiento de proyectos de pequeña y mediana escala de Energías Renovables para las actividades productivas de los distintos sectores 
        industriales"""
   
    elif tecno == "6":
        return """Redes de Informacion: Diseñar, implementar y gestionar arquitecturas de redes empresariales, desarrollando su práctica profesional con una fuerte orientación a la resolución de problemas contemporáneos, adaptándose a 
        escenarios cambiantes, con alto sentido innovador y apegándose a los principios éticos y legales de la profesión."""
    
    elif tecno == "7":
        return """Mecatronica: dominarás la automatización de procesos de manufactura, integrando componentes mecánicos, eléctricos, electrónicos y de software aplicado al control. """
   
    elif tecno == "8":
        return """Manufactura automatica: serás capaz de manejar equipos y maquinarias de Control Numérico Computarizado (CNC), realizar operaciones de Manufactura Integrada por Computador (CIM), operar y manejar con destreza máquinas 
        herramientas programables, diseñar y fabricar moldes de inyección plástica y aplicar todos los métodos automatizados de manufactura. """
    
    elif tecno == "9":
        return """Manufactura de dispositivos medicos: podrás desempeñar una serie de posiciones de índole industrial y/o manufactura, dentro de un ambiente de trabajo de manufactura de dispositivos médicos """
    
    elif tecno == "10":
        return """Diseño industrial: obtendrás destrezas en operaciones de construcción de maquetas, así como el manejo de materiales."""
   
    elif tecno == "11":
        return """Multimedia: serás capaz de brindar soluciones de comunicación audiovisual de forma creativa y eficaz que den respuesta a las necesidades del sector empresarial, educativo e industria en general"""
   
    elif tecno == "12":
        return """Sonido: contarás con las competencias necesarias para diseñar, desarrollar y supervisar la ejecución de proyectos de sonido por medio de técnicas y softwares de audio digital aplicables para audiovisuales, 
        la radio, industria discográfica y del entretenimiento, desde espectáculos musicales hasta eventos corporativos, con sentido ético y responsable. """
    
    elif tecno == "13":
        return """Desarrollo de Software: conocerás todas las etapas que intervienen en el proceso de desarrollo de software, enfocándose en la práctica de las tareas más técnicas."""
    
    elif tecno == "14":
        return """Analitica y ciencia de los Datos: contarás con competencias para manejar de las técnicas y herramientas aplicables a la analítica de datos con el objetivo de proponer soluciones basadas en evidencias y ser aplicadas en 
        el mercado local e internacional. """
    
    elif tecno == "15":
        return """Seguridad Informatica: Planificar, diseñar, implementar y administrar arquitecturas de ciberseguridad de acuerdo con las necesidades globales actuales, desempeñando sus funciones con un enfoque sólido de resolución de 
        problemas complejos; siendo versátil, con actitud innovadora, ética, y de liderazgo."""
    
    else:
        return "HAY UN ERROR"


#Rector

rector = ["Cual es el rector del ITLA?", "Quien es el rector del ITLA?", "Como se llama el rector del ITLA?"]

def rec():
    return "El rector del ITLA es el Ing. Omar Méndez Lluberes."

#Quien es Amadis

profe = ["Quien es Amadis?", "Quien es el profesor Amadis?", "Amadis que imparte?"]

def Amadis():
    return "Amadis Suarez Genao es un profesor del ITLA que imparte Fundamentos de Programacion."

#Autor del programa (you)

mimi = ["Quien creo este programa?", "Cual es el autor de esto?", "Quien creo esto?", "Autor", "A quien le pertenece este programa?"]

def Thammy():
    return "La creadora de este programa es Thammy F. Vargas A. (2021-1809)"

#Dia que es

dias = ["Que dia es hoy?", "Que dia de la semana es hoy?", "A que estamos hoy?", "Que dia estamos hoy?"]

def dia_actual():
    dia = datetime.now().weekday()

    if dia == 0:
        return " Hoy es lunes"
    elif dia == 1:
        return " Hoy es martes"
    elif dia == 2:
        return " Hoy es miercoles"
    elif dia == 3:
        return " Hoy es jueves"
    elif dia == 4:
        return " Hoy es viernes"
    elif dia == 5:
        return " Hoy es sabado"
    elif dia == 6:
        return " Hoy es domingo"
    else:
        return " HAY UN ERROR"

#Hora que es

hora = ["Que hora es?", "Cual es la hora?", "Que hora son?"]

def hora_actual():
    hora = datetime.now().hour
    minutos = datetime.now().minute
    return str(hora)+ ":" +str(minutos)

#Donde esta el ITLA

localidad = ["Donde esta ubicado el ITLA?", "Donde esta el ITLA?"]

def direccion_itla():
    return " El ITLA esta ubicado en la Autopista Las Américas, Km. 27, PCSD, La Caleta, Boca Chica."

#Como se llega al ITLA

how = ["Como se llega al ITLA?", "como se llega al ITLA desde el norte?", "como se llega al ITLA desde el sur?", "Como se llega al ITLA desde el este?", "Como se llega al ITLA desde santo domingo?", "Como se llega al ITLA?"]

def sitio():
    return("""

                                 REGIONES DEL PAIS

        1. Norte o Cibao                2. Suroeste         3.Sureste
    
    """)

def como_llegar():
    print(sitio())

    selec = input(audio(">>>Selecciona desde que region quieres llegar a ITLA: "))

    if selec == "1":
        return "Para llegar desde El Norte o Cibao se debe tomar un bus con rumbo a Santo Domingo, ya allí tomar uno rumbo a Boca Chica"
    elif selec == "2":
        return "Para llegar desde el Suroeste se debe tomar un bus con rumbo a la Duarte o Santo Domingo Este, ya allí tomar uno rumbo a Boca Chica"
    elif selec == "3":
        return "Para llegar desde el Sureste se debe tomar un bus con rumbo a Santo Domingo Este."
    else:
        return "HAY UN ERROR"

#Nota final de fundamentos

nota = ["Cual es la nota del autor?", "Cual es la nota del creador?", "Cual es la nota final?", "Nota final", "Aproximado de la nota final del autor"]

def notes():
    return "En la materia de Fundamentos de Programación el autor podría tener un 1OO al final si completa de manera correcta todas las asignaciones."