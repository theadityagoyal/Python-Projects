decimal_number=int(input('Enter the Decimal number: '))
print('The decimal number is ',decimal_number)

print(bin (decimal_number),'in binary: ')
print(oct (decimal_number),'in octal: ')
print(hex (decimal_number),'in Hexadecimal: ')

# def convertdecimaltobinary(n):
#     if n>1:
#         convertdecimaltobinary(n//2)
#     print(n%2,end='')
# decimal_number=int(input('Enter the Decimal number: '))
# convertdecimaltobinary(decimal_number)
# print()