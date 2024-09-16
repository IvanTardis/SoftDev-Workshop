def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  else:
    return a+b

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return 2*(n - 21)

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour>20)

def makes10(a, b):
  return a == 10 or b == 10 or (a+b) == 10

def near_hundred(n):
  return abs(n - 100) <= 10 or abs(n - 200) <= 10

def pos_neg(a, b, negative):
  if(negative):
    return a <0 and b <0
  else:
    return (a > 0 and b < 0) or (a < 0 and b > 0)

def not_string(str):
  if "not" in str[0:3]:
    return str
  else:
    return "not " + str

def missing_char(str, n):
  return str[0:n] + str[n+1:]

def front_back(str):
  if len(str) < 2:
    return str
  return str[len(str) - 1] + str[1:len(str)-1] + str[0]

def front3(str):
  if len(str) < 3:
    return str*3
  return str[0:3]*3
