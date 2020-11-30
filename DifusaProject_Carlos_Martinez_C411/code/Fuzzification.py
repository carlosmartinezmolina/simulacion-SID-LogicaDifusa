

class VariableLinguistica:
    def __init__(self,name,domain):
        self.name = name
        self.domain = domain
        self.fuzzySet = []

    def addSet(self,_fuzzySet):
        self.fuzzySet.append(_fuzzySet)
    
    def getSet(self,name):
        for i in self.fuzzySet:
            if i.name == name:
                return i
        return None

class FuzzySet:
    def __init__(self,name):
        self.name = name
        self.membershipFunction = None
    
    def evalMembershipFunction(self,value):
        return self.membershipFunction(value)

    def funMembresiaTriangular(self,minVal,midVal,maxVal,x):
        if x < minVal:
            return 0
        elif x >= minVal and x <= midVal:
            if midVal == minVal:
                return x - minVal
            return (x - minVal)/(midVal - minVal)
        elif x >= midVal and x <= maxVal:
            if maxVal == midVal:
                return maxVal - x
            return (maxVal - x)/(maxVal - midVal)
        else:
            return 0

    def setTriangularFunction(self,a,b,c):
        self.membershipFunction = lambda x : self.funMembresiaTriangular(a,b,c,x)

    def setTrapezoidalFunction(self,a,b,c,d):
        self.membershipFunction = lambda x : self.funMembresiaTrapezoidal(a,b,c,d,x)

    def funMembresiaTrapezoidal(self,minVal,midVal1,midVal2,maxVal,x):
        if x < minVal:
            return 0
        elif x >= minVal and x <= midVal1:
            if midVal1 == minVal:
                return x - minVal
            return (x - minVal)/(midVal1 - minVal)
        elif x >= midVal1 and x <= midVal2:
            return 1
        elif x >= midVal2 and x <= maxVal:
            return (maxVal - x)/maxVal
        else:
            return 0

class FuzzyRule:
    def __init__(self):
        self.antecedent = []
        self.consecuent = []
        self.linguisticVariableName = None
    # operation es un string que indica la operacion que va a realizar
    # con el que viene atras, es un . si es el ultimo miembro
    def addAntecedent(self,fuzzySet,variableLinguistica,operation):
        self.antecedent.append((fuzzySet,variableLinguistica,operation))

    def addConsecuent(self,fuzzySet,variableLinguistica,operation):
        self.linguisticVariableName = variableLinguistica.name
        self.consecuent.append((fuzzySet,variableLinguistica,operation))

    def eval_consecuent(self):
        return lambda x : self.consecuent[0][0].membershipFunction(x)

    # value es un diccionario de VariableLinguistica : valor
    def eval_antecedet(self,values):
        x = self.antecedent[0]
        result = x[0].membershipFunction(values[x[1].name])
        for i in range(1,len(self.antecedent)):
            item = self.antecedent[i]
            if self.antecedent[i-1][2] == 'and':
                result = min(result, item[0].membershipFunction(values[item[1].name]))
            elif self.antecedent[i-1][2] == 'or':
                result = max(result, item[0].membershipFunction(values[item[1].name]))
        return result
            
