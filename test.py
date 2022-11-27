# Data Structure
list1= [70, 36, 43, 69, 82, 48, 34, 62, 35, 15,
59, 139, 46, 37, 42, 30, 55, 56, 36, 82,
38, 89, 54, 25, 35, 24, 22, 9, 56, 19]

list2=[]
while True:
    counter=0
    while counter < len(list1):
        if counter==len(list1)-1:
            break
        elif list1[counter]>list1[counter+1]:
            swap=list1[counter+1]
            list1[counter+1]=list1[counter]
            list1[counter]=swap
            counter+=1
        else: 
            counter+=1
            continue

print(list1)
