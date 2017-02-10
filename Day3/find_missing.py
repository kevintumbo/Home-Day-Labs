 def find_missing(a, b):
     new = [num for num in b if num not in a]
     if not new:
         return 0
     return new[0]