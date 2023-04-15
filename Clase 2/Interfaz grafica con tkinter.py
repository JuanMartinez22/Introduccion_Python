from tkinter import Tk ,Text,Button,END,re
class Interfaz:
    #valores iniciales     
    def __init__(self,ventana):
        #Inicializamos la ventana
        self.ventana=ventana
        self.ventana.title("CALCULADORA")
        #Agregamos caja de texto para mostrar las operaciones
        #El usuario no puede escribir nada por eso se le da un estado desabilitado
        self.pantalla=Text(ventana,state="disabled",width=40,height=3,background="#8d1c3d",foreground="white",font=("Helvetica",15))
        #ubicar la pantalla dentro de la ventana, gestores
        #pady es para no pegarlo al fin del recuadro 
        self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        #Inicializamos la operacion , esperando datos
        self.operacion=""

        #Creación de los botones de la calculadora
        boton1=self.crearBoton(7)
        boton2=self.crearBoton(8)
        boton3=self.crearBoton(9)
        boton4=self.crearBoton(u"\u232B",escribir=False)
        boton5=self.crearBoton(4)
        boton6=self.crearBoton(5)
        boton7=self.crearBoton(6)
        boton8=self.crearBoton(u"\u00F7")
        boton9=self.crearBoton(1)
        boton10=self.crearBoton(2)
        boton11=self.crearBoton(3)
        boton12=self.crearBoton("*")
        boton13=self.crearBoton(".")
        boton14=self.crearBoton(0)
        boton15=self.crearBoton("+")
        boton16=self.crearBoton("-")
        boton17=self.crearBoton("=",escribir=False,ancho=20,alto=2)


        #Ubicacion de los botones con el gestor grid
        botones=[boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16,boton17]
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador +=1
        #Ubicacion del boton del signo igual
        botones[16].grid(row=5,column=0,columnspan=4)
        
        return
    
    #crear  un botón mostrando el valor pasado por el parametro
    def crearBoton(self,valor,escribir=True,ancho=9,alto=1):
        #retorno del valor 
        return Button(self.ventana,text=valor,width=ancho,height=alto,font=("Helvetica",15),command=lambda:self.click(valor,escribir))
    

    #Metodo click , controla el click
    def click(self,texto,escribir):
        #si el prarametro "escribir" es True,entonces el parametro texto debe mostrarse en pantalla.
        if not escribir:
            #solo calcular si hay una operacion a ser evaluada y si el usuario presiono "="
            if texto=="=" and self.operacion !="":
                #Remplazar el valor de division por el operador '/'
                self.operacion=re.sub(u"\u00F7", "/", self.operacion)
                #Concatena todo la cadena de string y de valores puestos en pantalla
                # y evalua la operacion matematica del string
                resultado=str(eval(self.operacion))
                #Nueva operacion
                self.operacion=""
                #limpiar Pantalla
                self.limpiarPantalla()
                #Se muestra el resultado
                self.mostrarEnPantalla(resultado)
            #si se presionó el boton de borrado limpia la caja de texto , y llama al 
            # metodo limpiarPantalla()
            elif texto==u"\u232B":
                self.operacion=""
                self.limpiarPantalla()

        #si el boton tiene parametro en True
        else:
            #concatenacion de string
            self.operacion+=str(texto)
            #muestra la concatenacion de string en pantalla
            self.mostrarEnPantalla(texto)
        return
    
    def limpiarPantalla(self):
        #se confiugra la pantalla para modificarla
        self.pantalla.configure(state="normal")
        #indice de donde a donde recorre el delete delete("fila.columna",Final)
        self.pantalla.delete("1.0",END)
        #se vuelve a configurar la pantalla para desabilitarla
        self.pantalla.configure(state="disabled")
        return
    def mostrarEnPantalla(self,valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END,valor)
        self.pantalla.configure(state="disabled")
        return

#Instanciamos la ventana
ventana_principal=Tk()
calculadora=Interfaz(ventana_principal)
#bucle para mostrar la ventana
ventana_principal.mainloop()