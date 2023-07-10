# Esta es la aplicacion de python
import sqlite3
from sqlite3 import Error

# Configurar la conexión a la base de datos SQLite
DATABASE = 'sistema.db'

# Obtener la conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    # Crear la tabla 'Usuarios' si no existe
    
    conn = None
#    try:
    conn = get_db_connection()
    print(sqlite3.version)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        id_u INTEGER PRIMARY KEY,
        correo TEXT NOT NULL,
        nombre TEXT NOT NULL,
        contra TEXT NOT NULL)''')
    conn.commit()
    cursor.close()
    conn.close()
#    except Error as e:
#    print(e)
#    finally:
#    if conn:
#        conn.close()
    
    
    
    
    

def create_database():
    # Verificar si la base de datos existe, si no, crearla y crear la tabla
    conn = sqlite3.connect(DATABASE)
    conn.close()
    create_table()

# Crear la base de datos y la tabla si no existen
create_database()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Clases relevantes
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Usuario():
    
    admins=[]
    
    def __init__(self, id_u, correo, nombre, contra ):
        self.id_u=id_u
        self.correo=correo
        self.nombre=nombre
        self.contra=contra
        
    
    def comprobar_admin(self):
        if self.id_u in Usuario.admins:
            return True
    
    def promover_a_admin(self):
        Usuario.admin.append(self.id_u)
        
    def modificar_usuario(self, n_correo, n_nombre, n_contra):
        self.correo=n_correo
        self.nombre=n_nombre
        self.contra=n_contra
    
    
    
class Sistema():
    
    
    def __init__(self):
        self.usuarios = []
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()
        
       
    def agregar_usuario(self, id_u, correo, nombre, contra ):
        
        usuario_existente = self.consultar_usuario(id_u)
        if usuario_existente:
            print("Ya existe un usuario con ese id.")
            return False

        #nuevo_usuario = Producto(codigo, descripcion, cantidad, precio)
        self.cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?)", (id_u, correo, nombre, contra))
        self.conexion.commit()
        return True

    def consultar_usuario(self, id_u):
        self.cursor.execute("SELECT * FROM usuarios WHERE id_u = ?", (id_u,))
        row = self.cursor.fetchone()
        if row:
            id_u, correo, nombre, contra = row
            return Usuario(id_u, correo, nombre, contra)
        return False
            
    def obtener_id_de_usuario(self, correo="", nombre =""):
        if correo != "":
            for u in self.usuarios:
                if u.correo == correo:
                    return u
        if nombre != "":       
            for u in self.usuarios:
                if u.correo == correo:
                    return u
        
    
    def modificar_usuario(self, id_u, n_correo, n_nombre, n_contra):
        u = self.consular_usuario(id_u)
        if u:
           u.modificar_usuario(n_correo, n_nombre, n_contra)
           
        u = self.consultar_usuario(id_u)
        if u:
            u.modificar(n_correo, n_nombre, n_contra)
            self.cursor.execute("UPDATE usuarios SET correo = ?, nombre = ?, contra = ? WHERE id_u = ?",
                                (n_correo, n_nombre, n_contra, id_u))
            self.conexion.commit()
            
    def listar_usuarios(self):
        print("-" * 30)
        self.cursor.execute("SELECT * FROM usuarios")
        rows = self.cursor.fetchall()
        for row in rows:
            id_u, correo, nombre, contra = row
            print(f"Código: {id_u}")
            print(f"correo: {correo}")
            print(f"nombre: {nombre}")
            print("-" * 30)
           
    def eliminar_usuario(self, id_u):
        self.cursor.execute("DELETE FROM usuarios WHERE id_u = ?", (id_u,))
        if self.cursor.rowcount > 0:
            print("Usuario eliminado.")
            self.conexion.commit()
        else:
            print("Usuario no encontrado.")
        
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
misistema = Sistema()
misistema.listar_usuarios()
        
