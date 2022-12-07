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

    # InterQuartile Range IQR
    IQR=Q3-Q1

    return {'Median':median,'Q1':Q1,'Q3':Q3,'Q0Q1':Q0Q1,'Q1Q2':Q1Q2,'Q2Q3':Q2Q3,'Q3Q4':Q3Q4,'IQR':IQR}