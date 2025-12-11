import pyautogui
import time

pyautogui.PAUSE = 0.5
# abrir meu navegador (Chrome)
# pyautogui.press() -> apertar 1 tecla
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar várias teclas juntas ex('ctrl', 'c')

# abrir meu navegador (Chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(4)

pyautogui.click(x=987, y=403)

# Esperar a tela de seleção de perfil aparecer
pyautogui.write('hashtagtreinamentos.com/curso-python') # Aqui é a URL que utilizei para teste mas pode substitui por outra qualquer
pyautogui.press('enter')

time.sleep(4)

# Aqui foram as cordenadas que utilizei para clicar no botão do formulário, você pode alterar conforme a sua tela
pyautogui.click(x=231, y=642)

# print(pyautogui.position())

# preencher o formulário, 
time.sleep(2)

pyautogui.write('SEU NOME COMPLETO') 
pyautogui.press('tab')

pyautogui.write('SEU E-MAIL')
pyautogui.press('tab')  

pyautogui.write('SEU TELEFONE')
pyautogui.press('tab')

# enviar formulário     
pyautogui.press('enter')         