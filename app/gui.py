from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox as popup
import turtle as t
from turtle import Canvas, RawTurtle, TurtleScreen

import bbdd as bd
import algoritmo as alg

primera_parada = True
segunda_parada = True
global origen, destino

origen_text = ""
destino_text = ""
path = []

elements = []

global sc, pathwindow, a

sc = None
    
def iniciar():
    global path, sc, pathwindow, window
    global init_button, init_button_osc, reinit_button, reinit_button_osc

    # Deshabilitar el uso de la ventana principal
    window.wm_attributes('-disabled', True)
    canvas.itemconfigure(block, state='normal')

    # Oscurecer el botón de inicio
    init_button.place_forget()
    init_button_block.place(
        x = 189.0,
        y = 662.0,
        width = 222.0,
        height = 78.0
    )
    # Oscurecer el botón de reinicio
    reinit_button.place_forget()
    reinit_button_block.place(
        x=191.0,
        y=754.0,
        width=222.0,
        height=78.0
    )

    # Otra opción para bloquear el uso de la pantalla de inicio que
    # en este caso despliga una ventana emergente de error al clickar.
    window.bind('<Button 1>', errorWindow)

    # Crear objeto turtle que despliega una nueva ventana
    sc = t.Screen()
    sc.title("Trayecto óptimo - " + origen.nombre + " a " + destino.nombre)

    # Asignar tamaño de ventana y centrar en la vista
    frm_width = window.winfo_rootx() - window.winfo_x()
    height = 900
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    y = window.winfo_screenheight()//2 - win_height//2
    sc.setup(820,900, startx = None, starty = y)

    # Obtener la equivalencia canvas para expandir funcionalidades
    pathwindow = sc.getcanvas().winfo_toplevel()
    pathwindow.iconbitmap("./build/assets/frame0/metro.ico")
    # Bloquear la redimensión de la pantalla
    pathwindow.resizable(0,0)
    # Ejecutar la funcion on_close_sc al intentar cerrar la ventana
    pathwindow.protocol("WM_DELETE_WINDOW", on_close_sc)
    # Mantener la ventana por encima del resto
    pathwindow.grab_set()
    pathwindow.deiconify()

    # Establecer el fondo de la ventana
    sc.bgpic("./build/assets/frame0/metro_map.png")

   # Crear objeto que se encarga de dibujar sobre la ventana
    a = t.RawTurtle(sc)
    a.hideturtle()

    # Imprime el valor de las coordenadas al clickar
    # sc.onclick(position, btn=1)

    # Obtener el trayecto óptimo entre dos paradas 
    path = alg.aStarAlgo(origen, destino)

    # Dibuja un círculo en la parada de origen 
    t.speed(8)
    t.hideturtle()
    t.pensize(4)
    t.up()
    t.setposition((origen.printCoords[0], origen.printCoords[1] - 5))
    t.down()
    t.fillcolor("black")
    #t.fillcolor(origen.color)
    t.begin_fill()
    t.circle(6)
    t.end_fill()
    
    # Dibuja el trayecto óptimo
    a.speed(0)
    a.hideturtle()
    a.pen(pensize=7)
    a.color("black")
    a.penup()
    for p in path:
        #a.color(p.color)
        a.goto(p.printCoords[0], p.printCoords[1])
        a.speed(1.5)
        a.pendown()
    a.penup()
    a.hideturtle()

    # Dibuja un círculo en la parada de destino
    t.hideturtle()
    t.pensize(4)
    t.up()
    t.setposition((destino.printCoords[0], destino.printCoords[1] - 5))
    t.down()
    t.fillcolor("black")
    #t.fillcolor(destino.color)
    t.begin_fill()
    t.circle(6)
    t.end_fill()

