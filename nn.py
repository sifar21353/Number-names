n = input('Enter int: ')
text = open('nums.csv','r')
count = len(n) - 2
a = False
for i in range(len(n)):
  text = open('nums.csv','r')
  if n[i] == '0':
    pass
  elif i == len(n) - 2:
    if n[len(n) - 2] == '1' and n[len(n) - 1] == '1':
      print('eleven', end = '')
      a = True
    elif n[len(n) - 2] == '1' and n[len(n) - 1] == '2':
      print('twelve', end = '')
      a = True
    elif n[len(n) - 2] == '1' and n[len(n) - 1] == '3':
      print('thirteen', end = '')
      a = True
    elif n[len(n) - 2] == '1' and n[len(n) - 1] == '4':
      print('fourteen', end = '')
      a = True
    elif n[len(n) - 2] == '1' and n[len(n) - 1] == '5':
      print('fifteen', end = '')
      a = True
    elif n[len(n) - 2] == '1' and n[len(n) - 1] == '6':
      print('sixteen', end = '')
      a = True
    elif n[len(n) - 2] == '1' and n[len(n) - 1] == '7':
      print('seventeen', end = '')
      a = True
    elif n[len(n) - 2] == '1' and n[len(n) - 1] == '8':
      print('eighteen', end = '')
      a = True
    elif n[len(n) - 2] == '1' and n[len(n) - 1] == '9':
      print('nineteen', end = '')
      a = True
    elif n[i] == '1' and (i == (len(n) - 4) or i == (len(n) - 1))and a == False:
      print('one', end = '')
    elif n[i] == '1' and a == False:
      print('ten', end = '')
    elif n[i] == '2' and (i == (len(n) - 3) or i == (len(n) - 1)):
      print('two', end = '')
    elif n[i] == '2':
      print('twen', end = '')
    elif n[i] == '3':
      print('three', end = '')
    elif n[i] == '4':
      print('four', end = '')
    elif n[i] == '5':
      print('five', end = '')
    elif n[i] == '6':
      print('six', end = '')
    elif n[i] == '7':
      print('seven', end = '')
    elif n[i] == '8':
      print('eight', end = '')
    elif n[i] == '9':
      print('nine', end = '')

  elif n[i] == '1' and (i == (len(n) - 4) or i == (len(n) - 1))and a == False:
    print('one', end = '')
  elif n[i] == '1' and a == False:
    print('ten', end = '')
  elif n[i] == '2' and (i == (len(n) - 3) or i == (len(n) - 1)):
    print('two', end = '')
  elif n[i] == '2':
    print('twen', end = '')
  elif n[i] == '3':
    print('three', end = '')
  elif n[i] == '4':
    print('four', end = '')
  elif n[i] == '5':
    print('five', end = '')
  elif n[i] == '6':
    print('six', end = '')
  elif n[i] == '7':
    print('seven', end = '')
  elif n[i] == '8':
    print('eight', end = '')
  elif n[i] == '9':
    print('nine', end = '')
  for i in text:
    if a == False:
      l1 = i.split(',')
      if count == -1:
        pass
      else:
        print(l1[count], end = ' ')
        count -= 1

text.close()
