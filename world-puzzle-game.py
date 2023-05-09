import random
l1=['top','try','chill','move','father','brake','green','aeroplane','sample']
l2=['llcih','yrt','evom','pot','afhtre','kabre','reneg','oaerelanp','elpmas']
l2=random.sample(l2,9)
print('welcome to world puzzle game')
i=5
b=0
for e in l2:
    if b>=5:
     break
    print("Your set of character is : ", e)
    a=input('enter your answer: ')
    b+=1
    if a not in l1 and i>0:
      i=i-1
print('your score is out of 5 is: ',i)


      
