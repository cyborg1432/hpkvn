def arithmetic_arranger(array):
    for exp in array:
        opPos = exp.index("+") or exp.index("-")
        print(exp[:opPos].strip() + "\n" + exp[opPos + 1:].strip())











# arithmetic_arranger(["32 + 698"])

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])