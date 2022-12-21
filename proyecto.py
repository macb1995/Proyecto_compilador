from asyncore import read
from tkinter import*
from tkinter import filedialog
from tkinter import font
from turtle import width
from webbrowser import get

ventana = Tk()
ventana.title("Compilador by MACB")
#ventana.geometry("1300x1000")
ventana.state('zoomed')
ventana.config(bg="#17202A") #color background 

#Abrir archivo ventana izquierda
def explorador():
    archivo = filedialog.askopenfilename(title="Explorador", initialdir="C:/Users/MELVIN ALEXANDER/Desktop/EDUCATION/UMG/COMPILADORES/COMPILADOR", filetypes=(("txt files","*_*"),("txt files","*.txt")))
    archivo = open(archivo,'r',encoding="utf-8")
    stuff = archivo.read()
    lectorv1.insert(END, stuff)
    archivo.close()

#def compilarArchivo():  
    #lectura.config(text=lectorv1.get(1.0, END))
    
#Diccionarios
operadores = {'=' : '= op Asignacion','+' : '+ op Adicion', '-' : '- op Substraccion', '/' : '/ op Division',
              '*' : '* op Multiplicacion', '<' : '< op Menor', '>' : '> op Mayor', '**' : 'op Potencia'}
operadores_key = operadores.keys()

data_type = {'int' : 'tipo integer', 'float': 'punto flotante', 'char' : 'tipo caracter',
             'long' : 'long int'}
data_type_key = data_type.keys()

puntuacion = {':' : 'dos puntos', ';' : 'punto y coma', '.': 'punto', ',' : 'coma'}
puntuacion_key = puntuacion.keys()

identificador = {'x' : 'id', 'y' : 'id', 'z' : 'id', 'f' : 'id'}
identificador_key = identificador.keys()

pReservadas = {'False' : 'Falso booleano', 'True' : 'Verdadero booleano', 'And' : 'Op Logico',
               'Def' : 'Definidor de Función', 'elif' : 'declaración condicional', 'if' : 'declaración condicional',
               'else' : 'declaración condicional', 'for' : 'ejecución de blucles', 'import' : 'importador de modulo',
               'in' : 'Comprobador de valores', 'return' : 'devuevle valor en función', 'while' : 'reliza bucles',
               'print' : 'Imprime en pantalla'}
pReservadas_key = pReservadas.keys()

#Leer archivo ventana derecha
def compilarArchivo():
    a = lectorv1.get(1.0,END)
    program = a.split("\n")
    print(program)
    count = 0 
    
    #split de variable compilarArchivo dividido en lineas con salto de linea
    pntoken = {' ', '\t', '\n'}

    for line in program:
        count += 1
        print("Linea: ", count, "\n", line)
        
        #lectura de tokens
        tokens = line.split(' ')
        print("Los Tokens son: ",tokens)
        print("Linea: ",count,"Propiedades: \n")
        token=""
        line +=""
        for c in line:
            if c in pntoken:
                if token in operadores_key:
                    print("el operador es: ",operadores[token])
                elif token in data_type_key:
                    print("el tipo de dato es: ", data_type[token])
                elif token in puntuacion_key:
                    print(token, "El simbolo de puntuación es: ", puntuacion[token])
                    
                elif token in pReservadas_key:
                    print(token, "Palabra reservada: ", [token])
                else:
                    print(token, "Identificador: ", [token])
                token = ""    
            else:
                token += c
    lectura.config(text=compilarArchivo)
    
#Ventana1 Izquierda superior
ventana1=Frame(ventana)
ventana1.place(x=10,y=40, width=670, height=550)
ventana1.config(bg="#0F0F0F")

scroll_1 = Scrollbar(ventana1)
scroll_1.pack(side=LEFT, fill=Y)

scroll_2 = Scrollbar(ventana1, orient=HORIZONTAL)
scroll_2.pack(side=BOTTOM, fill=X)

lectorv1 = Text(ventana1, yscrollcommand=scroll_1.set, xscrollcommand=scroll_2.set, font=('Microsoft Sans Serif',10), wrap="none")
lectorv1.place(x=20,y=0, width=650, height=530)
lectorv1.config(bg="#0F0F0F")
lectorv1.config(fg="yellow")

scroll_1.config(command=lectorv1.yview)
scroll_2.config(command=lectorv1.xview)

#ventana2 Derecha superior
ventana2=Frame(ventana, width=40, height=10)
ventana2.place(x=690,y=40, width=670, height=550)
ventana2.config(bg="#0F0F0F")
#ventana2.config(bg="white")

lectura = Label(ventana2, text='', justify=LEFT,font=('Microsoft Sans Serif',10))
lectura.place(relx=0.01, rely=0.01)
lectura.config(bg="#0F0F0F")
lectura.config(fg="#64FF00")

#ventana3 manejador de errores
verrores=Text(ventana, width=40, height=10)
verrores.place(x=10,y=600, width=1350, height=100)
verrores.config(bg="#0F0F0F")
verrores.config(fg="#64FF00")

label_manError = Label(verrores, text="Manejador de Errores")
label_manError.config(bg="#060606", fg="white")
label_manError.pack()

#MENU DE BOTONES
menu_botones = Frame(ventana, width=40, height=10)
menu_botones.place(x=5,y=5, width=1100, height=30)
menu_botones.config(bg="#17202A")

#boton Abrir 
boton1 = Button(menu_botones,text="Abrir archivo", command=explorador)
boton1.place(x=5,y=3)
boton1.config(bg="#154360") #color boton background
boton1.config(fg="#fff")

#boton2 Compilar
boton2 = Button(menu_botones, text="Compilar", command=compilarArchivo)
boton2.place(x=100,y=3)
boton2.config(bg="#154360") #color boton background
boton2.config(fg="#fff")

ventana.mainloop()