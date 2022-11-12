class StringUtility:
  def __init__(self, string):
    self.string = string
  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    vowels = "aeiouAEIOU"
    for letters in self.string:
      if letters in vowels:
        count = count + 1
      if count >= 5:
        return "many"
      else:
        return str(count)
      
  def bothEnds(self):
    count = len(self.string)
    count += len(self.string)
    if count > 3 or count == 3:
      smallstring = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
      return smallstring

  def fixStart(self):
      stringasterisk = self.string[0] +self.string[1].replace(self.string[0],"*")
      if len(self.string) <= 1:
        self.string = self.string
        return stringasterisk

  def asciiSum(self):
    sum = 0
    for ascii in self.string:
      for chars in ascii:
        letters = ord(chars)
        sum =  sum + letters
      return sum

  def cipher(self):
    for i in self.string:
      for letters in i:
        shift = ord(letters)
        shift = shift + 3
      for i in shift:
        chr(i)
        return shift
    
      



  