import tkinter as tk
from vistaMenuPrincipal import menu

class appMain:
    def __init__(self):
        #Inicializa la ventana principal
        self.base = tk.Tk()
        self.base.geometry("1080x580")
        self.base.title("LubriControl")

        #Llama al Menú
        menu(self.base)

#Para que solo se ejecute la app (Ni le toquen)
if __name__ == "__main__":
    app=appMain()
    app.base.mainloop()
        

