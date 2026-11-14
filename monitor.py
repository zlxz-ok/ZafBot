from database import get,createcursor
from urllib.parse import urlparse
import json,random
import threading
stop = threading.Event()
from notifications.discord import discord
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
def crear_driver():
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    for argumento in ["--headless=new", "--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]:
        chrome_options.add_argument(argumento)

    try:
        return webdriver.Chrome(options=chrome_options)

    except WebDriverException:
        edge_options = EdgeOptions()
        for argumento in ["--headless=new", "--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]:
            edge_options.add_argument(argumento)

        return webdriver.Edge(options=edge_options)
driveri = crear_driver()
def auto(timesleep,stop=None):
    with open("config.json","r")as config:
         selector = json.load(config)["selector"]
    wait = random.uniform(2, 4)
    try:
        while stop is None or not stop.is_set():
            productos = get()
            for datos in productos:
                if stop is None and stop.is_set():
                  return
                exito,mensaje,*shit = revisarpro(datos["name"], datos["link"], datos["precio"],selector,notificar=True)
                if not exito:
                  return False,mensaje
                if stop is not None:
                  if stop.wait(wait):
                    return
            if stop is not None:
              if stop.wait(timesleep):
               return
    except KeyboardInterrupt:
        return False, "Automatizacion detenida"
def revisarpro(nombre,url,objetivo,selector,notificar=True):
	conexion = createcursor()
	cursor = conexion.cursor()
	try:
		driveri.get(url)
	except WebDriverException as e:
		return False, f"No se pudo abrir el producto {nombre}, Tal Vez Ingrese Una URL Valida?"
	r = driveri.page_source
	soup = BeautifulSoup(r,"html.parser")
	if "validateCaptcha" in r:		
		return False, f"El Producto {nombre} Dio Captcha, Recomendamos Esperar o Cambiar De Link"
	precio = soup.select_one(selector)
	if precio is None:
		return False, f"No se pudo encontrar el precio de : {nombre}"
	try:
		precio = precio.text
		precio = precio.replace("$","")
		precio = precio.replace(",","")
		precio = float(precio)
	except (ValueError,AttributeError):
		return False, f"No se pudo procesar el precio de {nombre},Tal Vez Cambia El Link?"
	if precio < objetivo:
		mensaje = f"La {nombre} bajo de precio,precio:${precio}"
	elif precio == objetivo:
		mensaje = f"La {nombre} sigue igual de precio,precio:${precio}"
	else:
		mensaje = f"La {nombre} subio de precio,precio:${precio}"
	if notificar:
		cursor.execute("""
  	  	SELECT url FROM config WHERE key = ?
  	    """,("webhook",))
		rel = cursor.fetchone()
		if rel is None or not rel[0]:
			return False, f"Configura una webhook primero"
		webhook = rel[0]
		exito,problem = discord(webhook,mensaje)
		if not exito:
			return False, f"Error al enviar la notificación,Tal Vez Configura Bien La Webhook?: {problem}"
	return True, mensaje, precio