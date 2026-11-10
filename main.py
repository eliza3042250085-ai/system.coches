from coches import coches
from tkinter import Label, Entry, Button, Tk, messagebox
print("\033c")

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0) # para poder modificar el tamaño desde la interfaz
        self.main()

    ## ...Vistas   
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        input("\n\t.... ¡Opcion invalidad, vuelve a intentarlo!.... ") 
        
    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Coches"
        Label(self.ventana,text=f"....:::: Menu de {tipo} ::::...\n").pack(pady=10)
        Button(self.ventana,text="1.-Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.-Borrar",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.-Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.-Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.-Regresar",command=self.main).pack(pady=5)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="\n...::: M E N U  P R I N C I P A L :::...").pack(pady=10)
        Button(self.ventana,text="1.- Coches", command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text="2.- Salir", command=self.ventana.quit).pack(pady=5)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="... Ingresar los datos del coche ...").pack(pady=10)
        Label(self.ventana, text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana, text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana, text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana, text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana, text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana, text="Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)
        Button(self.ventana,text="Guardar",command=self.insertar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar el ID del coche a Eliminar...").pack(pady=10)

        Label(self.ventana, text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.pack(pady=5)


        Button(self.ventana,text="Eliminar",command=self.eliminar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)


    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar el ID del coche a modificar...").pack(pady=10)
        
        Label(self.ventana, text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana, text="Nueva Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.pack(pady=5)

        Label(self.ventana, text="Nuevo Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana, text="Nuevo Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana, text="Nueva Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana, text="Nueva Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana, text="Nuevos Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        
        Button(self.ventana,text="Guardar",command=self.modificar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text=" ::: Consultar los coches :::").pack(pady=10)
        filas=""
        filas=self.consultar_controller(filas)
        Label(self.ventana,text=f"{'No.':<10}{'ID':<10}{'Marca':<15}{'Color':<15}{'Modelo':<15}{'Velocidad':<15}{'Potencia':<15}{'# Asientos':<15}").pack(pady=5)
        Label(self.ventana,text=f"-"*100).pack(pady=5)
        Label(self.ventana,text=f"{filas}").pack(pady=10)
        Label(self.ventana,text=f"-"*100).pack(pady=5)
        Button(ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)


    ## ...Controlador


    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...",message="...¡Accion Realizada con Exito!...")
        else:
            input("...¡Esta Accion no pudo realizarse en este momento !...")
            messagebox.showerror(title="...¡ Verifica por favor !...",message="...¡Esta Accion no pudo realizarse en este momento !...")

    def insertar_controller(self):
        coche1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1 

    def eliminar_controller(self):
        id=self.id.get()
        respuesta=coches.coches.eliminar(id)
        self.respuesta_sql(respuesta)

    def modificar_controller(self):
        id=self.id.get()
        coche1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1 

    def consultar_controller(self,filas):
        registros=coches.Coches.consultar()    
        num_coche=1
        if len(registros)>0:
            for fila in registros:
                filas=filas+f"\n{num_coche:<10}{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}"
                num_coche+=1
        else:
            filas="..¡No se encontraro informacion en la BD!"
        return filas



if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()