# ========================================================
# 1. STRING CREATION (String Banane Ke 3 Tareeke)
# ========================================================
str1 = "This is a string"
str2 = 'lakshya'   # Single, Double aur Triple quotes - teeno valid hain
str3 = """sharma"""


# ========================================================
# 2. ESCAPE SEQUENCE CHARACTERS (Text Formatting Tools)
# ========================================================
# Galti ka reason (Commented out): Normal string bina special tools ke line break nahi jhel sakti
# str4 = "This is a string.  
# we are creating in python"  

# \n (New Line): Cursor ko automatic agli line me dhakel deta hai
str4 = "This is a string.\nwe are creating in python" 
print(str4)

# \t (Tab Space): Word ke beech me ek systematic lamba space (4-8 spaces) deta hai
str4 = "This is a string.\twe are creating in python" 
print(str4)


# ========================================================
# 3. BASIC STRING OPERATIONS (Jodna Aur Ginna)
# ========================================================

# A. Concatenation: '+' ka use karke strings ko aapas me ek silsile me jodna
print(str2 + " " + str3)  # Output: lakshya sharma

# B. Length: len() function spaces aur special characters ko mila kar poori length batata hai
print(len(str4))

# C. Indexing: Har character ko seat number dena (Aage se counting 0 se start hoti hai)
#  L  a  k  s  h  y  a     S  h  a  r  m  a
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13
str_name = "Lakshya Sharma"
print(str_name[0])  # Output: L


# ========================================================
# 4. STRING SLICING (Bade Text Se Chota Tukda Kaatna)
# ========================================================
name = "Lakshya Sharma"

# Formula: [start_index : end_index] -> end index hamesha exclusive (ek pehle tak) hota hai
print(name[0:7])  # 0 se index 6 tak chalega -> Output: Lakshya
print(name[0:])   # Start 0 se, end empty hai matlab bilkul aakhri tak jayega -> Output: Lakshya Sharma
print(name[:])    # Dono side blank hain yani poori string ki photocopy -> Output: Lakshya Sharma


# ========================================================
# 5. NEGATIVE INDEXING (Peeche Se Ulte Numbers Me Counting)
# ========================================================
#  L    a    k    s   h   y   a       S   h   a   r   m   a
# -14  -13  -12  -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
name = "Lakshya Sharma"

# Lakshya's Update: -14 se start kiya aur end blank chhoda, matlab start se lekar full end tak print hoga
print(name[-14:]) # Output: Lakshya Sharma
print(name[-7:])  # Index -7 (S) se shuru hoke end tak jayega -> Output: Sharma


# ========================================================
# 6. STRING FUNCTIONS (Inbuilt Readymade Tools)
# ========================================================
# Note: Python me strings immutable hoti hain, isliye ye functions naya temporary output dete hain, original variable badal nahi jata.

test_str = "lakshya sharma"

print(test_str.endswith("ma"))       # Check karega true/false -> Output: True
print(test_str.startswith("lak"))    # Check karega true/false -> Output: True
print(test_str.replace("lakshya", "LAKSHYA")) # Purane word ki jagah naya word fit karega
print(test_str.find("sharma"))       # Dhundega ki woh word kis index position se start ho raha hai (Index: 8)
print(test_str.count("a"))          # Poori string me woh character kitni baar repeat hua -> Output: 4
print(test_str.capitalize())        # Sirf pehle word ka pehla character capital (L) karega, baaki sab small


# ========================================================
# 7. CONDITIONAL STATEMENTS (if-elif-else Syntax & Rules)
# ========================================================
"""
if (Condition):
    statement1
elif (Condition):
    statement2
else:
    statement3
"""

# PRACTICAL IMPLEMENTATION EXAMPLE (Traffic Light Logic):
light = "green"

if (light == "red"):
    print("STOP! Gaadi roko.")
elif (light == "yellow"):
    print("LOOK! Dekho aur slow ho jao.")
else:
    print("GO! Aap ja sakte hain.")  # Agar light red ya yellow nahi hai, toh green hi hogi

# RULE 1: Python me {} brackets nahi hote block batane ke liye, indentation (4 spaces/1 Tab space) zaroori hai.
# RULE 2: 'if' aur 'elif' ke baad colon ':' lagana compulsory hai.