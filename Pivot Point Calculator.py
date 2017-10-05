#This is a simple program to calculate the pivot point in Forex Trading
#This is created by Md. Rakibul Islam

#inputs from the user

high = float(input('High= '))
low = float(input('Low= '))
closed = float(input('Closed= '))

print('\n')

#Considering pivot point as 'p'

p = (high+low+closed)/3

r1 = (p*2)-low
r2 = p +(high-low)
r3 = high +2*(p -low)

s1 = (p*2) -high
s2 = p -(high-low)
s3 = low -2*(high -p)

print('The values are:')
print('r3= ', "%.2f"%r3)
print('r2= ', "%.2f"%r2)
print('r1= ', "%.2f"%r1)

print(' p= ', "%.2f"%p)

print('s1= ', "%.2f"%s1)
print('s2= ', "%.2f"%s2)
print('s3= ', "%.2f"%s3)


input()


