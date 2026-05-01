# Python-Zero-to-Hero-Notes

# PYTHON PROGRAMMING 
# Practiced by Fahim Ullah 
## What is Programming? 
Programming is a way for us to tell computer what to do. So computer is a dumb 
machine and it only does what we tell it to do. 
## What is Python? 
Python is a dynamically typed, general purpose programming language that supports an 
object-oriented programming approach as well as functional programming approach. 
Python is an interpreted and a high-level programming language. 
It was created by Guido Van Rossum in 1989. 
Features of Python.   
Python is simple and easy to understand. 
It is interpreted and platform-independent which makes debugging very easy. 
Python is and open-source programming language. 
Python provides very big library support. Some of the popular libraries includes NumPy, 
Tensorflow, Selenium, OpenCV etc. 
It is possible to integrate other programming languages within python. 
## What is Python used for? 
Python is used in Data Visualization to create plots and graphical representations. 
Python helps in Data Analytics to analyze and understand raw data for insights and 
trends. 
It is used in AI and Machine learning to simulate human behavior and to learn from past 
data without hard coding. 
It is used to create web applications. 
It can be used to handle databases. 
It is used in business and accounting to perform complex mathematical operations 
along with quantitative and qualitative analysis. 
## Modules in python 
Module is like a code library which can be used to borrow the code written by somebody 
else in our python program. There are two types of modules in python: 
**1. Built in modules:** These modules are ready to import and use and ships with the 
python interpreter, there is no need to install such modules explicitly. 
**2. External modules:** These modules are imported from a third party file or can be 
installed using a package manager like pip or conda. Since this code is written by 
someone else, we can install different versions of a same module with time. 
```
The pip command
 ```
It can be used as a package manager pip to install a python module. Lets install a 
module called pandas using the following command. 
i.e  
```
pip install pandas
```
Using a module in Python (Usage) 
We use the import sytaz to import a module in Python. Here is an example code: 
i.e  
```
import pandas 
 #Read and work with a file named “words.csv” 
pandas. Read-csv(‘words.csv’)
```
Similarly we can install other modules and look into their documentations for 
usage instructions. We will find ourselved doing this often in the later part of this 
course. 

# Comments, Escape sequence & Print in Python: 
Escape sequences and little bit more about print statement in python. We will 
also throw some light on Escape Sequences. 
 
## 1. Python Comments: 
 
 A comment is a part of the coding file that the programmer does not want to 
execute, rather the programmer uses it to either explain a block of code or to avoid the 
execution of a specific part of code while testing. (Shortcut key comment and 
Uncomment is Ctrl + /), (We can also comment our text when we write it into triple 
quotes (“”” Python is a high level language “””)) 
 
## 2. Single-Line Comments: 
 
 To write a comment just adds a ‘#’ at the start of the line. 
 
 i.e: 
 ```
  #This is a single line comment 
  Print(“This is a print statement”) 
 Output: 
  This is a print statement 
 ```
## 3. Multi-Line Comments: 
 
 To write multi-line comments you can use ‘#’ at each line or you can use the 
multiline string. 
 
 i.e: 
  #It will execute a block of code if a specified condition is true. 
  #If the condition is false then it will execute another block of code. 
   
  ```
  P=7 
  if (P>5); 
     print(“P is greater than 5.”) 
  else; 
     print(“P is not greater than 5”) 
  Output: 
 P is greater than 5. 
 ```
 
## 4. Escape Sequence Characters 
 
 To insert characters that cannot be directly used in a string, we use an escape 
sequence character. An escape sequence character is a backlash \ followed by the 
character you want to insert. 
 
 An example of a character that cannot be directly used in a string is a double 
