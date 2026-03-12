class Users():
    user_name = str
    email = str
    tel = str

    def __init__(self, user_name, email, tel):
        self.user_name = user_name
        self.email = email
        self.tel = tel

    def __str__(self):
        return f'User name: {self.user_name}\nEmail: {self.email}\nTel: {self.tel}'


    def autenticar(self):
        return "USuario no autenticado"
    


user1 = Users('Gerardo', 'gerardo@gmail.com', '123456789')
print( user1.autenticar())




#herencia
class Admin(Users):
    __is_admin = bool

    def __init__(self, is_admin, user_name, email, tel):
        super().__init__(user_name, email, tel)

        self.is_admin = is_admin

    
    def __str__(self):
        return super().__str__() +  f'Is admin : {self.is_admin}'


    def autenticar(self):
        return "USuario Autenticado"
    

userAdmin = Admin(True,'Enrique','enrique@gmail.com','234567890')
print(userAdmin.autenticar())


