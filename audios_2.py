# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:08:02 2024

@author: HP
"""

import wave

def hide_message(audio_file, message):
    # Abrir el archivo de audio
    with wave.open(audio_file, "rb") as audio:
        # Leer los parámetros del archivo de audio
        params = audio.getparams()
        frames = audio.readframes(audio.getnframes())
    
    # Convertir el mensaje a binario
    message_bin = ''.join(format(ord(char), '08b') for char in message)
    
    # Asegurarse de que el mensaje no sea más largo que el audio
    if len(message_bin) > len(frames):
        raise ValueError("El mensaje es demasiado largo para ser ocultado en el audio.")
    
    # Ocultar el mensaje utilizando paridad
    modified_frames = bytearray(frames)
    for i in range(len(message_bin)):
        if message_bin[i] == '1':
            if modified_frames[i] % 2 == 0:
                modified_frames[i] += 1
        else:
            if modified_frames[i] % 2 == 1:
                modified_frames[i] -= 1
    
    # Guardar el archivo de audio modificado
    with wave.open("audio_oculto.wav", "wb") as audio_hidden:
        audio_hidden.setparams(params)
        audio_hidden.writeframes(modified_frames)

# Ejemplo 
audio_file = "OYE MI AMOR.wav"


mensaje = """El maestro de Kung fu Po ayuda a sus padres, el Sr. Ping y Li, a abrir su nuevo restaurante. El Maestro Shifu conversa con Po que debe avanzar para convertirse en el líder espiritual del Valle de la Paz, lo que significa que ya no será el Guerrero Dragón y debe encontrar un candidato adecuado para ocupar su lugar como el próximo Guerrero Dragón.

Mientras Po lucha por elegir candidatos, atrapa a una ladrona llamada Zhen tratando de robar armas antiguas y la envía a prisión, pero pronto se entera del repentino regreso de Tai Lung de Zhen. Gracias a una pista de Zhen, descubre que Tai Lung no ha regresado, pero alguien se ha hecho pasar por él. Ella le dice que la persona que cambió de forma a Tai Lung es La Camaleona y que si quiere detenerla, necesitará su ayuda. Reacio al principio pero con ganas de emprender una última aventura como Guerrero Dragón, Po se dirige a Juniper City con Zhen. Mientras tanto, el Sr. Ping y Li, aterrorizados por lo que podría pasarle a su hijo, los siguen.

En Juniper City, son arrestados, pero Po y Zhen escapan a la Guarida de los Ladrones, donde Zhen se reúne con Han, quien les permite quedarse en la Guarida pero quiere que se vayan al día siguiente. Pronto, Po y Zhen se dirigen a la guarida de la Camaleona para acabar con ella. Sin embargo, se revela que la Camaleona había acogido a Zhen cuando era niña como su aprendiz y está trabajando para ella, traicionando la confianza de Po. Se escapa, pero sin el Bastón de la Sabiduría. Cuando le pide a Zhen que se lo devuelva, se revela que es a la Camaleona disfrazada, quien lo envía por un precipicio. Con el bastón, la Camaleona crea una puerta espiritual para convocar a todos los maestros de artes marciales para que les roben su kung fu, incluidos Tai Lung, Lord Shen y Kai. Zhen, al ver el error que ha cometido, decide huir de la Camaleona para siempre.

Mientras tanto, Po habla con sus padres y les dice que teme el cambio. El Sr. Ping le dice que al principio tenía miedo del cambio, pero que no sería padre si las cosas no cambiaran, lo que anima a Po a detener a la Camaleona. Po se reúne con Zhen, quien intenta detenerlo, lo que lleva a un duelo entre ellos. Al darse cuenta de que no puede hacerle cambiar de opinión, se despide de él antes de que Po se enfrente a la Camaleona.

Zhen logra convencer a Den of Thieves para que la ayuden a salvar a Po. Mientras tanto, Tai Lung descubre que Po perdió el Bastón de la Sabiduría, lo que le hizo perder aún más fe en Po que originalmente. Po intenta enfrentarse a la Camaleona y recuperar su bastón. Antes de que la Camaleona pueda dar el golpe final, interviene Zhen. La Camaleona se transforma en un híbrido de múltiples criaturas y los tres luchan por toda la habitación. Zhen cae entre los escombros, mientras la Camaleona se transforma en Po, a quien se enfrenta el verdadero Po. Sin embargo, la Camaleona lo atrapa en una jaula.

Confiando en Zhen, le da el Bastón de la Sabiduría, que ella usa para devolver el kung fu a todos los maestros a los que la Camaleona le robó. Al no aceptar la derrota fácilmente, este último intenta matar a Po nuevamente, pero es rápidamente derrotada. Al darse cuenta de que estaba equivocado acerca de Po, Tai Lung le muestra su respeto y lo reconoce como el Guerrero Dragón. Po abre una puerta espiritual y envía a todos los maestros de regreso al Reino de los Espíritus, y Tai Lung se lleva a la Camaleona con él.

De vuelta en el Valle de la Paz, Zhen está lista para volver a prisión, pero Po decide elegirla como la próxima Guerrera Dragón. Confiando en su elección, Po y los Cinco Furiosos (Tigresa, Mono, Mantis, Víbora y Grulla) ayudan a entrenar a Zhen para que se convierta en el próximo Guerrero Dragón."""


hide_message(audio_file, mensaje)
print("Mensaje oculto correctamente en el audio.")

def find_hidden_message(audio_file):
    # Abrir el archivo de audio
    with wave.open(audio_file, "rb") as audio:
        frames = audio.readframes(audio.getnframes())
    
    # Encontrar el mensaje oculto en los bits menos significativos
    hidden_message = ""
    for frame in frames:
        if frame % 2 == 0:
            hidden_message += '0'
        else:
            hidden_message += '1'
    
    # Convertir el mensaje binario a texto
    message = ""
    for i in range(0, len(hidden_message), 8):
        byte = hidden_message[i:i+8]
        message += chr(int(byte, 2))
        if message[-1] == '\x00':
            break
    
    return message


# Ejemplo

audio_file = "audio_oculto.wav"
mensaje_oculto = find_hidden_message(audio_file)
print("Mensaje oculto encontrado:", mensaje_oculto)





