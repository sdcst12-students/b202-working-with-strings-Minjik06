"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split function.
Have the user enter a sentence or paragraph and gives a word count.
"""
def countstr(stri):
    string1=stri
    count=0
    for i in range(len(string1)):
        if string1[i:i+1]==" ":
            count+=1
    wordc=count+1
    return f"words : {wordc}, characters : {len(string1)}"


def main():
    string2="hello, hello!! hi"
    assert countstr(string2) == "words : 13, characters : 17"

        
