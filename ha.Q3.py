

# def sum_number():
#     a=[1, 2, 3, [4 , 5, 6], 7, [8 ,9 ]]
#     i=1
#     sum=0
#     while i<len(a):
#         sum=sum+i
#         i=i+1
#         sum1=0
#         while i<len(a):
#             sum1=sum1+i
#             i=i+1
#             sum2=0
#             while i<len(a):
#                 sum2=sum2+1
#                 i=i+1                
#         print(sum+sum1+sum2)
# sum_number()

def column_sum(lst):
      
    #  return [sum(i) for i in zip(*lst)]
    
    lst=[1,2,3,[4,5,6],7,[8,9]]
    i=1
    while i<zip(*lst):
        print(column_sum(lst))
        i=i+1
    (column_sum(lst))

def column_sum(lst):
    arr=(lst)
    return sum(arr, 0).tolist()
      
lst=[1,2,3,[4,5,6],7,[8,9]]
print(column_sum(lst))