quote inside a string that is surrounded by double quotes:  
If we want make a new line in the text of our program then we can use \n. 
i.e 
```
Print (“This boy is working very hard may \n Almighty Allah blessed him 
long life and prosperity”) 
output: 
This boy is working very hard may  
Almighty Allah blessed him long life and prosperity
```
Moreover if we want to add a specific text in double colon in the text of our 
program. For example: 
i.e 
```
Print(“This boy is working very hard may \”Almighty Allah\” blessed him 
long life and prosperity”) 
output: 
This boy is working very hard may “Almighty Allah” blessed him long life 
and prosperity 
```
## 5. More on Print statement 
The syntax of a print statement looks something like this: 
i.e: 
print(object(s), sep=separator, end=end, file=file, flush=flush) 

## 6. Other Parameters of Print Statement: 
**a. objects(s):** Any object, and as many as you like, will be converted to string 
before printed. <br />
**b. sep=’seperator’:** Specify how to separate the objects, if there is more than 
one. Default is ‘ ‘ <br />
**c. end=’end’:** Specify what to print at the end. Default is \n (line feed) <br />
**d. file:** An object with a write method. Default is sys.stdout <br />
Parameter 2 to 4 are optional.

## 7. Variables and Data Types: 
Variables is like a container that holds data. Very similar to how our container in 
kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory 
and assigning it some value. In Python its as easy as writing. <br />
a = 1 <br />
b = True <br />
c = “Marry” <br />
d = None <br />
These are four variables of different data types. 
## 9. What is a Data Type? 
Data Type specifies the type of value a variable holds. This is required in 
programming to do various operations without causing an error. <br />
In python, we can print the type of any operator using type function: <br />
 ```
 a = 1 
 print(type(a)) 
 b = “1” 
 print(type(b))
```
 By default python provides the following built-in types: 
 
 ### a. Numeric data: int, float, complex
```   
  int: 3, -8, 0 
  float: 7.349, -9.0, 0.00000001 
  complex: 6 =2i
```
 
 ### b. Text data: Str 
 
  Str: “Hello World!!!!!”, “Python Programming” 
 
### c. Boolean data: 
 
  Boolean data consists of values True or False 
 
### e. Sequenced data: list, tuple 
**List:** A list is an ordered collection of data with elements separated by a 
comma and enclosed within square brackets. Lists are  
mutable (changeable) and can be modified after creation 
 
i.e  
```
 list1 = [8, 2.3, [-4, 5], [“apple”, “banana”]] 
 print(list1) 
 output: 
 [8, 2, 3, [-4, 5]], [“apple”, ‘banana’’]]
```
 
**Tuple:** A tuple is an ordered collection of data with elements separated by 
a comma and enclosed within parentheses. Tuples are immutable (non changeable) and cannot be modified after creation.  
 
i.e 
 tuple1 = ((“parrot”, “sparrow”), (“Lion”, “Tiger”)) 
 
## 10. Mapped data: dict (Dictionary) 
dict: A dictionary is an unordered collection of data containing a key:value pair. The 
key:value pairs are enclosed within curly brackets. 
 i.e 
 ``` dict1 = {“name”: “Gull”, “age”: 28, “canVote”: True} 
  Print(dict1) 
 Output 
  {‘name’: ‘Gull’, ‘age’: 28, ‘canVote’: True}
```
## 11. Operators: 
Python has different types of operators for different operations. To create a calculation 
we require arithmetic operators. 
 
 **Arithmetic operators:**   
| Attempt | #1 | #2 | #3 | #4 | #5 | #6 | #7 | #8 | #9 | #10 | #11 | #12 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Seconds | 301 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269 | 254 |
 
Exercise 
My first code "Fahim Ullah" 
a = 25 
b = 7 
ans1 = a+b 
print("Addition of",a,"and",b,"is",ans1) 
ans1 = a-b 
print("Subtraction of",a,"and",b,"is",ans1) 
ans1 = a*b 
print("Multiplication of",a,"and",b,"is",ans1) 
ans1 = a/b 
print("Division of",a,"and",b,"is",ans1) 
ans1 = a**b 
print("Exponent of",a,"and",b,"is",ans1) 
ans1 = a%b 
print("Modulus of",a,"and",b,"is",ans1) 
ans1 = a//b 
print("Floor Division of",a,"and",b,"is",ans1) 
 
