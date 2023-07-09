# Esta es la aplicacion de python

import sqlite3
con = sqlite3.connect('sistema.db')
cur = con.cursor()

class Usuario():
    def __init__(self, correo, nombre, contra, id_usuario):
        self.correo
        self.nombre=nombre
        self.contra=contra
        self.id_usuario=id_usuario
    
class Sistema():
    usuarios = []
    
    def iniciar_usuarios():
        
        
        cur.execute('''CREATE TABLE usuarios (
                       id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                       correo varchar(255),
                       nombre varchar(255) NOT NULL,
                       contra varchar(255) NOT NULL''')
        
    def agregar_usuario(self, usuario):
        cur.execute(f"INSERT INTO usuarios VALUES ('{usuario.id_usuario}','{usuario.correo}','{usuario.nombre}','{usuario.contra}')")
        

    
    
    
        