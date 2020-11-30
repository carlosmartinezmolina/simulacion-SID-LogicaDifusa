from Fuzzification import *
from Defusification import *
from aggregation import *

def linguisticVariables():
    performance = VariableLinguistica('Performance',(0,100))
    def lp(i):
        if i < 50:
            return 1
        if i >= 50 and i < 70:
            return((-1/20)*i + 7/2)
        if i >= 70:
            return(0)

    def mp(i):
        if i < 60 or i >= 80:
            return(0)
        if i >= 60 and i < 65:
            return(i/5 - 12)
        if i >= 65 and i < 75:
            return(1)
        if i >= 75 and i < 80:
            return((-1/5)*i + 16)

    def hp(i):
        if i < 70:
            return(0)
        if i >= 70 and i < 85:
            return(i/15 - 14/3)
        if i >= 85:
            return(1)
    
    low = FuzzySet('low')
    low.setTriangularFunction(0,10,60)
    mid = FuzzySet('mid')
    mid.setTriangularFunction(40,60,80)
    high = FuzzySet('high')
    high.setTriangularFunction(60,90,100)
    performance.addSet(low)
    performance.addSet(mid)
    performance.addSet(high)

    shape = VariableLinguistica('Shape',(0,100))

    def bs(i):
        if i < 40:
            return(-1*i/40 + 1)
        if i >= 40:
            return(0)
        # Regular
    
    def rs(i):
        if i < 30 or i >= 70:
            return(0)
        if i >= 30 and i < 50:
            return(i/20 - 3/2)
        if i >= 50 and i < 70:
            return(-1*i/20 + 7/2)
        # Good
    
    def gs(i):
        if i < 60:
            return(0)
        if i >= 60:
            return(i/40 - 3/2)

    bad = FuzzySet('bad')
    bad.setTriangularFunction(0,20,60)
    regular = FuzzySet('regular')
    regular.setTriangularFunction(40,60,80)
    good = FuzzySet('good')
    good.setTriangularFunction(60,85,100)

    shape.addSet(bad)
    shape.addSet(regular)
    shape.addSet(good)

    probabilidadJugabilidad = VariableLinguistica('Jugabilidad',(0,10))

    def altaProbJugar(i):
        if i < 4:
            return 0
        if i >= 8:
            return 1
        return (i - 4) / 7

    def bajaProbJugar(i):
        if i > 7:
            return 0
        if i < 2:
            return 1
        return (7 - i) / 7

    alta = FuzzySet('altaProb')
    alta.setTriangularFunction(5,8,10)
    baja = FuzzySet('bajaProb')
    baja.setTriangularFunction(0,2,5)

    probabilidadJugabilidad.addSet(alta)
    probabilidadJugabilidad.addSet(baja)

    return performance, shape, probabilidadJugabilidad

def fuzzyRules(performance,shape,jugabilidad):
    fr1 = FuzzyRule()
    fr1.addAntecedent(performance.getSet('low'),performance,'and')
    fr1.addAntecedent(shape.getSet('regular'),shape,'.')
    fr1.addConsecuent(jugabilidad.getSet('bajaProb'),jugabilidad,'.')

    fr2 = FuzzyRule()
    fr2.addAntecedent(performance.getSet('mid'),performance,'and')
    fr2.addAntecedent(shape.getSet('good'),shape,'.')
    fr2.addConsecuent(jugabilidad.getSet('altaProb'),jugabilidad,'.')

    fr3 = FuzzyRule()
    fr3.addAntecedent(performance.getSet('mid'),performance,'and')
    fr3.addAntecedent(shape.getSet('regular'),shape,'.')
    fr3.addConsecuent(jugabilidad.getSet('bajaProb'),jugabilidad,'.')

    fr4 = FuzzyRule()
    fr4.addAntecedent(performance.getSet('high'),performance,'and')
    fr4.addAntecedent(shape.getSet('bad'),shape,'.')
    fr4.addConsecuent(jugabilidad.getSet('altaProb'),jugabilidad,'.')

    fr5 = FuzzyRule()
    fr5.addAntecedent(performance.getSet('high'),performance,'or')
    fr5.addAntecedent(shape.getSet('good'),shape,'.')
    fr5.addConsecuent(jugabilidad.getSet('altaProb'),jugabilidad,'.')

    fr6 = FuzzyRule()
    fr6.addAntecedent(performance.getSet('high'),performance,'and')
    fr6.addAntecedent(shape.getSet('regular'),shape,'.')
    fr6.addConsecuent(jugabilidad.getSet('altaProb'),jugabilidad,'.')

    fr7 = FuzzyRule()
    fr7.addAntecedent(performance.getSet('mid'),performance,'and')
    fr7.addAntecedent(shape.getSet('good'),shape,'.')
    fr7.addConsecuent(jugabilidad.getSet('altaProb'),jugabilidad,'.')


    

    return [fr1,fr2,fr3,fr4,fr5,fr6,fr7]

