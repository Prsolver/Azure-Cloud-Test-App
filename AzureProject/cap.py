import pyautogui

# Ekranın belirli bir konumuna fareyi hareket ettir
pyautogui.moveTo(100, 500)  # (x, y) koordinatları

# Orada tıklama yap
pyautogui.click()

# Eğer belirli bir süreyle hareket etmesini isterseniz
# pyautogui.moveTo(100, 150, duration=1)  # 1 saniye süresince hareket
