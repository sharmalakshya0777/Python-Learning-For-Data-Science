# ========================================================
# 1. THE PROBLEM (Alag-alag variables banana mushkil hai)
# ========================================================
marks1 = 94.4
marks2 = 87.5
marks3 = 95.2
marks4 = 66.4
marks5 = 45.4


# ========================================================
# 2. THE SOLUTION: LIST CREATION (Data Ka Single Folder)
# ========================================================
# Sabhi variables ko hata kar ek single list 'Marks' me store kiya
Marks = [94.4, 87.5, 95.1, 66.4, 45.1]
print(Marks)
print(type(Marks))  # Output: <class 'list'>


# ========================================================
# 3. LIST INDEXING (Seat Number Se Data Nikalna)
# ========================================================
# Index hamesha 0 se start hota hai: [0]=94.4, [1]=87.5, [2]=95.1...
print(Marks[0], Marks[1])  # Output: 94.4 87.5


# ========================================================
# 4. LIST METHODS (Readymade Tools To Modify List)
# ========================================================

# A. append(): Yeh naye element ko list ke bilkul AAKHRI (end) me jodta hai
Marks.append(59.4)  # Ab 59.4 list ke last me add ho jayega

# B. insert(): Yeh hamare bataye gaye index (seat number) par data ghusata hai
# Syntax: insert(index, value) -> Index 5 par 44.4 daal do
Marks.insert(5, 44.4) 

# C. sort(): Yeh list ko Ascending Order (Chote se Bada / 1 to 10) me arrange karta hai
Marks.sort()

# D. sort(reverse=True): Yeh list ko Descending Order (Bade se Chota / 10 to 1) me arrange karta hai
Marks.sort(reverse=True)

# E. reverse(): (Commented out) Yeh bina sort kiye, list ko bas ulta (flip) kar deta hai
# Marks.reverse()


# ========================================================
# 5. FINAL OUTPUT (Methods Ke Baad Ka State)
# ========================================================
# Yahan par sorted (Bade se Chota) aur modify hui final list print hogi
print(Marks)


# ========================================================
# 6. DELETING ELEMENTS FROM LIST (Data Hatane Ke Tareeke)
# ========================================================

# F. remove(value): Yeh list me se direct us VALUE ko dhoond kar delete karta hai.
# NOTE: Agar list me '1' nahi hai, toh yeh ValueError dega. Agar 94.4 hatana ho toh Marks.remove(94.4) likhenge.
Marks.remove(1) 

# G. pop(index): Yeh bataye gaye INDEX (seat number) waale element ko uda deta hai.
# Marks.pop(0) karne se index 0 par jo sabse badi value baithi thi, woh hat jayegi.
Marks.pop(0)

#tupels

