"""input = 'i have a dog and a goldfish as my pets'
k=input.index('dog')
i=0
total=""
while i<k:
    total=total+input[i:i+1]
    i+=1
total+='kitty'
total+=input[k+3:len(input)]
modifiedString = total
print(modifiedString) """

"""input="I'm JuSt A LiTtle Black RainCLOUD!"
text1=""
text1=input[0:1]
text1=text1.upper()
text2=input[1: len(input)]
text2=text2.lower()
text=text1+text2
    
print(text)"""

"""input="There is a big balloon in the blue sky"
mid=len(input)/2
mid=int(mid)
total1=input[0:mid]
total2=input[mid:len(input)+1]
totals=total1+"\n"+total2
print(totals)"""

"""ranks = "A23456789TJQK"
suits = "CDHS"
lis=[""]
x=0
for i in range(len(ranks)):
      for j in range(len(suits)):
        k=ranks[i:i+1],suits[j:j+1]
        lis.append(k)
        x=x+1
print(lis)"""

string1="hello my name is minji and I like dog"
count=0
for i in range(len(string1)):
  if string1[i:i+1]==" ":
    count+=1
wordc=count+1
print(f"words : {wordc}, characters : {len(string1)}") 


