from tkinter import Tk
from views.coches_view import AppView

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.vista=AppView(self.ventana)

 
if __name__=="__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()