Output 
Addition of 25 and 7 is 32 
Subtraction of 25 and 7 is 18 
Multiplication of 25 and 7 is 175 
Division of 25 and 7 is 3.5714285714285716 
Exponent of 25 and 7 is 6103515625 
Modulus of 25 and 7 is 4 
Floor Division of 25 and 7 is 3 
 
12. Typecasting in Python: 
The conversion of one data type into the other data type is known as type casting in 
python or type conversion in python. 
Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), 
hex(), oct(), tuple(), set(), list(), dict() etc for the type casting in python. 
 
 Two types of Typecasting: 
a. Explicit conversion (Explicit type casting in python) 
Operators Operators Name Example 
+ Addition 15+7 - Subtraction 15-7 
* Multiplication 15*7 
** Exponential 15**7 
/ Division 15/7 
% Modulus 15%7 
// Floor Division 15//7 
b. 
Practiced by Fahim Ullah 
Implicit conversion (implicit type casting in python) 
a. 
Explicit typecasting: 
The conversion of one data type into another data type, done via developer or 
programmer’s intervention or manually as per the requirement, is known as 
explicit type conversion. 
It can be achieved with the help of Python’s built-in type conversion functions 
such as int(), float(), hex(), oct(), str() etc. 
Example 1 of explicit typecasting: 
a = "15" 
b = 8 
tcastingofstr = int(a) 
sum = tcastingofstr + b 
print("The Sum of both the numbers is: ", sum) 
Output 
The Sum of both the numbers is:  23 
Example 2 of explicit typecasting: 
a = "15" 
b = 8 
print("The Sum of both the numbers is: ", int(a) + b) 
output 
The Sum of both the numbers is:  23 
b. 
Implicit typecasting: 
Data types in Python do not have the same i.e ordering of data types in not the 
same in Python. Some of the data types of higher-order and same in Python. 
Some of the data types have higher-order, and some have lower order. While 
performing any operations on variables with different data types in Python, one of 
the variable’s data types will changed to the higher data type. According to the 
level, one data type is converted into other by Python interpreter itself 
(automatically). This is called, implicit typecasting in python. 
Python converts a smaller data type to a higher data type of prevent data loss. 
5 of 17 
Practiced by Fahim Ullah 
 
6 of 17 
Example of implicit typecasting: 
 
a = 15 
b = 8 
c = a + b 
print(c) 
print(type(c)) 
 
a = 15.8 
b = 8 
c = a + b 
print(c) 
print(type(c)) 
 
a = 99.9 
b = 8 
c = a + b 
print(c) 
print(type(c)) 
 
output: 
23 
<class 'int'> 
23.8 
<class 'float'> 
107.9 
<class 'float'> 
 
  
  
Practiced by Fahim Ullah 
 
7 of 17 
Taking User Input in Python: 
 
In python, we can take user input directly by using input() function. This input function 
gives a return value as string / character hence we have to pass that into a variable. 
 
 Syntax: 
  Variable=input() 
 
But input function returns the value as string. Hence we have to typecast them 
whenever required to another datatype. 
 
 Example: 
  Variable=int(input()) 
  Variable=float(input()) 
 
We can also display a text using input function This will make input() function take user 
input and display a message as well. 
 
 Example: 
a = input("Enter the first number:" ) 
b = input ("Enter the second number:" ) 
c = int(a) + int(b) 
print("The addition of your two numbers is:", c) 
c = int(a) - int(b) 
print("The subtraction of your two numbers is:", c) 
c = int(a) * int(b) 
print("The multiplication of your two numbers is:", c) 
c = int(a) / int(b) 
print("The divition of your two numbers is:", c) 
c = int(a) % int(b) 
print("The exponential of your two numbers is:", c) 
c = int(a) // int(b) 
print("The floor division of your two numbers is:", c) 
 
Output: 
 
