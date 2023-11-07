users = [] # Banco para guardar os usuários quando cadastrados.

def addUser(name, user, password):
    user = {
        'name' : name,
        'user' : user,
        'password' : password,
        'status' : 0, # 0 = False | 1 = True
        'isBanned': 0, # 0 = False | 1 = True
        'isVerify' : 0, # 0 = False | 1 = True
        'posts' : [],
        'friends' : []
    }

    for user in users:
        if user['name'] == name and user['user'] == user:
            print(f"Usuário {user['user']} já existe, escolha outro!")
            return False
        else:
            if len(user['user']) > 6 and len(user['password']) >= 6:
                users.append(user)
                print("Usuário cadastrado com sucesso!")
            else:
                print("Usuário e senha tem que ter pelo menos 6 caractéres!")
                return False
        return True
    
def login(user, password):
    for user in users:
        if user['user'] == user and user['password'] == password:
            print(f"Seja bem vindo {user['name']}")
        elif user['user'] != user and user['password'] == password:
            print(f"Usuário {user['user']} não encontrado.")
        else:
            print("Usuário ou senha incorreto")
            return False
    return True