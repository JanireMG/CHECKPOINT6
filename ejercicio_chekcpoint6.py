"""
Cree una clase de Python llamada Usuario que use el método init y cree
un nombre de usuario y una contraseña. Crea un objeto usando la clase.
Esta es toda la asignación, ¡mucha suerte!
"""

class Usuario:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def my_user(self):
        print(f'My username is= "{self.user_name}" and my password is= "{self.password}".')

    

log = Usuario ('Janire', 'micontraseña')
log.my_user()

