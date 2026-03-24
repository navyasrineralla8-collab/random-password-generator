import string
import random
def generatePassword(length):
    if length<4:
            return "the password should be atleats length greater than 4"
    lower=random.choice(string.ascii_lowercase)
    upper=random.choice(string.ascii_uppercase)
    digit=random.choice(string.digits)
    symbols=random.choice(string.punctuation)
    remaining="".join(random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(length-4))
    password=list(lower+upper+digit+symbols+remaining)
    random.shuffle(password)
    return "".join(password)
length=int(input("enter length of password"))
print("strong password:",generatePassword(length))