def reiniciar():
    global primera_parada
    global segunda_parada

    clean_elements()

    canvas.itemconfigure(line_input2, state='normal') # Seleccionar origen
    canvas.itemconfigure(line_input2_blanco, state='hidden') # Seleccionar en blanco
    canvas.itemconfigure(line_input, state='hidden') # Seleccionar destino
    canvas.itemconfigure(end_title, state='hidden') # Destino del trayecto
    canvas.itemconfigure(points, state='hidden') # Puntos
    canvas.itemconfigure(line_input_blanco, state='hidden')
    init_button.place_forget()
    reinit_button.place_forget()
    canvas.itemconfigure(origen_text, state='hidden')
    canvas.itemconfigure(destino_text, state='hidden')
    primera_parada = True
    segunda_parada = True
    # Oscurecer ventana principal 
    canvas.itemconfigure(block, state='hidden')
    # Iniciar oscuro
    init_button_block.place_forget()
    # Reiniciar oscuro
    reinit_button_block.place_forget()
    # Click handler reseteado
    window.bind('<Button 1>', motion)
    a.hideturtle()

def motion(event):
    global primera_parada, segunda_parada
    global origen_text, destino_text 
    global origen, destino

    x, y = event.x, event.y
    parada = bd.which_stop(x,y)

    if parada != None:
        print(parada.nombre + ' {}, {}'.format(x, y))
    else:
        print('{}, {}'.format(x, y))
    
    if(primera_parada):
        if(parada is not None):
            canvas.itemconfigure(line_input2, state='hidden')
            canvas.itemconfigure(line_input2_blanco, state='normal')
            origen_text = canvas.create_text(
                151.0,
                358.0,
                anchor="nw",
                text=parada,
                fill="#222222",
                font=("Inter Medium", 18 * -1)
            )
            canvas.itemconfigure(line_input, state='normal')
            canvas.itemconfigure(end_title, state='normal')
            canvas.itemconfigure(points, state='normal')
            primera_parada = False
            origen = parada
            origin = canvas.create_oval(parada.coords[0]-7, parada.coords[1]-7, parada.coords[0] + 7, parada.coords[1] + 7, fill="black")
            elements.append(origin)
            
    elif(segunda_parada):
        if(parada is not None):
            if(parada == origen):
                popup.showwarning("Error en la selección de destino", "Has seleccionado la misma parada para el origen y destino. Por favor, selecciona otra parada.")
                return
            destino = parada
            canvas.itemconfigure(line_input, state='hidden')
            canvas.itemconfigure(line_input_blanco, state='normal')
            destino_text = canvas.create_text(
                151.0,
                576.0,
                anchor="nw",
                text=parada,
                fill="#222222",
                font=("Inter Medium", 18 * -1)
            )
            init_button.place(
                x=189.0,
                y=662.0,
                width=222.0,
                height=78.0
            )
            reinit_button.place(
                x=191.0,
                y=754.0,
                width=222.0,
                height=78.0
            )
            segunda_parada = False
            goal = canvas.create_oval(parada.coords[0]-7, parada.coords[1]-7, parada.coords[0] + 7, parada.coords[1] + 7, fill="black")
            elements.append(goal)

def on_close_window():
    global sc
    if popup.askyesno("Salir", "¿Estás seguro de que quieres salir del programa?"):
        if sc is not None:
            sc.bye()
        window.destroy()
        
def on_close_sc():
    close = popup.askyesno("Confirmación de cierre de ventana", "Si cierras la ventana, se perderá el trayecto obtenido.\n¿Quieres continuar?", parent=pathwindow)
    if close:
        window.wm_attributes('-disabled', False)
        window.wm_attributes('-topmost', True)
        window.wm_attributes('-topmost', False)
        sc.reset()
        pathwindow.withdraw()
        reiniciar()

def clean_elements():
    global elements
    for p in elements:
        canvas.delete(p)
    elements.clear()

def position(x,y):
    print('{}, {}'.format(x, y))

# Optional feature to block main windows use
def errorWindow(event):
    #popup.showerror("Uso denegado", "Cierre la ventana emergente antes de volver a la principal.")
    print("Ventana bloqueada")

