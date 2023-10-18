import math
import time
import random
import os
import shutil
import functools

# modules

import Module as MyModule # ou import print

#val = input("diz um numero ai fdp: ")
#val2 = input("diz outro numero ai corno: ")

#table = {}

#print('O resultado dessa porra foi ', math.floor(float(val) + float(val2)))

#string = str(input('Qual seu nome? '))

#r = string.find(' ')

#substring = string[:r]
#laststring = string[r:]
#reverse = string[::-1]

#print(substring, laststring, reverse)

#web1 = "http://youtube.com"

#slicer = slice(7,-4)

#print(web1[slicer])

#age = int(input('How old are you '))

#if age >= 100 :
    #print(":Skull:")
#elif age >= 40 and age <= 50 :
   # print(':Ok:')
#elif age <= 10:
  #  print(':lol:')
#else:
 #   print('else')

#temp = int(input('temperature outside is: '))

#if temp > 0 and temp <= 30:
 #   print(' the temperature is ok today ')

#    gooutside = input('Go outside?')

 #   if gooutside == True:
  #      print(' you are outside.')
   # else:
    #    print(' better be home. ')
#elif temp <= 0 or temp >= 30:

 #   print(' today is too cold to go outside')

#val = 1

#while val<10: # i know that for loop exists , relax.
#    val += 1 
 #   print('how are you?')

#name = None

#while not name:
 #   name = input('Your name please: ')

#if not name.find(' ') == -1:
 #   r = name.find(' ')
  #  laststring = name[r:]

   # print('be welcome sir ', laststring)
#else:
 #   print('be welcome ', name)

#for i in range(10+1):
 #   print(i)

#for i in range(50,100+1,1):
 #   print(i)

#for i in 'Bolsonaro, o messias':
 #   print(i.upper())

#for i in range(10,0,-1):
 #   print(i)
 #   time.sleep(1)
#print('feliz ano novo fdp')

#rows = int(input(' how many rows? '))
#colums = int(input(' how many columns? '))
#symbol = input(' symbol? ')

#for x in range(rows):
 #   for y in range(colums): 
  #      print(symbol, end="")
   # print()

#phonenumber = "123-456-7890"

#for i, in phonenumber:
 #   if i == '-':
  #      continue
   # print(i, end="")

#for i in range(1,21+1):
 #   if i == 13:
 #       continue
  #  else:
   #     print(i, end=" ")

#food = ["Pinata",'Hamburger','pizza','doghot','spahegiehtet']

#food.append('Russian food')
#food.insert(0,'cake')
#food.sort()
#food.clear()

#for i in food:
 #   print(i, end=" ")

#table = int(input('which table do you want to see? '))

#drinks = ['Coffe','Water','Water','Green Tea']
#dinner = ['pizza','hamburger','hotdog','russian food']
#dessert = ['cake','ice cream']

#food = [drinks,dinner,dessert]

#for i in food[table]:
    #for v in i:
 #       print(i, end=' ')

#student = ('Sofia', '15', 'Muie')

#print(student.index('Sofia'))

#for x in student:
 #   print(x)



#if not "Bro" in student:
 #   print('Bro nao ta aq')

#utensilios = {"Fork", "Spoon", "Knife"}
#dishes = {'bowl','plate','cup','Knife'}

#utensilios.add('Napkin')
#utensilios.remove('Fork')
#utensilios.clear()

#utensilios.update(dishes)

#print(utensilios.difference(dishes))

#for x in utensilios:
 #   print(x, end=" ")

#capitals = {'Brasil':'Brasilia', 'USA': 'Washington DC', 'China': 'Beijing', 'Russia': 'Moscow'}

#print(capitals['Russia'])
#print(capitals.get('Brasil'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#capitals.update({'Germany':'Berlin'})
#capitals.update({'USA':'São Paulo'})
#capitals.pop('China')
#capitals.clear()

#for k,v in capitals.items():
 #   print('key:',k,' Value:',v, )

#name = 'Joao pedro'

#if (name[0].islower()):
 #   print('true')
#else:
 #   print('not true')

#def Count(Question1,Question2):
 #   Val = Question1 + Question2
  #  return Val

#Return_Val = Count(1,6)

#print(Return_Val)

#def Count(First,Second,Last):
 #   String = First,' ',Second,' ',Last
  #  return String

#Stri = Count(First='Hello',Second='Sofia',Last='Heck')

#print(str(Stri))

#def add(*args):
 #   sum = 0 
  #  for i in args:
   #     sum += i
    #return sum

#print(add(1,2,3,5,2,1,4,5))

#def Dic(**kwargs):
 #   #print('Hello', kwargs['First'], ' ', kwargs['Last'])
  #  print('Hello',end=' ')

#    for k,v in kwargs.items():
 #       print(v,end=' ')

#Dic(Title = 'Sra', First = 'Sofia',Middle = 'Heck', Last = 'D. Santos')

#animal = 'cow'
#item = 'moon'

#pi = 3.14159
#number = 1000000

