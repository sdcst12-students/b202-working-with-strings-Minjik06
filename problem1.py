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


if __name__ == "__main__":
    string2="hello, hello!! hi"
    assert countstr(string2) == f"words : {3}, characters : {17}"
    string3= "hello my name is minji and I like dog"
    assert countstr(string3) == f"words : {9}, characters : {37}"


    #"words : {13}, characters : {17}
    
"""def countstr(stri):
    string1=stri
    num=[]
    count=0
    for i in range(len(string1)):
        if string1[i:i+1]==" ":
            count+=1
    wordc=count+1
    num.append(wordc)
    a1=len(string1)
    a1=int(a1)
    num.append(a1)
    return num


if __name__ == "__main__":
    string2="hello, hello!! hi"
    assert countstr(string2) == [3, 17]"""

        
