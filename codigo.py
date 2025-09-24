import pyautogui
import time

# Abrir o Google Chrome
pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.write("http://127.0.0.1:5500/automacao_python/")
pyautogui.press("enter")
pyautogui.click(x=1019, y=434)
pyautogui.write("Gian Pablo Benvive Torres")
pyautogui.press("tab")
pyautogui.write("giantorresbenvive@gmail.com")
pyautogui.press("tab")
pyautogui.write("147963258@")
pyautogui.press("tab")
pyautogui.press("space")
pyautogui.press("tab")
pyautogui.press("enter")