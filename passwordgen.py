import random
def pass_gen():
      l=["!","@","#","$","%","*"]
      cap=chr(random.randint(65,90))
      small=chr(random.randint(97,122))
      sym=random.choice(l)
      num=random.randint(10000,999999)
      passwor =cap+sym+str(num)+small
      return passwor

print("RANDOM PASSWORD IS:")
print(pass_gen())    