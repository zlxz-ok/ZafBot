import customtkinter
import threading
stop = threading.Event()
from urllib.parse import urlparse
from database import view,addproduct,deleteproduct,get,webhookchange
from monitor import revisarpro,auto
import threading
import time,random
import json
try:
    with open ("config.json","r") as config:
        datos = json.load(config)
        notificar = datos["notificaciones"]
        selector = datos["selector"]
except FileNotFoundError:
    notificar = False
    with open ("config.json","w") as archivo:
        json.dump({"notificaciones":False,"selector":""},archivo)
global app
#Cambiar de Frames
def change(frame,actual,actual1):
    actual.pack_forget()
    actual1.pack_forget()
    frame.pack(fill="both",expand=True)

#Consultar Precios
def consul():
    with open("config.json","r")as config:
        selector = json.load(config)["selector"]
    wait = random.uniform(2,4)
    products = get()
    for i,datos in enumerate(products):
        exito,mensaje,*shit = revisarpro(datos["name"],datos["link"],datos["precio"],selector,notificar=notificar) 
        if not exito:
            errorwin(mensaje,"Error")
        elif not notificar:
            global precl
            global app
            app.after(0,lambda i=i,shit=shit: precl[i].configure(text=f"Precio Actual:{shit[0]}"))
        time.sleep(wait)
#Guardar configuracion
def saveconfig():
    global notis
    global web
    global notificar
    global selector
    noti = notis.get()
    notificar = bool(noti)
    selectore = selector.get().strip()
    if selectore == "":
      with open("config.json", "r") as config:
        selectore = json.load(config)["selector"]
    webe = web.get().strip()
    with open ("config.json","w") as archivo:
        json.dump({"notificaciones":bool(noti),"selector":selectore},archivo)
    if webe == "":
        errorwin("No configuraste WebHook!, o tal vez ya tienes una?","Exito")
    elif selectore == "":
        errorwin("No configuraste ningun selector CSS, no podras obtener el precio, o ya tienes una?","Exito")
    else:
      exito,mensaje = webhookchange(webe)
      if not exito:
          errorwin(mensaje,"Error")
      else:
          errorwin(mensaje,"Exito")
#Enviar datos a monitoreo
monst = False
def catch():
    global monst
    if monst:
        return
    else:
        monst =True 
    choice = minut.get()
    choice = int(choice.split()[0]) * 60
    stop.clear()
    threading.Thread(target=auto,args=(choice,stop),daemon=True).start()
#Detener
def stopmon():
    global monst
    stop.set()
    monst = False
#Pantalla de Error MultiFuncional
def errorwin(message,state):
    window = customtkinter.CTkToplevel()
    window.geometry("400x300")
    window.title(f"{state} - {state}")
    errorl = customtkinter.CTkLabel(window, text=f"{state}. Lea bien el mensaje para entender que sucedio.",font=("Arial",15,"bold"),text_color="purple")
    errorl.pack()
    error = customtkinter.CTkTextbox(window)
    error.insert("0.0",message)
    error.configure(state="disabled")
    error.pack()
    close = customtkinter.CTkButton(window,text="Salir",hover_color="black",command=lambda:window.destroy())
    close.pack()
#Reiniciar Los Articulos
def restartpro():
    global mainarsv
    global main
    viewall = view()
    if not viewall:
        errorwin("No Hay Productos,Agregue Algunos!","Error")
    mainarsv.destroy()
    mainarsv = customtkinter.CTkFrame(main,fg_color="#242424")
    mainarsv.pack(anchor="nw", padx=25, pady=25)
    arsvtitle = customtkinter.CTkLabel(mainarsv, text="Articulos Guardados",font=("Arial",24,"bold"))
    arsvtitle.pack()
    global precl
    precl = []
    for id,name,link,precio in viewall:
        proframe = customtkinter.CTkFrame(mainarsv)
        proframe.pack(fill="x",padx=10, pady=5)
        proname = customtkinter.CTkLabel(proframe, text=f"{id}. {name}",font=("Arial",15,"bold"))
        proname.grid(row=0, column=0, padx=10, pady=5)
        prolink = customtkinter.CTkEntry(proframe,height=15,width=200)
        prolink.insert(0,f"{link}")
        prolink.configure(state="readonly")
        prolink.grid(row=1, column=0, padx=0, pady=0)
        proprice = customtkinter.CTkLabel(proframe, text=f"Precio Objetivo:${precio}",font=("Arial",11,"bold"))
        proprice.grid(row=0, column=1, padx=10, pady=5)
        realprice = customtkinter.CTkLabel(proframe, text=f"Precio Actual:",font=("Arial",13,"bold"),text_color="green")
        realprice.grid(row=1,column=1,padx=10, pady=5)
        precl.append(realprice)
