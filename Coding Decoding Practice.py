import string
import random
#  Coding Decoding
reply=input("Do u want to code or decode, For code press c and For decode press d?")
word=input("Enter your word?")
a=""
if(reply=='c' or reply=='C'):
    if (len(word)<=3):
        a=word[::-1]
    else:
       firstRandom=''.join(random.choice(string.ascii_letters) for _ in range(3))
       lastRandom=''.join(random.choice(string.ascii_letters) for _ in range(3))
       char=word[0]
       word=word.replace(word[0],"")
       a=firstRandom+word+char+lastRandom

elif(reply=='d' or reply=='D'):
     
     if(len(word)>=7):
        firstindex=word[:3]
        lastIndex=word[-3:]
        word=word.replace(word[0:3],"")
        word=word.replace(word[-3:],"")     
        if(len(word)<=3):
           a=word[::-1]
        else:
           char=word[-1]
           word=word.replace(word[-1],"")
           a=char+word
              
print(a)     