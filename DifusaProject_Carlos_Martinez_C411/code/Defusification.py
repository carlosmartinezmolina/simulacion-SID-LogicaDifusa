

def centroid(outputLinguisticVaraible,fuzzySet, epsilon):
    domain = outputLinguisticVaraible.domain
    
    i = domain[0]
    sum_numerator = 0
    sum_denominator = 0
    
    while i <= domain[1]:
        sum_numerator += i*fuzzySet(i)
        sum_denominator += fuzzySet(i)
        i += epsilon
    if sum_denominator == 0:
        return 0
    return sum_numerator / sum_denominator



def mean_of_maxim(outputLinguisticVaraible,fuzzySet, epsilon):
    domain = outputLinguisticVaraible.domain
    i = domain[0]
    l = []
    my_max = -1
    while i <= domain[1]:
        temp = fuzzySet(i)
        if my_max < temp:
            my_max = temp
            l = [i]
        if my_max == temp:
            l.append(i)
        i += epsilon
    my_sum = 0
    for i in l:
        my_sum += i
    return my_sum / len(l)


def bisection(outputLinguisticVaraible,fuzzySet, epsilon):
    domain = outputLinguisticVaraible.domain

    i = domain[0]
    area_total = 0
    while i <= domain[1]:
        area_total += fuzzySet(i)
        i += epsilon
    temp_area = 0
    best_area = 0
    diference = area_total
    i = 0
    while i <= domain[1]:
        temp_area += fuzzySet(i)
        if abs(temp_area - (area_total - temp_area)) < diference:
            diference = abs(temp_area - (area_total - temp_area))
            best_area = i
        i += epsilon

    return best_area