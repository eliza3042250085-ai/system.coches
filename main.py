from coches import coches
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_acciones(self):
            self.borrarPantalla()
            self.tipo = "Coches"
            Label(self.ventana, text= f"...::: Menu de {self.tipo} :::...").pack(pady=5)
            Button(self.ventana, text="1.- Agregar", command=self.insertar_view).pack(pady=10)
            Button(self.ventana, text="2.- Borrar", command=self.eliminar_view).pack(pady=10)
            Button(self.ventana, text="3.- Modificar", command=self.modificar_view).pack(pady=10)
            Button(self.ventana, text="4.- Mostrar", command=self.consultar_view).pack(pady=10)
            Button(self.ventana, text="5.- Regresar", command=self.main).pack(pady=10)     

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="\n...:: M E N U  P R I N C I P A L ::...").pack(pady=10)
        Button(self.ventana, text="1.- Coches", command=self.menu_acciones).pack(pady=5)
        Button(self.ventana, text="2.- Salir", command=self.ventana.quit).pack(pady=10)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar los datos del coche...").pack(pady=10)

        Label(self.ventana, text="Marca: ", anchor= 'e').pack(pady=10)
        self.marca = Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)
        Label(self.ventana, text="color: ").pack(pady=10)
        self.color = Entry(self.ventana)
        self.color.pack(pady=5)
        Label(self.ventana, text="modelo: ").pack(pady=10)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=5)
        Label(self.ventana, text="velocidad: ").pack(pady=10)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=5)
        Label(self.ventana, text="potencia: ").pack(pady=10)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=5)
        Label(self.ventana, text="asientos: ").pack(pady=10)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=5)
        Button(self.ventana, text="Guardar", command=lambda: {self.insertar_controller(), self.insertar_view()}).pack(pady=5)
        Button(self.ventana, text= "Regresar", command=self.menu_acciones).pack(pady=5)

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar el ID del coche a eliminar...").pack(pady=10)

        Label(self.ventana, text="ID: ").pack(pady=10)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        self.btn_buscar = Button(self.ventana, text= "Buscar", command=lambda: self.buscar_controller("Eliminar"))
        self.btn_buscar.pack(pady=5)
        

        self.btn_eliminar= Button(self.ventana, text= "Eliminar", state="disabled", command=lambda: {self.eliminar_controller(), self.eliminar_view()})
        self.btn_eliminar.pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar el ID del coche a modificar...").pack(pady=10)

        Label(self.ventana, text="ID: ").pack(pady=10)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana, text="Nueva Marca: ").pack(pady=10)
        self.marca = Entry(self.ventana)
        self.marca.pack(pady=5)

        Label(self.ventana, text="Nuevo color: ").pack(pady=10)
        self.color = Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana, text="Nuevo modelo: ").pack(pady=10)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana, text="Nueva velocidad: ").pack(pady=10)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana, text="Nueva potencia: ").pack(pady=10)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana, text="Nuevos asientos: ").pack(pady=10)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana, text="Guardar", command=lambda: {self.modificar_controller(), self.modificar_view()}).pack(pady=5)
        Button(self.ventana, text= "Regresar", command=self.menu_acciones).pack(pady=5)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...::Consultar los coches::...").pack(pady=10)
        filas=""
        filas=self.consultar_controller(filas)
        Label(self.ventana, text=f"{'Coche #':<15}{'ID':<15}{'marca':<15}{'color':<15}{'modelo':<15}{'velocidad':<15}{'potencia':<15}{'asientos':<15}").pack(pady=10)
        Label(self.ventana, text=f"{filas}").pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def cambiar_estado_btn(self, estado, tipo_accion):
        if estado: 
            if tipo_accion == "Eliminar":
                self.btn_eliminar.config(state="normal")
            elif tipo_accion == "Modificar":
                self.btn_modificar.config(state="normal")
        else:
            if tipo_accion == "Eliminar":
                self.btn_eliminar.config(state="disabled")
            elif tipo_accion == "Modificar":
                self.btn_modificar.config(state="disabled")

    def confirmar_eliminar(self, tipo):
        resp=messagebox.askquestion(title="... ¡Atención!...", message=f"¿Desea {tipo} el registro?...")
        if resp == "yes":
            return True
        else:
            return False



    def respuesta_sql(self, respuesta):
            if respuesta:
                messagebox.showinfo(title="... Exitoso ...", message= "Accion Realizada con Exito")
            else:
                messagebox.showerror(title="... ¡ Verifica por favor ! ...", message="Opcion invalida! ")
    
    def insertar_controller(self):
        coche1 = coches.Coches(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())                    
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1
        # self.insertar_view()

    def eliminar_controller(self):
        id=self.id.get()
        resp=self.confirmar_eliminar("eliminar")
        if resp:
            respuesta = coches.Coches.eliminar(id)
        else:
            respuesta = False
        self.respuesta_sql(respuesta)
 
    def modificar_controller(self):
        id=self.id.get()                     
        coche1 = coches.Coches(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1
        # self.modificar_view()

    def consultar_controller(self, filas):
        registros=coches.Coches.consultar()
        if len(registros) > 0:
            numero_coches=1
            for fila in registros:
                #Se va a concatenar con el + 
                filas=filas + f"{numero_coches:<15}{fila[0]:<15}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}\n"
                numero_coches += 1
        else:
            filas = "... ¡No existe datos que mostrar por el momento! ..."
        return filas

    def buscar_controller(self,tipo_accion):
        id=self.id.get()
        coche1 = coches.Coches.buscar(id)
        if len(coche1)>0:
            messagebox.showinfo(title="...El registro fue encontrado...",message=f"El registro fue encontrado con exito, se puede {tipo_accion}!...")
            self.cambiar_estado_btn(True, tipo_accion)
            #if tipo_accion == "Modificar":

        else:
            messagebox.showerror(title="... ¡ Verifica por favor ! ...", message=f"El registro no fue encontrado, {tipo_accion}!...")
            self.cambiar_estado_btn(False, tipo_accion)


if __name__=="__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()