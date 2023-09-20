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

input="There is a big balloon in the blue sky"
mid=len(input)/2
mid=int(mid)
total1=input[0:mid]
total2=input[mid:len(input)+1]
totals=total1+"\n"+total2
print(totals)