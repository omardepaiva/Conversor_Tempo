#Quantidade de tempo em segundos
tempo_total = int(input())

#Calculo de Horas. minutos e segundos

quantidade_segundos = [3600,60,1] # 1 hora - 3600 segundos/ 1 minuto - 60 segundos
resultado = []

for alvo in quantidade_segundos:
    quantidade = int(tempo_total / alvo)
    resultado.append(str(quantidade))
    tempo_total -= quantidade * alvo

#iprimir o resultado
print(":" .join(resultado))