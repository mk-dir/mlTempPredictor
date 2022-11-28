from median import calc_median

def all_quartiles(sample):
    median=median=calc_median(sample)
    #Between First Datapoint and Median
    Q0Q2=[each for each in sample if each<=median]
    Q2Q4=[each for each in sample if each>=median]

    # Calculate Q1 & Q3
    Q1=calc_median(Q0Q2)
    Q3=calc_median(Q2Q4)
    #Between Q0 and Q1
    Q0Q1=[each for each in Q0Q2 if each<=Q1]
    #Between Q1 and Q2
    Q1Q2=[each for each in Q0Q2 if each>=Q1]
    #Between Q2 and Q3
    Q2Q3=[each for each in Q2Q4 if each>=median and each <=Q3]
    #Between Q3 and Q4
    Q3Q4=[each for each in Q2Q4 if each>=Q3]

    return {'Median':median,'Q1':Q1,'Q3':Q3,'Q0Q1':Q0Q1,'Q1Q2':Q1Q2,'Q2Q3':Q2Q3,'Q3Q4':Q3Q4}

    


# Rebuild this Function as a class

# def quartile1(sample):

#     median=calc_median(sample)[1]

#     # quartile_sample=sample[0:median+1]
#     return median

sample=[70, 36, 43, 69, 82, 48, 34, 62, 35, 15,
59, 139, 46, 37, 42, 30, 55, 56, 36, 82,
38, 89, 54, 25, 35, 24, 22, 9, 56, 19,23,23]

print(len(sample))
sample.sort()
print(sample)

print('Median',all_quartiles(sample)['Median'])
print('Q1',all_quartiles(sample)['Q1'])
print('Q3',all_quartiles(sample)['Q3'])
print('Q0--->Q1',all_quartiles(sample)['Q0Q1'])
print('Q1--->Q2',all_quartiles(sample)['Q1Q2'])
print('Q2--->Q3',all_quartiles(sample)['Q2Q3'])
print('Q3--->Q4',all_quartiles(sample)['Q3Q4'])