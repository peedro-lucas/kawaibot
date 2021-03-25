import pyautogui as cursor
import time
cont = 0
#OBS: TODAS AS COORDENADAS PASSADAS SÃO DE ACORDO COM MINHA RESOLUÇÃO, QUE É 1440x900

#A variavel "quant" é o tempo que o programa ficara em cada vídeo
quant = int(input('Quanto tempo deseja esperar para passar os videos? (EM SEGUNDOS): '))




while True:
    time.sleep(3) # Tempo para iniciar o programa.
    print(cursor.position())
    cursor.click(x=2856, y=1202) # Caso o programa esteja minimizado ele o abre novamente
    cursor.click(x=2856, y=1202)  # Caso o programa esteja minimizado ele o abre novamente

    cursor.moveTo(x=2869, y=292) # Cursor do mouse se move nas coordenadas x=2869 e y=292.

    cursor.scroll(-100) #Scroll do mouse passa para o próximo vídeo.

    time.sleep(quant) # O Programa espera o tempo máximo do vídeo que é 1 minuto e continua.
    cont +=1
    print(f'Você ja viu {cont} vídeos')


