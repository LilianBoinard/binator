class binary:
    def toDecimal(binaryNumberDefault):
        binaryNumber = tuple(int(c) for c in reversed(str(binaryNumberDefault)))
        decimalNumber = 0
        events = []
        for i in range(0, len(binaryNumber)):
            if binaryNumber[i] != 0:
                decimalNumber += 2**i
                events.append("ans + 2**" + str(i) + "=" + str(decimalNumber))
        events.append(str(binaryNumberDefault) + "=" + str(decimalNumber))
        return events
    
class decimal:
    def toBinary(decimalNumber):
        binaryNumber = []
        events = []
        while decimalNumber != 0:
            binaryNumber.append(decimalNumber % 2)
            decimalNumber = int(decimalNumber / 2)
            events.append((decimalNumber, "/2"))
        events.append(tuple(reversed(binaryNumber)))
        return events
class hexadecimal:
    def toDecimal(hexaNumberDefault):
        hexaNumber = tuple(str(c) for c in reversed(str(hexaNumberDefault)))
        decimalNumber = 0
        events = []
        for i in range(0, len(hexaNumber)):
            if hexaNumber[i] == 'A':
                decimalNumber += 10 * 16**i
                events.append((("10 * 16**", i, "=", decimalNumber)))
            elif hexaNumber[i] == 'B':
                decimalNumber += 11 * 16**i
                events.append((("11 * 16**", i, "=", decimalNumber)))
            elif hexaNumber[i] == 'C':
                decimalNumber += 12 * 16**i
                events.append((("12 * 16**", i, "=", decimalNumber)))
            elif hexaNumber[i] == 'D':
                decimalNumber += 13 * 16**i
                events.append((("13 * 16**", i, "=", decimalNumber)))
            elif hexaNumber[i] == 'E':
                decimalNumber += 14 * 16**i
                events.append((("14 * 16**", i, "=", decimalNumber)))
            elif hexaNumber[i] == 'F':
                decimalNumber += 15 * 16**i
                events.append((("15 * 16**", i, "=", decimalNumber)))
            else:
                decimalNumber += int(hexaNumber[i]) * 16**i
                events.append(((hexaNumber[i] + " * 16**", i, "=", decimalNumber)))
                
        events.append(((hexaNumberDefault, "=", decimalNumber)))
        return events
    
    def toBinary(hexaNumberDefault):
        hexaNumber = tuple(str(c) for c in reversed(str(hexaNumberDefault)))
        binaryNumber = []
        events = []
        for i in range(0, len(hexaNumber)):
            if hexaNumber[i] == 'A':
                binaryNumber.append("1010")
                events.append((("A =", binaryNumber[i])))
            elif hexaNumber[i] == 'B':
                binaryNumber.append("1011")
                events.append((("B =", binaryNumber[i])))
            elif hexaNumber[i] == 'C':
                binaryNumber.append("1100")
                events.append((("C =", binaryNumber[i])))
            elif hexaNumber[i] == 'D':
                binaryNumber.append("1101")
                events.append((("D =", binaryNumber[i])))
            elif hexaNumber[i] == 'E':
                binaryNumber.append("1110")
                events.append((("E =", binaryNumber[i])))
            elif hexaNumber[i] == 'F':
                binaryNumber.append("1111")
                events.append((("F =", binaryNumber[i])))
            else:
                binaryNumber.append(((0, decimal.toBinary(int(hexaNumber[i])))))
                events.append(((hexaNumber[i], "=", binaryNumber[i])))
                
        events.append(((hexaNumberDefault, "=", list(reversed(binaryNumber)))))
        return events
        
def displayEvents(events):
    for i in range(0, len(events) - 1):
        print(events[i])
    print("result: ", events[-1])
                
    
def main():

    choice = int(input("Operation: "))
    if choice == 1:
        events = binary.toDecimal(str(input("Binary number: ")))
        displayEvents(events)
        main()
    elif choice == 2:
        events = decimal.toBinary(int(input("Decimal number: ")))
        displayEvents(events)
        main()
    elif choice == 3:
        events = hexadecimal.toDecimal(str(input("Hexadecimal number: ")))
        displayEvents(events)
        main()
    elif choice == 4:
        events = hexadecimal.toBinary(str(input("Hexadecimal number: ")))
        displayEvents(events)
        main()
    else:
        print("this operation does not exist")
        main()
    
main()

