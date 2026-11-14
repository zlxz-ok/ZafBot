from InquirerPy import inquirer
from monitor import revisarpro,driveri,auto
from database import view,get,addproduct,editprice,webhookchange,deleteproduct
from urllib.parse import urlparse
from rich.console import Console
import json
import time,random
console = Console()
def menucli():
    try:
        with open("config.json", "r") as config:
            config_datos = json.load(config)
            notificar = config_datos["notificaciones"]
            selector = config_datos["selector"]
    except FileNotFoundError:
        notificar = False
        selector = ""
        with open("config.json", "w") as archivo:
            config_datos = {"notificaciones": False, "selector": selector}
            json.dump(config_datos, archivo)
    while True:
        menu = inquirer.select(
            message="Seleccione Una Opcion",
            choices=[
                "Ver Productos",
                "Automatizar",
                "Agregar Producto",
                "Eliminar Producto",
                "Editar Precio Estimado",
                "Editar Webhook",
                "Configuración",
                "Salir"
            ]
        ).execute()
        if menu == "Ver Productos":
            viewall = view()
            if not viewall:
                console.print("[bold red]No hay productos agregados[/bold red]")
            for id,name,link,precio in viewall:
                console.print(f"ID: [bold yellow]{id}[/bold yellow]")
                console.print(f"Product: [bold blue]{name}[/bold blue]")
                console.print(f"Link: [bold green]{link}[/bold green]")
                console.print(f"Precio Estimado: [bold green]{precio}[/bold green]")
            ask = inquirer.confirm(
                message="Consultar Precios?"
            ).execute()
            if ask:
                productos = get()
                wait = random.uniform(2,4)
                for datos in productos:
                    exito,mensaje,*_ = revisarpro(datos["name"],datos["link"],datos["precio"],selector,notificar=notificar)
                    if not exito:
                        console.print(f"[yellow]{mensaje}[/yellow]")
                    elif not notificar:
                        console.print(f"[yellow]{mensaje}[/yellow]")
                    time.sleep(wait)
                time.sleep(0.5)
            else:
                time .sleep(0.5)
                pass
        elif menu == "Agregar Producto":
            name = inquirer.text(
                message="Nombre Del Producto:"
            ).execute()
            link = inquirer.text(
                message="Link Del Producto:"
            ).execute()
            precio = inquirer.number(
                message="Precio Estimado:"
            ).execute()
            parsed = urlparse(link)
            if parsed.scheme not in ("http", "https") or not parsed.netloc:
                console.print("[bold red]URL inválida[/bold red]")
            else:
                addproduct(name,link,precio)
                time.sleep(0.5) 
        elif menu == "Eliminar Producto":
            iddelete = inquirer.number(
                message="ID Del Producto:"
            ).execute()
            exito = deleteproduct(iddelete)
            if exito:
                console.print("[bold green]Producto Eliminado Con Exito[/bold green]")
            else:
                console.print("[bold red]Error al eliminar el producto[/bold red]")
            time.sleep(0.5)
        elif menu == "Editar Precio Estimado":
            idnewprice = inquirer.number(
                message="ID Del Producto:"
            ).execute()
            newprice = inquirer.number(
                message="Nuevo Precio Estimado:"
            ).execute()
            exito = editprice(newprice,idnewprice)
            if exito:
                console.print("[bold green]Precio Modificado Con Exito[/bold green]")
            else:
                console.print("[bold red]Error al modificar el precio[/bold red]")
        elif menu == "Editar Webhook":
            editweb = inquirer.text(
                message="Nueva Webhook:"
            ).execute()
            exito,mensaje = webhookchange(editweb)
            if not exito:
                console.print(f"[bold red]{mensaje}[/bold red]")
            else:
                console.print(f"[bold green]{mensaje}[/bold green]")
        elif menu == "Automatizar":
            ask2 = int(inquirer.number(
                message="Intervalo En Minutos:",
                float_allowed=False	
            ).execute())
            minutes = ask2*60
            if ask2 <= 0:
                console.print("[bold red]Ingrese un numero mayor a 0[/bold red]")
            else:
                 state,message = auto(minutes)
                 if not state:
                     console.print(f"[bold red]{message}[/bold red]")
        elif menu == "Salir":
            driveri.quit()
            break
        elif menu == "Configuración":
            config = inquirer.select(
                message="Que Desea Configurar",
                choices=[
                    "Notificaciones",
                    "Selector CSS"
                ]
            ).execute()
            if config == "Notificaciones":
                ask1 = inquirer.confirm(
                    message="Activar Notificaciones?"
                ).execute()
                if ask1:
                    notificar = ask1
                    config_datos["notificaciones"] = True
                    with open ("config.json","w") as config:
                        json.dump(config_datos,config)
                else:
                    notificar = ask1
                    config_datos["notificaciones"] = False
                    with open ("config.json","w") as config:
                        json.dump(config_datos,config)
            elif config == "Selector CSS":
                ask3 = inquirer.text(
                    message="Selector CSS:"
                ).execute()
                if ask3 == "":
                    console.print(f"[bold red]Ingrese un selector valido[/bold red]")
                else:
                    selector = ask3
                    config_datos["selector"] = ask3
                    with open ("config.json","w")as config:
                        json.dump(config_datos,config)