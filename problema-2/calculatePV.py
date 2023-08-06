import datetime as dt


def date_format(date):
    split_date = date.replace(",", "/").replace("-", "/").replace(".", "/").split("/")
    return dt.datetime(int(split_date[2]), int(split_date[1]), int(split_date[0]))


def duration_time(future_date):
    formated_futura_date = date_format(future_date)
    today = dt.datetime.now()
    duration = ((formated_futura_date - today).days) / 365

    return duration


def calculate_present_value(future_value, interest_rate, future_date):
    present_value = future_value / (
        (1 + (interest_rate / 100)) ** duration_time(future_date)
    )
    return present_value


def calculate_present_value_form():
    future_value = float(input("Insira o valor futuro:").replace(",", "."))
    interest_rate = float(
        input("Insira a taxa de juros (em porcentagem): ").replace(",", ".")
    )

    future_date_isValid = False

    while future_date_isValid == False:
        future_date = input("Insira a data futura (dd/mm/aaaa): ")

        if len(future_date.strip()) != 10:
            print("Por favor insira a data em um formato válido!")
        else:
            if duration_time(future_date) > 0:
                future_date_isValid = True
            else:
                print("Por favor insira uma data válida! (maior que o dia de hoje)")

    present_value = calculate_present_value(future_value, interest_rate, future_date)
    MOI = (future_value / present_value) - 1

    print(f"Valor presente: {present_value:.2f}")
    print(f"Margem sobre investimento de: {MOI:.2%}")
