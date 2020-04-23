n = input()
vowel = ["a", "e", "i", "o", "u", "y"]
for i in n:
  if i.lower() not in vowel:
    print("." + i.lower(), end = "")
print()
