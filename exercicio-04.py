distancia= float(input("digite a distancia:\n"))
veiculo = input("digite o veiculo (obs: carro, moto ou bicicleta)\n").upper()

def calculo_custo_viagem(veiculo,distancia):
    if veiculo == "CARRO":
        km = 0.50
    elif veiculo == "MOTO":
        km = 0.20 
    elif veiculo == "BICICLETA": 
        km = 0.10
    else:   
        print("tipo de veiculo invalido")
        return None

    custo_total = distancia*km
    return custo_total

custo = calculo_custo_viagem(veiculo ,distancia)
if custo != None:
    print("o custo total da viagem é:{:.2f}".format(custo))





