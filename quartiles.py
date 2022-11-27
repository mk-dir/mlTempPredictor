from statslib import calc_median

def quartile1(sample):

    median=calc_median(sample)[1]
    quartile_sample=sample[0:median+1]
    return quartile_sample