The addition of your two numbers is: 777 
The subtraction of your two numbers is: 309 
The multiplication of your two numbers is: 127062 
The division of your two numbers is: 2.3205128205128207 
The exponential of your two numbers is: 75 
The floor division of your two numbers is: 2 
 
  
What are strings ? 
Practiced by Fahim Ullah 
In Python, anything that you enclosed between single or double quotation marks is 
considered a string. A string is essentially a sequence or array of textual data. Strings 
are used when working with Unicode characters. 
Example 
Name = “Harry” 
Print(“Hello, ” + Name) 
Output 
Hello, Harry 
Note: It does not matter whether you enclose your strings in single or double quotes, the 
output remains the same. 
Sometimes, the user might need to put quotation marks in between the strings. 
Example, consider the sentence: He said, “I want to eat an apple”. 
How will you print this statement in python?: He said, “I want to eat an apple”. We will 
definitely use single quotes for convenience.  
Multiline strings : 
If our strings has multiple lines, we can create them like this: 
Example: 
Assalamualaikum, Everybody my name is FahimUllah. I am a permanent dweller of 
Distt Peshawar. In fact I am a Muslim, and being a Muslim I pray to Almighty Allah to 
forgive all my sins, moreover may Almighty Allah makes me as just like he wants. May 
Almighty Allah blessed me to worship Him, and I intend myself to obey all the principles 
of Islam whether my heart and brain accepts or not. 
a="""Assalamualaikum,  
Everybody my name is FahimUllah.  
I am a permanent dweller of Distt Peshawar.  
In fact I am a "Muslim", and being a Muslim I pray to  
"Almighty Allah" to forgive all my sins, moreover may  
"Almighty Allah" makes me as just like he wants.  
May Almighty Allah blessed me to worship Him, and  
I intend myself to obey all the principles of Islam  
whether my heart and brain accepts or not.""" 
print(a) 
Output:  
Assalamualaikum,  
Everybody my name is FahimUllah.  
I am a permanent dweller of Distt Peshawar.  
In fact I am a "Muslim", and being a Muslim I pray to  
"Almighty Allah" to forgive all my sins, moreover may  
"Almighty Allah" makes me as just like he wants.  
May Almighty Allah blessed me to worship Him, and  
I intend myself to obey all the principles of Islam  
whether my heart and brain accepts or not. 
8 of 17 
Practiced by Fahim Ullah 
 
9 of 17 
 Accessing Characters of a string: 
In Python, string is like an array of characters. We can access parts of string by 
using its index which starts from 0.  
Square brackets can be used to acces elements of the string. 
 
 i.e 
  print(name[0]) 
  print(name[1]) 
 
Looping through the string 
We can loop through strings using a for loop like this: 
 
 i.e 
  for character in name: 
   print(character) 
 
 The above code prints all the characters in the string name one by one 
 
String slicing & Operations on String: 
 
Length of a String: We can find the length of string using len() function. 
 
Example: 
  fruit= “Mango” 
len1= len(fruit) 
print(“Mango is a”, len1, “letter word.”) 
 
 Output: 
  Mango is a 5 letter word. 
 
 String as an array 
  
 A string is essentially a sequence of characters also called an array, thus we can   
 access the elements of this array. 
 
 Example:  
  Pie = “ApplePie” 
  print(pie[:5]) 
  print(pie[6]) #returns character at specified index 
 
 Output: 
  Apple 
  i 
 
Note: This method of specifying the start and end index to specify a part of a 
string s called slicing. 
 
 
 
 
Practiced by Fahim Ullah 
 
10 of 17 
Slicing Example: 
 
Pie = “ApplePie” 
print(pie[:5])  #Slicing from the start  
print(pie[5:])  #slicing till end 
print(pie[2:6])  #slicing in between 
print(pie[-8])  #slicing using negative index 
 
Output; 
 Apple 
 Pie 
 pleP 
 ApplePie 
 
Example 2: 
 
