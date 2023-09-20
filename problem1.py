"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split function.
Have the user enter a sentence or paragraph and gives a word count.
"""

string1="hello, hello!! hi"
count=0
for i in range(len(string1)):
    if string1[i:i+1]==" ":
        count+=1
wordc=count+1
print(f"words : {wordc}")
print(f"characters : {len(string1)}")

        
