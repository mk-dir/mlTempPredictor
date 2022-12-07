def mean(sample):
    observations=len(sample)
    return sum(sample)/observations

def variance(sample):
    avg=mean(sample)
    sample.sort()
    devaitions_from_mean=[(each-avg)**2 for each in sample]
    variance=sum(devaitions_from_mean)/(len(sample)-1)


    import math
    # Standard Deviation
    SD=math.sqrt(variance)
    # Standard Error == SD/SQRT(n)
    stderr=SD/(math.sqrt(len(sample)))
    return {'STD DEV': SD, 'Variance':variance, 'Mean':avg,'SE':stderr}


from quartiles import all_quartiles
# sample=[70, 36, 43, 69, 82, 48, 34, 62, 35, 15,
# 59, 139, 46, 37, 42, 30, 55, 56, 36, 82,
# # 38, 89, 54, 25, 35, 24, 22, 9]
# sample=[70, 36, 43, 69, 82, 48, 34, 62, 35, 15,
# 59, 139, 46, 37, 42, 30, 55, 56, 36, 82,
# # 38, 89, 54, 25, 35, 24, 22, 9, 56, 19]
# print('VARIANCE ',['STD DEV'])
# print('STD DEV',variance(sample)['STD DEV'])
# print('MEAN',variance(sample)['Mean'])
# print('MEDIAN ',all_quartiles(sample)['Median'])
# print('Q1 ',all_quartiles(sample)['Q1'])
# print('Q3', all_quartiles(sample)['Q3'])
# print('Interquartile Range', all_quartiles(sample)['IQR'])