#print('the {0} jumped over the {1}'.format(animal,item))

#print(' the value of pi is {:.2f}'.format(pi))
#print(' the value of the number is {:,}'.format(number))
#print(' the binary version of the number is {:b}'.format(number))
#print(' the Scientific notation for this number is {:E}'.format(number))

#x = random.randint(1,10)
#y = random.random()

#mylist = ['rock','papers','scissors']
#z = random.choice(mylist)

#cards = [1,2,3,4,5,6,7,8,9,'J','K','Q','A']

#random.shuffle(cards)

#print('{}'.format(cards))

#try:
 #   numerador = int(input('1 ')) 
  #  Denominador = int(input('2 ')) 
   # result = numerador /Denominador
#except ZeroDivisionError as e:
 #   print(e)
  #  print(' n se divide por 0 imbecil')
#except ValueError as e:
 #   print(e)
  #  print(' ta querendo dividir letra burrão')
#except Exception as e:
 #   print(e)
  #  print('n previ desculpa')
#else:
 #   print(result)
#finally:
 #   print(' ALWAYS EXECUTE ')

#pathe = "C:\\Users\\gusta\\Desktop\\Text.txt"

#if os.path.exists(pathe):
 #   print('exists')
  #  if os.path.isfile(pathe):
   #     with open(pathe,'r') as file:



    #        print(file.read())
#else:
  #  print('not exist')

#pathe = "C:\\Users\\gusta\\Desktop\\Text.txt"
#
#text = '\nFirst file changed, how do you feel?'

#if os.path.exists(pathe):
 #   print('exists')
  #  if os.path.isfile(pathe):
   #     with open(pathe,'a') as file:
    #        file.write(text)
#else:
 #   print('not exist')

#pathe = "C:\\Users\\gusta\\Desktop\\Text.txt"
#pathe2 = "C:\\Users\\gusta\\Desktop\\Pass to me.txt"

#shutil.copyfile(pathe)

#source = "Folder"
#Destination = "C:\\Users\\gusta\\Desktop\\Folder"

#try:
 #   if os.path.exists(Destination):
  #      print('theres a file here')
   # else:
    #    os.replace(source,Destination)
     #   print('done.')
#except FileNotFoundError:
 #   print('source not found')

#source = "test.txt"
#
#try:
 #   if os.path.isdir(source):
  #      boolean = input(' do you want to Continue? Y for yes N for no')
   #     if boolean.upper() == 'Y':
    #        shutil.rmtree(source)
    #else:
      #  os.remove(source)

#except OSError as e:
 #   print(' cannot delete that')
#except FileNotFoundError as e:
 #   print(' file not found')
#except PermissionError as e:
 #   print(' Do not have Perm to do it')

#MyModule.Print('Tudo','Bem','?')


#foods = list()

#while food := input(' what food do you like? ').lower() != 'quit':
 #   foods.append(food)

#def hi():
 #   print(' hello ')

#hello = hi

#hello() # two names is kinda cool ngl

#say = print
#say('lol')

#def alto(text):
 #  return text.upper()

#def baixo(text):
 #   return text.lower()

#def func(feunc, texte):
 #   text = feunc(texte)
  #  print(text)

#func(baixo,'OI TUDO BEM?')

#def double(x):
 #   return x * 2

#double = lambda x:x * 2
#multiply = lambda x,y: x * y
#add = lambda x,y,z: x + y + z
#fullname = lambda first, last: first +' '+ last
#age = lambda age: True if age >= 18 else False

#print(age(19))

#studantes = ['d','a','c','u','e']
#studantes = ('d','a','c','u','e')

#studantes.sort(reverse=True)

#sortedd = sorted(studantes,reverse=True)

#for i in studantes:
 #   print(i)

#for i in sortedd:
#    print(i)

#students = (('bob esponja', 'A', 69),
 #           ('eu', 'SSS+', 15),
  #          ('bolsonaro', 'B', 22))

#grade = lambda grades:grades[1]

#students.sort(key=grade,reverse=True)
#sortedd = sorted(students,key=grade,reverse=True)

#for i in sortedd:
 #   print(i)

#store = [('Shirt', 30),
 #        ('Pants', 25),
  #       ('Jacket', 45),
   #      ('Socks', 10.00)]

#to_euros = lambda data: (data[0],data[1]*0.82)
#to_dolars = lambda data: (data[0],data[1]/0.82)

#store_dolars = map(to_dolars, store)

#for i in store_dolars:
 #   print(i)

#friends = [('rachel',69),
 #          ('pietro',12),
  #         ('joao', 19),
   #        ('raquel', 10)]

#age = lambda data:data[1] >= 18

#lister = list(filter(age,friends))

#for i in lister:
 #   print(i)

#letters = ['A','B','C','D']
#word = functools.reduce(lambda x,y: x + y,letters)
#print(word)

#factorial = [5,4,3,2,1]

#val = functools.reduce(lambda x,y: x*y,factorial)
#print(val)