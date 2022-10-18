score = float(input("What grade did you get on the test?: "))
def percentage_to_letter(score=0):
  if score >= 90:
    return("A")
  elif score >= 80 and score < 90:
    return("B")
  elif score >=70 and score < 80:
    return("C")
  elif score >= 60 and score < 70:
    return("D")
  else:
    return("F")
percentage_to_letter()
gradeLetter = percentage_to_letter(score)
print(gradeLetter)

def is_passing(letter=None):
  if letter == "A" or letter ==  "B" or letter == "C":
    return(True)
  elif letter == "D" or "F":
    return(False)
percentage_to_letter()
print(is_passing(gradeLetter))