def center_window(window):
    window.update_idletasks()
    width = 1440
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2*frm_width
    height = 900
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth()//2 - win_width//2
    y = window.winfo_screenheight()//2 - win_height//2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.deiconify()

# Creación de ventana principal
window = Tk()
window.geometry("1440x900")
window.resizable(0,0)
window.title(" Atenas Underground")
window.iconbitmap("./build/assets/frame0/metro.ico") 
window.configure(bg = "#494AA0")
# Centrar la ventana.
center_window(window)
# Al clickar en la ventana, se ejecuta motion, que se  
# encargará de realizar los cambios oportunos en la ventana
window.bind('<Button 1>', motion)

# Creación objeto canvas en el que se crean y situan los elementos
canvas = Canvas(
    window,
    bg = "#494AA0",
    height = 900,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

image_line_input = PhotoImage(
    file="./build/assets/frame0/line_input.png")
line_input = canvas.create_image(
    301.0,
    586.0,
    image=image_line_input
)
canvas.itemconfigure(line_input, state='hidden')

image_line_input_blanco = PhotoImage(
    file="./build/assets/frame0/line_input_blanco.png")
line_input_blanco = canvas.create_image(
    301.0,
    586.0,
    image=image_line_input_blanco
)
canvas.itemconfigure(line_input_blanco, state='hidden')

image_end_title = PhotoImage(
    file="./build/assets/frame0/end_title.png")
end_title = canvas.create_image(
    295.0,
    496.0,
    image=image_end_title
)
canvas.itemconfigure(end_title, state='hidden')

image_line_input2 = PhotoImage(
    file="./build/assets/frame0/line_input.png")
line_input2 = canvas.create_image(
    301.0,
    369.0,
    image=image_line_input2
)

image_line_input2_blanco = PhotoImage(
    file="./build/assets/frame0/line_input_blanco.png")
line_input2_blanco = canvas.create_image(
    301.0,
    369.0,
    image=image_line_input2_blanco
)
canvas.itemconfigure(line_input2_blanco, state='hidden')

image_origin_title = PhotoImage(
    file=r"./build/assets/frame0/origin_title.png")
origin_title = canvas.create_image(
    295.0,
    279.0,
    image=image_origin_title
)

button_line_input = PhotoImage(
    file="./build/assets/frame0/init_button.png")
init_button = Button(
    image=button_line_input,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: iniciar(),
    relief="flat"
)

iniciar_block = PhotoImage(
    file="./build/assets/frame0/init_button_osc.png")
init_button_block = Button(
    image=iniciar_block,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
)

button_end_title = PhotoImage(
    file="./build/assets/frame0/reinit_button.png")
reinit_button = Button(
    image=button_end_title,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: reiniciar(),
    relief="flat"
)

reiniciar_block = PhotoImage(
    file="./build/assets/frame0/reinit_button_osc.png")
reinit_button_block = Button(
    image=reiniciar_block,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)

image_metro_map = PhotoImage(
    file="./build/assets/frame0/metro_map.png")
metro_map = canvas.create_image(
    1030.0,
    450.0,
    image=image_metro_map
)

image_path_icon = PhotoImage(
    file="./build/assets/frame0/path_icon.png")
path_icon = canvas.create_image(
    492.0,
    131.0,
    image=image_path_icon
)

image_title = PhotoImage(
    file="./build/assets/frame0/title.png")
title = canvas.create_image(
    270.0,
    127.0,
    image=image_title
)

image_points = PhotoImage(
    file="./build/assets/frame0/points.png")
points = canvas.create_image(
    298.0,
    429.0,
    image=image_points
)
canvas.itemconfigure(points, state='hidden')

image_block = PhotoImage(
    file="./build/assets/frame0/blocked.png")
block = canvas.create_image(
    1440/2,
    900/2,
    image=image_block
)
canvas.itemconfigure(block, state='hidden')

window.protocol("WM_DELETE_WINDOW", on_close_window)

window.mainloop()