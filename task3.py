#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

(2 points)
'''

def split(input):
    '''
    parameters
    str input - string to be split
    
    return
    str new string with line break in the middle
    '''
    mid=len(input)/2
    mid=int(mid)
    total1=input[0:mid]
    total2=input[mid:len(input)+1]
    totals=total1+"\n"+total2
    return totals

if __name__ == "__main__":
    sentence = "There is a big balloon in the blue sky"
    assert split(sentence) == "There is a big ball\noon in the blue sky"

    sentence = "I am a fat cat"
    assert split(sentence) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(sentence) == "I was a\n fat cat"