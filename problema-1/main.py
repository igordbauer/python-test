def formatNumber(value, separator, counter):
    return value.replace(f"{counter}", separator).replace("_", f"{counter}")


class MonetaryValue:
    def __init__(self, int_value, coin_type, separator):  # constructor
        self.int_value = int_value
        self.coin_type = coin_type
        self.separator = separator[0]

    def valorFloat(self):
        return float(self.int_value)

    def finalValue(self, coin_type, separator):
        counter = ","
        if separator == ",":
            counter = "."
        value = f"{self.valorFloat():_.2f}"
        finalNumber = f"{coin_type} {formatNumber(value,separator,counter)}"
        return finalNumber


int_value = input("Insira um valor:")
coin_type_isValid = False

while coin_type_isValid == False:
    coin_type = str(input("Insira uma unidade monetária: [R$ ou $]: "))
    if coin_type == "R$" or coin_type == "$":
        coin_type_isValid = True
    else:
        print("Insira uma unidade monetária válida")

separator_isValid = False
while separator_isValid == False:
    separator = str(input("Insira um separador: "))
    if separator == "," or separator == ".":
        separator_isValid = True
    else:
        print("Insira um separador válido")


object = MonetaryValue(int_value, coin_type, separator)

print(object.finalValue("R$", "."))
print(object.finalValue("R$", ","))
print(object.finalValue("$", "."))
print(object.finalValue("$", ","))
