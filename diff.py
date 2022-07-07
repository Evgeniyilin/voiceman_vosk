import difflib

def similarity(s1, s2):  
  matcher = difflib.SequenceMatcher(None, s1, s2)
  return matcher.ratio()

genuine = ("",
          "гет запрос",
          "пост запрос", 
          "крит реакт эп")

plagiary = "гет запроса"

per_match = similarity(genuine[0], plagiary)
print(per_match)

# per_match = 0

print(len(genuine))

i = 0
id = 0
while i < len(genuine):
    if (per_match < similarity(genuine[i], plagiary)):
      per_match = similarity(genuine[i], plagiary)
      id = i
    i += 1
print(id)
