import pyautogui
import time

try:
    # Coordenadas do botão de curtir — ajuste conforme necessário
    curtir_x, curtir_y = 1145, 500 

    print('Programa iniciando. Não mexa em nada...')
    time.sleep(60)  # Tempo para posicionar o navegador no post certo

    while True:
        # Mover o mouse até o botão "Curtir"
        pyautogui.moveTo(curtir_x, curtir_y, duration=1)

        # Simular o clique com uma pausa um pouco maior
        for x in range(2):
            pyautogui.mouseDown()  # Simula um clique mais firme
            time.sleep(0.1)  # Pode ajustar o tempo para maior firmeza
            pyautogui.mouseUp()
            time.sleep(0.5)  # Pausa entre os cliques

        print("Post curtido com 2 cliques firmes!")
        time.sleep(20)

        # Atualizar a página
        pyautogui.press('f5')
        print("Página atualizada. Aguardando 24 horas...")

        # Esperar 24 horas (em segundos)
        time.sleep(86400)

except Exception as e:
    print(f"Ocorreu um erro: {e}")
