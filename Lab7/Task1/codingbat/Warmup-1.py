#diff21
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
  
#parrot_trouble
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

#makes10
def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)

#near_hundred
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#pos_neg
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
  
#not_string
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

#missing_char
def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

#front_back
def front_back(str):
  if len(str) <= 1:
    return str
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  return str[len(str)-1] + mid + str[0]

#front3
def front3(str):
  return str[:3] * 3

#monkey_trouble
def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or (not a_smile and not b_smile) 

#sleep_in
def sleep_in(weekday, vacation):
  return (not weekday or vacation)

#sum_double
def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  else:
    return a + b
  
