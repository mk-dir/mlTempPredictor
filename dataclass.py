from median import calc_median
from quartiles import all_quartiles
from variance import variance

class data:
    def __init__(self,sample):
        datadic=all_quartiles(sample)
        self.median=datadic['Median']
        self.Q1=datadic['Q1']
        self.Q3=datadic['Q3']
        self.IQR=datadic['IQR']

        datadic=variance(sample)
        self.std_dev=datadic['STD DEV']
        self.variance=datadic['Variance']
        self.mean=datadic['Mean']
        self.stderr=datadic['SE']

    def __repr__(self) -> str:
        return 'Mean: {} \n Median: {}\n Q1: {}\n Q3: {}\n IQR: {}\n STD DEVIATION: {}\n Variance: {}\n Standard Error: {}'.format(self.mean,self.median,self.Q1,self.Q3,self.IQR,self.std_dev,self.variance,self.stderr)