#Agregar Articulos
def addart():
    window = customtkinter.CTkToplevel()
    window.geometry("400x300")
    window.title("Agregar Producto")
    namel = customtkinter.CTkLabel(window, text="Nombre Del Producto:",font=("Arial",15,"bold"))
    namel.pack()
    name = customtkinter.CTkEntry(window,placeholder_text="Nombre del producto")
    name.pack()
    preciol = customtkinter.CTkLabel(window,text="Precio De Referencia:",font=("Arial",15,"bold"))
    preciol.pack()
    precio = customtkinter.CTkEntry(window, placeholder_text="Precio del producto")
    precio.pack()
    errorprecio = customtkinter.CTkLabel(window,text="",text_color="red")
    errorprecio.pack()
    linkl = customtkinter.CTkLabel(window, text="Link Del Producto",font=("Arial",15,"bold"))
    linkl.pack()
    link = customtkinter.CTkEntry(window, placeholder_text="Link del producto")
    link.pack()
    errorlink = customtkinter.CTkLabel(window,text="",text_color="red")
    errorlink.pack()
    def validate():
        parsed = urlparse(link.get())
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            errorlink.configure(text="Introduce Un Link Válido")
            return
        try:
            price = float(precio.get())
            if price < 0:
                errorprecio.configure(text="Introduce Un Numero Válido")
                return
        except ValueError:
            errorprecio.configure(text="Introduce Un Numero Válido") 
        else:
            addproduct(name.get(),link.get(),precio.get())
            restartpro()
            window.destroy()
    send = customtkinter.CTkButton(window, text="Guardar Producto",hover_color="black",command=validate)
    send.pack()
#Eliminar articulos
def delart():
    window = customtkinter.CTkToplevel()
    window.geometry("400x300")
    window.title("Eliminar Producto")
    idl = customtkinter.CTkLabel(window, text="ID Del Producto:",font=("Arial",15,"bold"))
    idl.pack()
    id = customtkinter.CTkEntry(window,placeholder_text="ID del producto")
    id.pack()
    errorid = customtkinter.CTkLabel(window, text="",text_color="red")
    errorid.pack()
    def validate():
        try:
            ide = int(id.get())
            exito = deleteproduct(ide)
            if exito:
                errorid.configure(text="Producto Eliminado Con Exito",text_color="green")
                restartpro()
                window.destroy()
            else:
                errorid.configure(text="Error al eliminar el producto")
        except ValueError:
            errorid.configure(text="Ingrese Un Numero Válido")
    send = customtkinter.CTkButton(window, text="Eliminar Producto",hover_color="black",command=validate)
    send.pack()
