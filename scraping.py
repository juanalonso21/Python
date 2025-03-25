import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configurar Selenium con Chrome WebDriver
options = Options()
options.add_argument("--headless")  # Ejecutar en modo sin interfaz gráfica
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Inicializar el WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL de la página de WhoScored (Ejemplo: Premier League)
url = "https://www.whoscored.com/Regions/252/Tournaments/2/England-Premier-League"

# Usar Selenium para cargar la página
driver.get(url)
time.sleep(3)  # Esperar a que cargue el contenido dinámico

# Obtener HTML de la página después de la carga completa
html = driver.page_source

# Cerrar el WebDriver
driver.quit()

# Parsear con BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Extraer información de partidos
matches = soup.find_all("div", class_="match")

for match in matches:
    teams = match.find_all("span", class_="team-name")
    if len(teams) == 2:
        team1 = teams[0].text.strip()
        team2 = teams[1].text.strip()
        print(f"Partido: {team1} vs {team2}")

# Si quieres extraer más datos (estadísticas, jugadores, etc.), inspecciona el HTML de WhoScored