def jugador1(jugador_values,defFun):
    print('Probando el jugador con un performance de ' + str(jugador_values['Performance']) + ' y forma fisica de ' + str(jugador_values['Shape']))
    p,s,j = linguisticVariables()
    listRules = fuzzyRules(p,s,j)
    fuzzySet = mamdani(jugador_values,listRules)
    print('Probabilidad de jugar: ')
    print(defFun(j,fuzzySet,0.1))

def jugador2(jugador_values,defFun):
    print('Probando el jugador con un performance de ' + str(jugador_values['Performance']) + ' y forma fisica de ' + str(jugador_values['Shape']))
    p,s,j = linguisticVariables()
    listRules = fuzzyRules(p,s,j)
    fuzzySet = larsen(jugador_values,listRules)
    print('Probabilidad de jugar: ')
    print(defFun(j,fuzzySet,0.1))

def main():
    jugador_values = {'Performance' : 50, 'Shape' : 80}
    print('Mamdani con Centroid')
    jugador1(jugador_values,centroid)
    print('Mamdani con Mean of Max')
    jugador1(jugador_values,mean_of_maxim)
    print('Mamdani con Biseccion')
    jugador1(jugador_values,bisection)
    print()

    jugador_values = {'Performance' : 10, 'Shape' : 90}
    print('Larsen con Centroid')
    jugador2(jugador_values,centroid)
    print('Larsen con Mean of Max')
    jugador2(jugador_values,mean_of_maxim)
    print('Larsen con Biseccion')
    jugador2(jugador_values,bisection)
    print()

    jugador_values = {'Performance' : 75, 'Shape' : 20}
    print('Mamdani con Centroid')
    jugador1(jugador_values,centroid)
    print('Mamdani con Mean of Max')
    jugador1(jugador_values,mean_of_maxim)
    print('Mamdani con Biseccion')
    jugador1(jugador_values,bisection)
    print()

    jugador_values = {'Performance' : 50, 'Shape' : 55}
    print('Larsen con Centroid')
    jugador2(jugador_values,centroid)
    print('Larsen con Mean of Max')
    jugador2(jugador_values,mean_of_maxim)
    print('Larsen con Biseccion')
    jugador2(jugador_values,bisection)
    print()

    jugador_values = {'Performance' : 20, 'Shape' : 30}
    print('Mamdani con Centroid')
    jugador1(jugador_values,centroid)
    print('Mamdani con Mean of Max')
    jugador1(jugador_values,mean_of_maxim)
    print('Mamdani con Biseccion')
    jugador1(jugador_values,bisection)
    print()
    
    jugador_values = {'Performance' : 90, 'Shape' : 80}
    print('Larsen con Centroid')
    jugador2(jugador_values,centroid)
    print('Larsen con Mean of Max')
    jugador2(jugador_values,mean_of_maxim)
    print('Larsen con Biseccion')
    jugador2(jugador_values,bisection)
     

main()