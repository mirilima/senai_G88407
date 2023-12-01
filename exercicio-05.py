usuarios ={
    'usuario1': 'usuario1',
    'usuario2': 'usuario22',
    'usuario3': 'usuario33'
    }
usuario = input("insira seu usuario:\n")
senha = input("insira sua senha:\n")

if usuarios in usuarios and usuarios[usuario] == senha:
    print(usuario)
else:
    print("usuario não existe")  
