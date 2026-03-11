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
    
user1 = Users('Gerardo', 'gerardo@gmail.com', '123456789')

def sumar():
    return 2 + 1

print(sumar())
