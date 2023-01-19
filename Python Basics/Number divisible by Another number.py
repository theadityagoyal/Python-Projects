my_list=[165 , 556 ,60,66,897,6544,643,2,2,664,6,646465,
         32526,6562,66,879,99,966,1,235,69,789,4587,54 ]
num=int(input('Enter The number you want a divisible in list:'))

result=list(filter(lambda x:(x%num==0),my_list))
print(num,'is divisible',result)