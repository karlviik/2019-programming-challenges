from sys import stdin

count = 0
for line in stdin:
    if count == 0:
        base = int(line)
        count += 1
    elif count == 1:
        stepper = int(line)
        count += 1
    elif count == 2:
        modder = int(line)
        count += 1

        if base % modder == 0 or modder == 1:
            print("0")
            continue
        if stepper == 0:
            print("1")
            continue

        modulosToCalculate = []

        moduloSample = 1
        stepperTemp = stepper
        while stepperTemp > 0:
            if moduloSample * 2 <= stepperTemp:
                moduloSample = moduloSample * 2
            elif moduloSample == stepperTemp:
                modulosToCalculate.append(moduloSample)
                stepperTemp -= moduloSample
            else:
                stepperTemp -= moduloSample
                modulosToCalculate.append(moduloSample)
                moduloSample = 1

        remainder = 1
        currentlyCalcingModulo = 1
        currentlyCalcModRemainder = base % modder

        while len(modulosToCalculate) > 0:
            if modulosToCalculate[-1] == currentlyCalcingModulo:
                remainder = remainder * currentlyCalcModRemainder % modder
                modulosToCalculate.pop(-1)
            currentlyCalcingModulo = currentlyCalcingModulo * 2
            currentlyCalcModRemainder = currentlyCalcModRemainder ** 2 % modder

        print(remainder)
    elif count == 3:
        count = 0
        continue
