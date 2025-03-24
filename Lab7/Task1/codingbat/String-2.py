#cat dog
def cat_dog(str):
  return str.count('cat') == str.count('dog')

#count code
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count

#end other
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a.endswith(b) or b.endswith(a)

#xyz there
def xyz_there(str):
  for i in range(len(str)):
    if str[i:i+3] == 'xyz':
      if i == 0 or str[i-1] != '.':
        return
  return False  

#count hi
def count_hi(str):
  return str.count('hi')

#double char
def double_char(str):
  result = ''
  for char in str:
    result += char * 2
  return result
