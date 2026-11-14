import requests
def discord(webhook,mensaje):
	try:
		respuesta = requests.post(
			webhook,
			json={"content":mensaje},
			timeout=10
		)
		respuesta.raise_for_status()
		return True, ""
	except requests.exceptions.RequestException as e:
		return False, f" {e}"