a = "ghaazi" 
print(a[0:6]) 
print(a[:6]) 
print(a[0:]) 
print(a[1:6]) 
print(a[-2:]) 
print(a[:-2]) 
print("-------------------") 
pie = "Fahimkhan" 
print(pie[:5])      #Slicing from the start  
print(pie[5:])      #slicing till end 
print(pie[2:6])     #slicing in between 
print(pie[-8])      #slicing using negative index 
 
Output: 
ghaazi 
ghaazi 
ghaazi 
haazi 
zi 
ghaa ------------------- 
Fahim 
khan 
himk 
a 
 
 
  
Practiced by Fahim Ullah 
 
11 of 17 
Loop through a String: 
 
Strings are arrays and arrays are iterable. Thus we can loop through strings. 
 
Example: 
 alphabets = “ABCDE” 
 for i in alphabets: 
  print(i) 
 
Output: 
 A 
B 
C 
D 
E 
 
String Methods: 
 
Python provides a set of built-in methods that we can use to alter and modify the 
strings. 
 
 upper(): 
  The upper() method converts string to upper case. 
 
 Example: 
  Str1 = “AbcDef” 
  print(str1.upper()) 
 
 Output: 
  ABCDEF 
 
 lower() 
  The lower() method convert a string to lower case 
  
 Example: 
  str1 = “AbcDef” 
  print(str1.lower()) 
 
rstrip() : 
 
The rstrip() removes any trailing characters. It will removes only the characters after out 
text in our program not before characters. 
 
 i.e 
  str3 = “Hello !!!!” 
  print(str3.rstrip(“!”))    
Output: 
 Hello 
 
  
Practiced by Fahim Ullah 
 
12 of 17 
replace() : 
 
The replace() method replaces all occurrences of a string with another string. 
 
 i.e 
  str2 = “Silver Spoon” 
  print(str2.replace(“Sp” , “M”)) 
 
 Output: 
  Silver Moon 
 
split() : 
 
The split() method splits the given string at the specified instance and returns the 
separated strings as list items. 
 
 Example : 
   str2 = “Silver Spoon” 
   print(str2.split(“ “)) #Its splits the string at the whitespace. 
 
 Output: 
   [‘Silver’, ‘Spoon’] 
There are various other string methods that we can use to modify 
our strings. 
 
capitalize() : 
 
The capitalize() method turns only the first character of the string to uppercase and the 
rest other characters of the string are turned to lowercase. The string has no effect if the 
first character is already uppercase. 
 
 i.e 1 
  str1 = “hello” 
  print(str1.capitalize()) 
 
 Output : 
  Hello 
 
 i.e  
  str1 = “hello” 
  capstr1 = str1.capitalize() 
  print(capstr) 
  str2 = “hello world” 
  capstr2 = str2.capitalize() 
  print(capstr2) 
 
 Output : 
  Hello 
  Hello world 
 
Practiced by Fahim Ullah 
 
13 of 17 
 
center() : 
  
The center() method aligns the string to the center as per the parameters given by the 
user. 
 
 i.e 1 : 
  str1 = “welcome to the console!!!” 
  print(str1.center(50)) 
 
 Output : 
   Welcome to the console!!! 
  
We can also provide padding character. It will fill the rest of the fill characters 
provided by the user. 
 
i.e 2 : 
  str1 = “welcome to the console!!!” 
  print(str1.center(50, “.”)) 
 
Output : 
  …………….welcome to the console!!!............... 
 
count() : 
 
The count() method returns the number of times the given value has occurred within the 
given string. 
 
 i.e 
  str2 = “AbdulSalam” 
  countStr = str2.count(“a”) 
  print(countStr) 
 
 Output : 
 
  3 
 
endswith() : 
 
The endswith() method checks if the string ends with a given value. If yes then return 
True, else return False. 
 
 i.e 
  str1 = “welcome to the Console !!!” 
  print(str1.endswith(“!!!”)) 
  
Output : 
 True 
 
Practiced by Fahim Ullah 
 
14 of 17 
We can even also check for a value in-between the string by providing start and 
end index positions. 
 
i.e 
 str2 = “welcome to the console !!!” 
 print(str2.endswith(“to”, 4, 10)) 
 
