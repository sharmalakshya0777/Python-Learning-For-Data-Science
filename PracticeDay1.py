# ==========================================
# 1. PRICE & DISCOUNT CALCULATION
# ==========================================
price = int(input("Enter amount of item:"))
discount = int(input("Enter how much discount for the user:"))

result = price*(discount/100)#Original Price × (Discount Percentage / 100)
newPrice = price-result
print("The final amount will be:",newPrice) 

# Hardcoded Value Test
price = "499"
discount = 50
print(int(price)-discount)


# ==========================================
# 2. STOCK MANAGEMENT
# ==========================================
items_in_stock = 100
items_in_stock -= 7
items_in_stock -= 7
items_in_stock -= 7
print(items_in_stock)


# ==========================================
# 3. AGE CHECK (RELATIONAL OPERATOR)
# ==========================================
age = int(input("Enter your age:"))
print(age>=18)


# ==========================================
# 4. LOGICAL OPERATORS (AUTHENTICATION)
# ==========================================
# ERROR FIX: Ek hi line me do assignments and se nahi judte, isliye alag line me likha:
is_logged_in = True
has_paid = False
print(is_logged_in and has_paid)


# ==========================================
# 5. CHAIN ASSIGNMENT PUZZLE
# ==========================================
x = 10
x += 5
x *= 2
x -= 3
x **= 2 
print(x)


# ==========================================
# 6. MULTI-OPERATOR USER INPUT CHALLENGE
# ==========================================
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(num1+num2>20)
mul=(num1*num2)
mul%=2
print(mul==0)
print(num1!=num2)

# better version: print((num1*num2)%2==0)


# ==========================================
# 7. FLOOR DIVISION VS MODULUS
# ==========================================
a = 5 
b = 2 
print("Times fitted:", a//b)
print("Remainder:", a%b)


# ==========================================
# 8. MIXED DATATYPE SUM
# ==========================================
A = 7.9
B = "3"
C = 2
print(A+float(B)+C)


# ==========================================
# 9. F-STRING AGE CALCULATOR (Year 2026)
# ==========================================
name = input("Enter yout name: ")
year = int(input("Enter your Year:"))
print(f"{name} is {2026-year} years old")


# ==========================================
# 10. COMPLEX LOGICAL GATE
# ==========================================
has_laptop = True
knows_python = False
has_internet = True
has_time = False

print((has_laptop  and has_internet )and (knows_python or has_time))