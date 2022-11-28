# Calc_Median is a function
def calc_median(sample):
    # sort sample in ascending order
    sample.sort()
    median_index=0
    # Check if Sample Size is odd to do (n+1)/2
    if len(sample)%2==1:
        median_index=((len(sample)+1)/2)-1
        return sample[int(median_index)]

    # if sample size is even
    if len(sample)%2==0:
        median_value1=sample[int((len(sample)/2))-1] # n/2
        median_value2=sample[int((len(sample)+2)/2)-1] # (n+2)/2

        return (median_value1+median_value2)/2

