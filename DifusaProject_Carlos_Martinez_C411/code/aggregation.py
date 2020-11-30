def fmax(fun1, fun2):
    def wrapper(v):
        return max(fun1(v), fun2(v))
    return wrapper

def fmul(value, function):
    def wrapper(x):
        return value * function(x)
    return wrapper

def fmin(value, function):
    def wrapper(x):
        return min(value, function(x))
    return wrapper

def mamdani(values,fuzzyRuleList):
    implication_function = []
    for i in fuzzyRuleList:
        antecedente_alfa = i.eval_antecedet(values)
        fun = i.eval_consecuent()
        implication_function.append(fmin(antecedente_alfa,fun))
    if len(implication_function) > 0:
        result_function = implication_function[0]
        for i in range(1,len(implication_function)):
            result_function = fmax(result_function,implication_function[i])
    return result_function


def larsen(values,fuzzyRuleList):
    implication_function = []
    for i in fuzzyRuleList:
        antecedente_alfa = i.eval_antecedet(values)
        fun = i.eval_consecuent()
        implication_function.append(fmul(antecedente_alfa,fun) )
    if len(implication_function) > 0:
        result_function = implication_function[0]
        for i in range(1,len(implication_function)):
            result_function = fmax(result_function,implication_function[i])
    return result_function

