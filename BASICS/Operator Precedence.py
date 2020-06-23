#In this lets see about "Operator Precedence" in Python Programming.

#Operator Precedence is used to which operator should be evaluated first.

#The precedence of the operators in Python is

#1) Exponent Operator - ( ** )

#2) Negation , unary puls and minus - ( ~ , + , - )

#3) The multiplication, divide, modules and floor division - ( * , / , % , // )

#4) Binary plus and minus - ( + , - )

#5) Left shift and Right shift - ( >> , << )

#6) Binary AND , XOR   and OR - ( & , ^ , | )

#7) Comparison Operators - ( <= , < , > , >= , == , != )

#8) Assignment Operators - ( = , %= , /= , //= , -= , += *= , **= )

#9) Identity Operators - ( is , is not )

#10) Membership Operators - ( in , not in )

#11) Logical Operators - ( not , or , and )

#Here is the simple program to understand this Operators Precedence in Python Program.

#Declaring variables

a = 10

b = 20

c = 30

d = 15

e = a + b * c / d    

print("\nValue of a + b * c / d is e = " , e )

e = ( a + b ) * ( c / d )   

print("\nValue of ( a + b ) * ( c / d ) is e = " , e )

e = ( a + b ) *  c / d   

print("\nValue of ( a + b ) *  c / d  is e = " , e )

e = ( ( a + b ) *  c ) / d  

print("\nValue of ( ( a + b ) *  c ) / d  is e = " , e )

e =  a + ( b  *  c / d ) ;  

print("\nValue of a +(  b *  c / d ) is e = " , e )

e =  a + ( b  *  c ) / d 

print("\nValue of a + ( b  *  c ) / d is e = " , e )

e = ( a + ( b  *  c ) ) / d   

print("\nValue of ( a + ( b  *  c ) ) / d is e = " , e )