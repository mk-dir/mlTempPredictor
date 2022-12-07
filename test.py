from dataclass import data

sample=[70, 36, 43, 69, 82, 48, 34, 62, 35, 15,
59, 139, 46, 37, 42, 30, 55, 56, 36, 82,
38, 89, 54, 25, 35, 24, 22, 9, 56, 19]

sample2=[53, 21, 32, 49, 45, 38, 44, 33, 32, 43, 53, 46, 36, 48, 39, 35, 37, 36, 39, 45]

data_obj=data(sample)
data_obj2=data(sample2)

print(data_obj)
print(data_obj2)
