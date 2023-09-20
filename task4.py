#!python3

"""
Strings are iterable.  Use for loops to iterate through both strings to create a list to represent a deck of cards. Note: We can also use list comprehension as strings are still iterable!
"""

ranks = "A23456789TJQK"
suits = "CDHS"


def createDeck():
  lis=[]
  x=0
  """lis=[f"{i+j}" for i in len(ranks) for j in len(suits)]"""

  lis=[]
  x=0
  for i in range(len(ranks)):
      for j in range(len(suits)):
        k=ranks[i:i+1]+suits[j:j+1]
        lis.append(k)
        x=x+1
  return lis

def main():
  deck = createDeck()
  print(deck)
  assert "AS" in deck
  assert "KC" in deck
  assert deck.count("TC") == 1


if __name__ == "__main__":
  main()
