import string
import math
N = 0
password = input("Enter Sample password: ")
length = len(password)
for i in password:
    if i in string.digits:
        N+=10
        break
for i in password:
    if i in string.digits:



