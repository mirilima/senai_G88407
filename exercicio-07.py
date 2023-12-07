import pandas as PD
dados ={
    "nome":["maria","paulo","joão","rafa"],
    "idade":[30,20,29,23],
    "cidade":[ "camaçari","são paulo","santo andré", "são caetano do sul"]
}
df = PD.DataFrame(dados)
for dado in df.values:
      print(dado[0],dado[1])

