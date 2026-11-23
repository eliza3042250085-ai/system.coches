import mysql.connector
from tkinter import messagebox

try:
    conexion= mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_coches'
        
    )
    cursor=conexion.cursor(buffered=True)
except:
    messagebox.showerror(title="Error de conexión", message="Por el momento no se pudo conectar a la base de datos. Intente más tarde")
    
