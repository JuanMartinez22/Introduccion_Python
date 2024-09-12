import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.generar()

    def generar(self):
        self.hello_label = tk.Label(self,text="Hola Mundo!")
        self.hello_label.pack(side="top")

        self.quit_button = tk.Button(self,text="Salir", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

root=tk.Tk()
app=Application(master=root)
app.mainloop()