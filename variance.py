def mean(sample):
    observations=len(sample)
    return sum(sample)/observations

def variance(sample):
    avg=mean(sample)
    sample.sort()
    devaitions_from_mean=[(each-avg)**2 for each in sample]
    variance=sum(devaitions_from_mean)/(len(sample)-1)

    import math
    SD=math.sqrt(variance)
    return {'STD DEV': SD, 'Variance':variance}


sample=[70, 36, 43, 69, 82, 48, 34, 62, 35, 15,
59, 139, 46, 37, 42, 30, 55, 56, 36, 82,
38, 89, 54, 25, 35, 24, 22, 9,]

print(variance(sample))
    