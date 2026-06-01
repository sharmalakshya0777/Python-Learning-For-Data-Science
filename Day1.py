# ==========================================
# 1. BASIC PRINT STATEMENTS (Screen Par Dikhana)
# ==========================================

# Normal text print karne ke liye double quotes "" ka use hota hai
print("Lakshya is my name.")
print("My age is 21")

# Comma ',' lagane se dono cheezein ek hi line me print ho jati hain aur beech me space aa jata hai
print("Lakshya is my name.", "My age 21")
print("Hello Lakshya!")

# ==========================================
# 2. VARIABLES & IDENTIFIERS (Data Ke Dabbe)
# ==========================================

# 'name' ek Identifier (naam) hai, jo ek String type ke variable (dabbe) ko point kar raha hai
name = "Lakshya"
# 'age' ek naya Identifier hai jisme number 21 store hai
age = 21

# Variables ke andar ki value ko print karna
print(name)
print(age)

# Text ke saath variable ki value jod kar print karna
print("My name is : ", name)
print("My age is : ", age)

# Re-assignment: 'age' naam ke purane dabbe me se 21 hata kar ab 21 fir se daal diya (ya 23 kar diya)
age = 21

# Python mein hum naye variables aise hi banate hain bina kisi type ko pehle bataye.

# ==========================================
# 3. DATA TYPES (Dabbe Ka Type/Nature)
# ==========================================

# type() function batata hai ki variable kis tarah ka data hold kar raha hai
print(type(name))  # Output: <class 'str'> (Yani String / Text data)
print(type(age))   # Output: <class 'int'> (Yani Integer / Bina point wala number)

# Age ki value ko update kiya (Ab age 23 ho gayi)
age = 23 

# Boolean Type: Isme sirf do hi values ho sakti hain - True ya False (Dhyan rahe T aur F capital honge)
old = False

# None Type: Iska matlab hai "Kuch Nahi" (Khaali dabba). Jab kisi variable me koi value na ho
a = None

print(type(old))  # Output: <class 'bool'> (Yani Boolean / Haan ya Naa)
print(type(a))    # Output: <class 'NoneType'> (Yani bilkul khaali value)

# ==========================================
# 4. ARITHMETIC OPERATORS (Hisab-Kitab)
# ==========================================
num1 = 2
num2 = 3

print("Addition", num1 + num2)       # 2 + 3 = 5
print("Subtraction", num1 - num2)    # 2 - 3 = -1
print("Multiple", num1 * num2)       # 2 * 3 = 6
print("Division", num1 / num2)       # 2 / 3 = 0.666... (Hamesha point me aayega)
print("Modulus", num1 % num2)        # 2 ko 3 se divide karne par bacha (Remainder) = 2
print("Power", num1 ** num2)         # 2 ki power 3 yani 2 * 2 * 2 = 8

# ==========================================
# 5. RELATIONAL OPERATORS (Comparison / Tulna)
# ==========================================
# Inka answer hamesha True ya False (Boolean) me aata hai

num1 = 2
num2 = 3 

print(num1 == num2) # Kya 2 aur 3 barabar hain? -> False
print(num1 != num2) # Kya 2 aur 3 alag-alag hain? -> True 
print(num1 > num2)  # Kya 2 bada hai 3 se? -> False
print(num1 < num2)  # Kya 2 chota hai 3 se? -> True
print(num1 >= num2) # Kya 2 bada ya barabar hai 3 ke? -> False
print(num1 <= num2) # Kya 2 chota ya barabar hai 3 ke? -> True

# ==========================================
# 6. ASSIGNMENT OPERATORS (Short-cut Se Value Badalna)
# ==========================================
num1 = 2

num1 += 2   # num1 = 2 + 2 -> 4
print(num1)
num1 -= 2   # num1 = 4 - 2 -> 2
print(num1)
num1 *= 2   # num1 = 2 * 2 -> 4
print(num1)
num1 **= 2  # num1 = 4 ki power 2 (4 * 4) -> 16
print(num1)
num1 /= 2   # num1 = 16 / 2 -> 8.0 (Point me badal gaya)
print(num1)
num1 %= 2   # num1 = 8.0 % 2 -> Remainder bacha 0.0
print(num1)

# ==========================================
# 7. LOGICAL OPERATORS (Short Revision)
# ==========================================
# and: Dono conditions ka sahi hona zaroori hai
# or: Koi ek condition bhi sahi ho toh chalega
# not: True ko False aur False ko True bana deta hai

# Hamaare paas do conditions hain
has_maths = True          # Aapke paas class 12 me maths tha (True)
has_zero_coding = True    # Aapko coding zero aati hai (True)

# 1. AND Operator Example
# Dono conditions True hongi tabhi final answer True aayega
print("AND Result:", has_maths and has_zero_coding)  # Output: True

# 2. OR Operator Example
# Koi ek bhi condition True hui toh answer True aayega
has_bike = False
has_metro = True
print("OR Result:", has_bike or has_metro)          # Output: True (kyunki metro hai)

# 3. NOT Operator Example
# Yeh value ko ulta kar deta hai
is_raining = True
print("NOT Result:", not is_raining)                 # Output: False (kyunki True ka ulta False)


# 1. Type Conversion (Implicit - Python interpreter khud karta hai)


a = 2       # Yeh Integer (bina point wala number) hai
b = 4.25    # Yeh Float (point wala number) hai

# Python bina data loss kiye 'a' ko apne aap float (2.0) mein badal dega
sum = a + b 

print(sum)  # Output: 6.25


# ========================================================
# 2. Type Casting (Explicit - Done by Programmer)
# ========================================================

# WRONG LOGIC (Commented out taaki code crash na ho):
# a = "hello"
# b = 4.25
# sum = float(a) + b  # ERROR! "hello" ko float mein nahi badla ja sakta.

# RIGHT LOGIC: String ke andar valid number hona chahiye
a = "5.5"   # Yeh dikhne mein text/string hai, par andar ek number hai
b = 4.25    # Yeh float hai

# Programmer ne Python ko zabardasti bola ki string "5.5" ko sachमुच float bana do
sum = float(a) + b 

print(sum)  # Output: 9.75

# USER INPUT HANDLING IN PYTHON

# Step 1: input() user se text "21" lega (String format me)
# Step 2: int() us "21" ka wrapper hata kar use pure number 21 (Integer) bana dega
num = int(input("Enter the number: "))

# Final output screen par dikhane ke liye
print("The value of number is :", num)

# RULE 1: input() -> Yeh function hamesha 'String' (text) return karta hai, chahe aap number hi kyun na type karein.
# RULE 2: int(input()) -> Yeh pehle input leta hai, fir use zabardasti 'Integer' (pure number) mein badal deta hai.