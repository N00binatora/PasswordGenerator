import random
import string


leets = [1,2,3,4,5,6,7,8, 10, 11]
for int in leets:
    print(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits + string.octdigits), end ="") 
    