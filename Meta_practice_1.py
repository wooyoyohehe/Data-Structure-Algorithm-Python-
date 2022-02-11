import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input, rotation_factor):
  # Write your code here
  output = ""
  for i in range(len(input)):
    if "a"<=input[i]<="z":
      output += chr(ord("a") + (ord(input[i])-ord("a")+rotation_factor)%26)
    elif "A"<=input[i]<="Z":
      output += chr(ord("A") + (ord(input[i])-ord("A")+rotation_factor)%26)
    elif "0"<=input[i]<="9":
      output += chr(ord("0") + (ord(input[i])-ord("0")+rotation_factor)%10)
    else:
      output += input[i]
  return output