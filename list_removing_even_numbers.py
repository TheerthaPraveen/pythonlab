list=[]
num=int(input("Enter the size of trhe list : "))
print("Enter the elements : ")
for i in range(0,num):
    list.append(int(input()))
print("the list elements are : ",list)
print("even numbers in list are : ")
for i in list:
    if(i%2==0):
        print (i)

