def add(a, b, c=0):
  if not (isinstance(a,(int, float)) and isinstance(b,(int, float)) and isinstance(c,(int, float))):
    return -1
  
  if not (0 <= a <= 10 and 0 <= b <= 10 and 0 <= c <= 10):
    return -2
  
  try:
    return int(a + b) + int(c)
  except:
    return "error"