Output: 
 True 
 
find() :  
 
The find() method searches for the first occurrence of the given value and returns the 
index where it is present. It given value is absent from the string then return -1. 
 
 i.e 
  str1 = “He’s name is Dan. He is an honest man.” 
  Print(str1.find(“is”))  
 
 Output : 
   10 
 
Index() : 
 
The index() method searches for the first occurrence of the given value and returns the 
index where it is present. If given value is absent from the string then it raise and 
exception. 
 
 i.e : 
  str1 = “He’s name is Dan. Dan is an honest man.” 
  Print(str1.index(“Dan”)) 
 
 Output: 
  13 
 
As we can see, this method is somewhat similar to the find() method. The major 
difference being that index() raises an exception if value is absent whereas find() 
does not.  
 
i.e: 
  str1 = “He’s name is Dan. Dan is an honest man.” 
  Print(str1.index(“Daniel”)) 
 
 Output: 
  ValueError: substring not found 
 
  
Practiced by Fahim Ullah 
 
15 of 17 
isalnum() : 
 
The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. 
If any other characters or punctuations are present, then it returns False. 
 
 i.e : 
  str1 = “WelcomeToTheConsole” 
  print(str1.isalnum()) 
 
 Output: 
  True 
 
isalpha(): 
 
The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If 
any other characters or punctuation or number (0-9) are present, then it returns False. 
 
 i.e: 
  str1 = “Welcome” 
  print(str1.isalpha()) 
  
 Output: 
   True 
 
islower() : 
 
The islower() method returns True if all the characters in the string are in lower case, 
else it returns False. 
 
 i.e: 
  str1 = “hello world” 
  print(str1.islower()) 
 
 Output : 
   True 
 
Isprintable() : 
 
The isprintable() method returns True if all the values whithin the given string are 
printable, if not then returns False. 
 
 i.e 1: 
  str1 = “We wish you a happy Eid Mubarrak” 
  print(str1, isprintable()) 
 
 Output: 
   True 
 i.e 2 : 
  str1 = “We wish you a happy Eid Mubarrak \n” 
  print(str1, isprintable()) 
  
 Output: 
   False  
  
Practiced by Fahim Ullah 
 
16 of 17 
Isspace() : 
 
The isspace() method returns True only and only if the string contains white spaces, 
else returns False. 
 
 i.e : 
  str1 = “          ”  #Using spacebar 
  print(str1.isspace()) 
  str2 = “ ”  #Using Tab 
  print(str2.ispace())  
 
 Output : 
   True 
   True 
 
Istitle() : 
 
The istitle() returns True only if the first letter of each word of the string is captalized, 
else it returns False. 
 
 i.e : 
  str1 = “World Health Organization” 
  print(str1.istitle()) 
 
 Output : 
   True 
 
 i.e 2 : 
  str2 = “To kill a Mocking bird” 
  print(str2.istitle()) 
 
 Output : 
   False           
 
Isupper() : 
 
The isupper() method returns True if all the characters in the string are upper case, else 
it returns False. 
 
 i.e: 
  str1 = “WORLD HEALTH ORGANIZATION” 
  print(str1.isupper()) 
 
 Output: 
   True 
 
  
Startswith() : 
Practiced by Fahim Ullah 
The startswith() method checks if the string starts with a given value. If yes then return 
True, else return False. 
i.e. 
str1 = “Python is a Interpreted Language” 
print(str1.startwith(“Python”)) 
Output : 
swapcase()  
True 
The swapcase() method changes the character casing of the string, Upper case and 
converted to lower case to upper case. 
i.e : 
str1 = “Python is a Interpreted Language” 
print(str1.swapcase()) 
Output: 
title() : 
pYTHON IS A iNTERPRETED lANGUAGE 
The title() method captalizes each letter of the word within the string. 
i.e: 
str1 = “He’s name is Dan. Dan is an honest man.” 
Print(str1.title()) 
Output : 
He’s Name Is Dan. Dan Is an Honest Man. 
17 of 17 

