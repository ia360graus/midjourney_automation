import time
import pyperclip
import pyautogui

time.sleep(10)

with open('prompts_midjourney.txt', 'r') as file:
    # Contador para rastrear a iteração
    contador = 0
    
    for line in file:
        # Incrementa o contador
        contador += 1

        # Copia a linha para a área de transferência
        pyperclip.copy(line.strip())
        
        # Aguarda um pouco para garantir que o texto foi copiado
        time.sleep(1)
        
        # Simula o atalho para colar (COMMAND+V) no Mac
        with pyautogui.hold(['command']):
            time.sleep(1)
            pyautogui.press('v')

        pyautogui.press('enter')

        # Se for a 8ª iteração, aguarda 1 minuto
        if contador == 8:
            print("Pausa de 5 minutos na 8ª iteração.")
            time.sleep(60)
            contador = 0

        # Aguarda 30 segundos antes de copiar e colar a próxima linha
        else:
            time.sleep(10)

        print(f"Linha copiada e colada: {line.strip()}")

print("Todas as linhas foram copiadas e coladas!")
