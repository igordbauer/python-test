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
