input = 'my dog has fleas'
k=input.index('dog')
i=0
total=""
while i<k:
    total=total+input[i:i+1]
    i+=1
total+='kitty'
total+=input[k+3:len(input)]
modifiedString = total
print(modifiedString) 