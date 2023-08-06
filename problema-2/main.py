from calculateFV import calculate_future_value_form
from calculatePV import calculate_present_value_form

choice_isValid = False

while choice_isValid == False:
    choice = str(
        input("Você deseja calcular Valor futuro [F] ou Valor Presente [P]? ")
    ).upper()
    if choice == "P":
        calculate_present_value_form()
    elif choice == "F":
        calculate_future_value_form()
    else:
        print("Por favor selecione uma opção válida!")
