from tkinter import Label, Entry,Button,messagebox, StringVar, Menu, Frame, ttk
from controllers.coches_controller import CochesController

class AppView:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0,0)
        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def barraMenu(self):
        #Menu de Opciones
        menuBar = Menu(self.ventana)
        self.ventana.config(menu=menuBar)

        menuPrincipal = Menu(menuBar , tearoff=False)
        menuBar.add_cascade(label="Principal" , menu=menuPrincipal)
        menuPrincipal.add_command(label="Menu Principal",command=self.main)
        menuPrincipal.add_command(label="Menu Acciones",command=self.menu_acciones)
        menuPrincipal.add_separator()
        menuPrincipal.add_command(label="Salir",command=self.ventana.quit)
                
        accionesMenu = Menu(menuBar , tearoff=False)
        menuBar.add_cascade(label="Acciones" , menu=accionesMenu)
        accionesMenu.add_command(label="Agregar",command=self.insertar_view )
        accionesMenu.add_command(label="Borrar",command=self.eliminar_view)
        accionesMenu.add_command(label="Modificar",command=self.modificar_view)
        accionesMenu.add_command(label="Mostrar",command=self.consultar_view)
        accionesMenu.add_separator()
        accionesMenu.add_command(label="Regresar",command=self.main)

    def menu_acciones(self):
            self.borrarPantalla()
            self.barraMenu()
            self.tipo = "Coches"
            Label(self.ventana, text= f"...::: Menu de {self.tipo} :::...").pack(pady=5)
            self.frame1=Frame(self.ventana)
            self.frame1.pack(pady=10)
            Button(self.frame1, text="Agregar", width=10,height=3, command=self.insertar_view).grid(row=0, column=0, pady=5, padx=5,sticky='e')
            Button(self.frame1, text="Borrar", width=10,height=3, command=self.eliminar_view).grid(row=0, column=1, pady=10,padx=5,sticky='w')
            Button(self.frame1, text="Modificar", width=10,height=3, command=self.modificar_view).grid(row=1, column=0, pady=10,padx=5,sticky='e')
            Button(self.frame1, text="Mostrar", width=10,height=3, command=self.consultar_view).grid(row=1, column=1, pady=10,padx=5,sticky='w')
            Button(self.frame1, text="Regresar", width=10,height=3, command=self.main).grid(row=2, column=0, columnspan=2,pady=5,padx=5)     

    def main(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana, text="\n...:: M E N U  P R I N C I P A L ::...").pack(pady=10)
        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=10)
        Button(self.frame1, text="Coches", width=10,height=3, command=self.menu_acciones).grid(row=0, column=0, pady=5, padx=5,sticky='e')
        Button(self.frame1, text="Salir", width=10,height=3, command=self.ventana.quit).grid(row=0, column=1, pady=10,padx=5,sticky='w')

    def insertar_view(self):
        self.borrarPantalla()
        self.barraMenu()

        Label(self.ventana, text="...Ingresar los datos del coche...").pack(pady=10)
        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=10)

        Label(self.frame1, text="Marca: ", anchor= 'e').grid(row=0, column=0, pady=5, padx=5, sticky='e')
        self.marca = Entry(self.frame1)
        self.marca.focus()
        self.marca .grid(row=0, column=1, pady=5, padx=5, sticky='w')
        Label(self.frame1, text="color: ").grid(row=1, column=0, pady=5, padx=5, sticky='e')
        self.color = Entry(self.frame1)
        self.color.grid(row=1, column=1, pady=5, padx=5, sticky='w')
        Label(self.frame1, text="modelo: ").grid(row=2, column=0, pady=5, padx=5, sticky='e')
        self.modelo = Entry(self.frame1)
        self.modelo.grid(row=2, column=1, pady=5, padx=5, sticky='w')
        Label(self.frame1, text="velocidad: ").grid(row=3, column=0, pady=5, padx=5, sticky='e')
        self.velocidad = Entry(self.frame1)
        self.velocidad.grid(row=3, column=1, pady=5, padx=5, sticky='w')
        Label(self.frame1, text="potencia: ").grid(row=4, column=0, pady=5, padx=5, sticky='e')
        self.potencia = Entry(self.frame1)
        self.potencia.grid(row=4, column=1, pady=5, padx=5, sticky='w')
        Label(self.frame1, text="asientos: ").grid(row=5, column=0, pady=5, padx=5, sticky='e')
        self.asientos = Entry(self.frame1)
        self.asientos.grid(row=5, column=1, pady=5, padx=5, sticky='w')
        Button(self.frame1, text="Guardar", command=lambda: {CochesController.insertar_controller(self), self.insertar_view()}).grid(row=6, column=0, pady=5, padx=5, sticky='e')
        Button(self.frame1, text= "Regresar", command=self.menu_acciones).grid(row=6, column=1, pady=5, padx=5, sticky='w')

    def eliminar_view(self):
        self.borrarPantalla()
        self.barraMenu()

        Label(self.ventana,text="...Ingresar el ID del coche a eliminar...").pack(pady=10)

        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)

        Label(self.frame1,text="ID:",anchor="e").grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.id = Entry(self.frame1)
        self.id.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.id.focus()

        self.btn_buscar = Button(self.frame1,text="Buscar",command=lambda: CochesController.buscar_controller(self, "Eliminar"))
        self.btn_buscar.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.btn_eliminar = Button(self.frame1,text="Eliminar",state="disabled",command=lambda: (CochesController.eliminar_controller(self),self.eliminar_view()))
        self.btn_eliminar.grid(row=2,column=1,padx=10,pady=10,sticky="e")

        Button(self.frame1,text="Regresar",command=self.menu_acciones).grid(row=2,column=1,padx=15,pady=10,sticky="w")

    def modificar_view(self):
        self.borrarPantalla()
        self.barraMenu()

        Label(self.ventana, text="...Ingresar el ID del coche a modificar...").pack(pady=10)

        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)

        Label(self.frame1, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.id = Entry(self.frame1)
        self.id.focus()
        self.id.grid(row=0, column=1, padx=5, pady=5)

        self.btn_buscar = Button(self.frame1, text="Buscar", command=lambda: CochesController.buscar_controller(self, "Modificar"))
        self.btn_buscar.grid(row=1, column=0, columnspan=5, padx=10, pady=5)

        self.var_marca= StringVar()
        self.var_color = StringVar()
        self.var_modelo = StringVar()
        self.var_velocidad= StringVar()
        self.var_potencia= StringVar()
        self.var_asientos= StringVar()

        self.frame2 = Frame(self.ventana)
        self.frame2.pack(pady=10)

        Label(self.frame2, text="Nueva Marca:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.marca = Entry(self.frame2, textvariable=self.var_marca)
        self.marca.grid(row=0, column=1, padx=5, pady=5)

        Label(self.frame2, text="Nuevo Color:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.color = Entry(self.frame2, textvariable=self.var_color)
        self.color.grid(row=1, column=1, padx=5, pady=5)

        Label(self.frame2, text="Nuevo Modelo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.modelo = Entry(self.frame2, textvariable=self.var_modelo)
        self.modelo.grid(row=2, column=1, padx=5, pady=5)

        Label(self.frame2, text="Nueva Velocidad:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.velocidad = Entry(self.frame2, textvariable=self.var_velocidad)
        self.velocidad.grid(row=3, column=1, padx=5, pady=5)

        Label(self.frame2, text="Nueva Potencia:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.potencia = Entry(self.frame2, textvariable=self.var_potencia)
        self.potencia.grid(row=4, column=1, padx=5, pady=5)

        Label(self.frame2, text="Nuevos Asientos:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.asientos = Entry(self.frame2, textvariable=self.var_asientos)
        self.asientos.grid(row=5, column=1, padx=5, pady=5)

        self.btn_modificar = Button(self.frame2,text="Modificar",state="disabled",command=lambda: (CochesController.modificar_controller(self), self.modificar_view()))
        self.btn_modificar.grid(row=6, column=0, padx=20, pady=15)

        Button(self.frame2,text="Regresar",command=self.menu_acciones).grid(row=6, column=1, padx=20, pady=15)

    def consultar_view(self):
        self.borrarPantalla()
        self.barraMenu()

        Label(self.ventana, text="...::Consultar los coches::...").pack(pady=10)
        #Tabla
        self.tree =ttk.Treeview(self.ventana, columns=("ID", "Marca", "Color", "Modelo","Velocidad","Potencia","Asientos"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Color", text="Color")
        self.tree.heading("Modelo", text="Modelo")
        self.tree.heading("Velocidad", text="Velocidad")
        self.tree.heading("Potencia", text="Potencia")
        self.tree.heading("Asientos", text="Asientos")
        self.tree.pack(fill="both", expand=False)

        #Colocar datos de la tabla
        CochesController.consultar_controller(self)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def cambiar_estado_btn(self, estado, tipo_accion):
        if estado and tipo_accion=="Eliminar":
            self.btn_eliminar.config(state="normal")
        elif estado and tipo_accion=="Modificar":
            self.btn_modificar.config(state="normal")
        elif estado and tipo_accion=="Eliminar":
            self.btn_eliminar.config(state="disabled")
        elif estado and tipo_accion=="Modificar":
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

    def encontrado(self,registro,tipo_accion):
        if len(registro)>0:            
            messagebox.showinfo(title="...El registro fue encontrado...",message=f"El registro fue encontrado con exito, se puede {tipo_accion}!...")
            self.cambiar_estado_btn(True, tipo_accion)
            #Nuevo
            if tipo_accion == "Modificar":
                self.var_marca.set(registro[0][1])
                self.var_color.set(registro[0][2])
                self.var_modelo.set(registro[0][3])
                self.var_velocidad.set(registro[0][4])
                self.var_potencia.set(registro[0][5])
                self.var_asientos.set(registro[0][6])               
        else:
            messagebox.showerror(title="... ¡ Verifica por favor ! ...", message=f"El registro no fue encontrado, no se puede {tipo_accion}!...")
            self.cambiar_estado_btn(False, tipo_accion)