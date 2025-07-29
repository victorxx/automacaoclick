import pyautogui
import time

# Coordenadas do botão de curtir — ajuste conforme necessário
curtir_x, curtir_y = 1104, 422 

while True:
    try:
        print('Programa iniciando. Não mexa em nada...')
        time.sleep(60)  # Tempo para posicionar o navegador no post certo

        while True:
            # Mover o mouse até o botão "Curtir"
            pyautogui.moveTo(curtir_x, curtir_y, duration=1)

            # Simular o clique rápido (3 cliques)
            for x in range(3):
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(0.2)

            print("Post curtido com 2 cliques rápidos!")
            time.sleep(20)

            # Atualizar a página
            pyautogui.press('f5')
            print("Página atualizada. Aguardando 12 horas...")

            # Esperar 12 horas
            time.sleep(43200)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print("Reiniciando o processo em 60 segundos...")
        time.sleep(60)  # Tempo antes de tentar novamente
