import pyautogui
import time

# Posição do botão "Curtir"
# Use pyautogui.position() para descobrir a posição correta
try:
    curtir_x, curtir_y = 1144, 488 
    print('Programa iniciando. Não mexa em nada...')
    time.sleep(60)

    while True:
        # Mover até o botão "Curtir"
        pyautogui.moveTo(curtir_x, curtir_y, duration=1)
        pyautogui.click()

        print("Post curtido!")

        # Pressionar F5 para atualizar a página
        pyautogui.press('f5')
        print("Página atualizada. Aguardando 24 horas...")

        # Aguardar 24 horas (86.400 segundos)
        time.sleep(86400)

except Exception as e:
    print(f"Ocorreu um erro: {e}")
