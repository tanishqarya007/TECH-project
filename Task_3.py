# a) Calculate the temperature altitude from a list of temperatures
#temperatures = [3, -20, -6, -12, 'error', 24, 18, 28, 16, 14]
def temperature():
  m=a=0
  temp = [3, -20, -6, -12, 'error', 24, 18, 28, 16, 14]
  for i in temp:
    if type(i) is int:
       if a<i:
          a=i
       if m>i:
          m=i
  diff=a-m
print("TEMPERATURE ALLTITUDE IS =")


# b) Count frequency of every character in a string (using dictionaries)
def sec():
    istr=input("enter the string ")
    freq = {} 
    print(istr.upper())
    for char in istr: 
        if char in freq: 
          freq[char] += 1
        else: 
         freq[char] = 1
    print("Per char frequency in '{}' is :\n {}".format(istr, str(freq)))

# c) Verify De Morgan Laws (using sets)
#U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
#A = {0, 2, 4, 6, 8}
#B = {3, 6, 9}
def morgan():
    U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    A = {0, 2, 4, 6, 8}
    B = {3, 6, 9}
    x = (not(A and B))==((not A) or (not B))
    y = (not(A or B))==((not A) and (not B))
    print('x is :', x, '\ny is :' ,y)
    print("Hence De Morgan's Law is Verified")