def gui():
    global app
    app = customtkinter.CTk()
    app.geometry("900x600")
    app.title("Zafbot - Home")
    customtkinter.set_appearance_mode("dark")
    viewall = view()
    if not viewall:
        errorwin("No Hay Productos,Agregue Algunos!","Error")
    navegation = customtkinter.CTkFrame(app,width=200)
    navegation.pack(side="left",fill="both")
    navegation.pack_propagate(False)
    global main
    main = customtkinter.CTkFrame(app,fg_color="#242424")
    main.pack(fill="both",expand=True)
    navtitle = customtkinter.CTkLabel(navegation, text="ZafBot",font=("Arial",24,"bold"))
    navtitle.pack(pady=25)
    navpro = customtkinter.CTkButton(navegation, text="Productos",command=lambda: change(main,mainconfig,mainmon))
    navpro.pack(fill="x", padx=10, pady=5)
    navmon = customtkinter.CTkButton(navegation, text="Monitoreo",command=lambda:change(mainmon,main,mainconfig))
    navmon.pack(fill="x", padx=10, pady=5)
    navconf = customtkinter.CTkButton(navegation, text="Configuración",command=lambda:change(mainconfig,main,mainmon))
    navconf.pack(fill="x", padx=10, pady=5)
    #Frame Configuracion "mainconfig"
    mainconfig = customtkinter.CTkFrame(app,fg_color="#242424")
    confititle = customtkinter.CTkLabel(mainconfig,text="Configuración",font=("Arial",24,"bold"))
    confititle.pack(anchor="nw", padx=25, pady=25)
    global notis
    global web
    global selector
    notis = customtkinter.CTkCheckBox(mainconfig,text="Notificaciones",font=("Arial",13,"bold"))
    notis.pack(anchor="nw",padx=25)
    if notificar:
        notis.select()
    else:
        notis.deselect()
    webl = customtkinter.CTkLabel(mainconfig,text="Configurar Webhook(notificaciones OBLIGATORIO)",font=("Arial",15,"bold"))
    webl.pack(anchor="nw",padx=25,pady=10)
    web = customtkinter.CTkEntry(mainconfig,placeholder_text="Tu WebHook:")
    web.pack(anchor="nw",padx=25,pady=10)
    selectorl = customtkinter.CTkLabel(mainconfig, text="Selector CSS del precio", font=("Arial",15,"bold"))
    selectorl.pack(anchor="nw", padx=25, pady=10)
    selector = customtkinter.CTkEntry(mainconfig, placeholder_text="Ejemplo: .price")
    selector.pack(anchor="nw", padx=25, pady=10)
    savebu = customtkinter.CTkButton(mainconfig,text="Guardar",fg_color="#67597A",hover_color="#85BAA1",command=saveconfig)
    savebu.pack()

    #Frame Monitoreo "mainmon"
    mainmon = customtkinter.CTkFrame(app,fg_color="#242424")
    montitle = customtkinter.CTkLabel(mainmon,text="Monitoreo",font=("Arial",24,"bold"))
    montitle.pack(anchor="nw", padx=25, pady=25)
    minul = customtkinter.CTkLabel(mainmon,text="Preferencias Monitoreo",font=("Arial",24,"bold"))
    minul.pack()
    global minut
    minut = customtkinter.CTkOptionMenu(mainmon, values=["1 Minuto", "30 Minutos", "60 Minutos"])
    minut.pack(anchor="nw", padx=25, pady=25)
    activate = customtkinter.CTkButton(mainmon,text="Activar Monitoreo",fg_color="#0B6E4F",hover_color="black",command=catch)
    activate.pack()
    global monst
    deactivate = customtkinter.CTkButton(mainmon,text="Parar Monitoreo",fg_color="#721817",hover_color="black",command=stopmon)
    deactivate.pack()
    awrn = customtkinter.CTkLabel(mainmon,text="Deberas tener una WebHook Configurada",font=("Arial",12,"bold"))
    awrn.pack(anchor="nw", padx=25, pady=25)



    protitle = customtkinter.CTkLabel(main, text="Productos",font=("Arial",24,"bold"))
    protitle.pack(anchor="nw", padx=25, pady=25)
    #main buttons
    mainbut = customtkinter.CTkFrame(main)
    mainbut.pack(anchor="nw", padx=25, pady=25)
    add = customtkinter.CTkButton(mainbut, text="Agregar Producto",fg_color="#3EC300",text_color="black",hover_color="#CEEDDB",width=150,height=50,command=addart)
    add.grid(row=0,column=0,padx=5)
    delete = customtkinter.CTkButton(mainbut, text="Eliminar Producto",fg_color="#E13700",text_color="black",hover_color="#03254E",width=150,height=50,command=delart)
    delete.grid(row=0,column=1,padx=5)
    cons = customtkinter.CTkButton(mainbut, text="Consultar Precios",fg_color="#067BC2",text_color="black",hover_color="#7CDF64",width=150,height=50,command=lambda: threading.Thread(target=consul).start())
    cons.grid(row=0,column=2,padx=5)
    #main articles saved
    global mainarsv
    mainarsv = customtkinter.CTkFrame(main,fg_color="#242424")
    mainarsv.pack(anchor="nw", padx=25, pady=25)
    arsvtitle = customtkinter.CTkLabel(mainarsv, text="Articulos Guardados",font=("Arial",24,"bold"))
    arsvtitle.pack()
    global precl
    precl = []
    for id,name,link,precio in viewall:
        proframe = customtkinter.CTkFrame(mainarsv)
        proframe.pack(fill="x",padx=10, pady=5)
        proname = customtkinter.CTkLabel(proframe, text=f"{id}. {name}",font=("Arial",15,"bold"))
        proname.grid(row=0, column=0, padx=10, pady=5)
        prolink = customtkinter.CTkEntry(proframe,height=15,width=200)
        prolink.insert(0,f"{link}")
        prolink.configure(state="readonly")
        prolink.grid(row=1, column=0, padx=0, pady=0)
        proprice = customtkinter.CTkLabel(proframe, text=f"Precio Objetivo:${precio}",font=("Arial",11,"bold"))
        proprice.grid(row=0, column=1, padx=10, pady=5)
        realprice = customtkinter.CTkLabel(proframe, text=f"Precio Actual:",font=("Arial",13,"bold"),text_color="green")
        realprice.grid(row=1,column=1,padx=10, pady=5)
        precl.append(realprice)
    app.mainloop()