def decimalToHex(decimalValue):
    hexValue = hex(decimalValue)
    return hexValue

def toHexChar(hexValue):
    hexValue = hexValue.upper()
    hexValue = hexValue[2:]
    return hexValue

decimal = int(input("Enter a decimal number: "))
hexValue = decimalToHex(decimal)
hexString = toHexChar(hexValue)
print("The hex number is", hexString)
