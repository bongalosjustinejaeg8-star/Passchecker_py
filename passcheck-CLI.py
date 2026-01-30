import string
import math
N = 0
password = input("Enter Sample password: ")
length = len(password)
for i in password:
    if i in string.digits:
        N+=len(string.digits)
        break
for i in password:
    if i in string.ascii_lowercase:
        N+=len(string.ascii_lowercase)
        break
for i in password:
    if i in string.ascii_uppercase:
        N+=len(string.ascii_uppercase)
        break
for i in password:
    if i in string.punctuation:
        N+=len(string.punctuation)
        break

entropy =math.log2(N**length)
print (entropy)
if entropy <= 72:
    print("weak ahh password")
elif entropy <=115:
    print("password pretty mid like u")
elif entropy <= 200:
    print("strong password")
else:
    print("ts ahh pass so tuff fr")



