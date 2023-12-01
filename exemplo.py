from traceback import print_tb


for i in range (5):
    print(i)

    notas =[90,85,78,92,88,76,95,89]#nota dos alunos
    soma=0
    for nota in notas:
        soma+=nota

        media = soma/len(notas)
        print("a media é:",media)