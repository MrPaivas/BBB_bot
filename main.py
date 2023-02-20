import time
import pyautogui

len_votos = 0


def votar():
    time.sleep(2)
    with pyautogui.hold('win'):
        pyautogui.press(['4', '4'])
    pyautogui.moveTo(1453, 428, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.moveTo(1330, 222, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1443, 410, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def salva_voto():
    with open('votos.txt', 'a') as txt:
        txt.write(f'Total de votos no Cristian:{len_votos}\n')
    return len_votos


while len_votos < 90:
    len_votos += 1
    votar()
    salva_voto()



