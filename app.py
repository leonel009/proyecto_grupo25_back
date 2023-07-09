# Esta es la aplicacion de python

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
       
    def agregar_usuario(self, id_u, correo, nombre, contra ):
        x = Usuario(id_u, correo, nombre, contra)
        self.usuarios.append(x)

    def consular_usuario(self, id_u):
        for u in self.usuarios:
            if u.id_u == id_u:
                return u
            
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
           
    def eliminar_usuario(self, id_u):
        u = self.consular_usuario(id_u)
        if u.comprobar_admin():
            return False
        self.usuarios.remove(u)
        
            
    
misistema = Sistema()
    
    
        
