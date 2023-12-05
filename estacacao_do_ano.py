#estação de ano
def estacao_ano_refinada(mes, dia):
    if (mes == 3 and dia >= 20) or (mes == 4 or mes == 5) or (mes == 6 and dia < 21):
        return "Outono"
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia < 23):
        return "Inverno"
    elif (mes == 9 and dia >= 23) or (mes == 10 or mes == 11) or (mes == 12 and dia < 21):
        return "Primavera"
    else:
        return "Verão"

#Resultados
mes_usuario = int(input("Digite o número do mês (1 a 12): "))
dia_usuario = int(input("Digite o número do dia (1 a 31): "))
print("Estação do ano (versão refinada):", estacao_ano_refinada(mes_usuario, dia_usuario))
