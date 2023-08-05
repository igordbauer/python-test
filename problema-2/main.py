# calcula valor presente a partir de
# valor futuro
# taxa de juros
# data futura

import datetime as dt


def format_data(data):
    split_data = data.replace("-", "/").replace(".", "/").split("/")
    return dt.datetime(int(split_data[2]), int(split_data[1]), int(split_data[0]))


def duration_time(data_futura):
    formated_futura_data = format_data(data_futura)
    today = dt.datetime.now()
    duration = ((formated_futura_data - today).days) / 365

    return duration


def calcula_valor_presente(valor_futuro, taxa_juros, data_futura):
    valor_presente = valor_futuro / (
        (1 + (taxa_juros / 100)) ** duration_time(data_futura)
    )
    return valor_presente


valor_futuro = float(input("Insira o valor futuro:"))
taxa_juros = float(input("Insira a taxa de juros (em porcentagem): "))


data_futura_isValid = False

while data_futura_isValid == False:
    data_futura = input("Insira a data futura (dd/mm/aaaa): ")
    if duration_time(data_futura) > 0:
        data_futura_isValid = True
    else:
        print("Por favor insira uma data válida! (maior que o dia de hoje)")

valor_presente = calcula_valor_presente(valor_futuro, taxa_juros, data_futura)
MOI = (valor_futuro / valor_presente) - 1

print(f"Valor presente: {valor_presente:.2f}")
print(f"Margem sobre investimento de: {MOI:.2%}")
