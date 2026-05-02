<h1 align="center">Python-Zero-to-Hero-Notes </h1>
<h1 align="center"> PYTHON PROGRAMMING </h1>
<h3 align="right"> Practiced by Fahim Ullah </h3>

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
else in our python program. There are two types of modules in python: </br>
**1. Built in modules:** These modules are ready to import and use and ships with the 
python interpreter, there is no need to install such modules explicitly. </br> 
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
 
### 1. Python Comments: 
 
 A comment is a part of the coding file that the programmer does not want to 
execute, rather the programmer uses it to either explain a block of code or to avoid the 
execution of a specific part of code while testing. (Shortcut key comment and 
Uncomment is Ctrl + /), (We can also comment our text when we write it into triple 
quotes (“”” Python is a high level language “””)) 
 
### 2. Single-Line Comments: 
 
 To write a comment just adds a ‘#’ at the start of the line. 
 
 i.e: 
 ```
  #This is a single line comment 
  Print(“This is a print statement”) 
 Output: 
  This is a print statement 
 ```
### 3. Multi-Line Comments: 
 
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
 
### 4. Escape Sequence Characters 
 
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
### 5. More on Print statement 
The syntax of a print statement looks something like this: 
i.e: 
print(object(s), sep=separator, end=end, file=file, flush=flush) 

### 6. Other Parameters of Print Statement: 
**a. objects(s):** Any object, and as many as you like, will be converted to string 
before printed. <br />
**b. sep=’seperator’:** Specify how to separate the objects, if there is more than 
one. Default is ‘ ‘ <br />
**c. end=’end’:** Specify what to print at the end. Default is \n (line feed) <br />
**d. file:** An object with a write method. Default is sys.stdout <br />
Parameter 2 to 4 are optional.

### 7. Variables and Data Types: 
Variables is like a container that holds data. Very similar to how our container in 
kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory 
and assigning it some value. In Python its as easy as writing. <br />
a = 1 <br />
b = True <br />
c = “Marry” <br />
d = None <br />
These are four variables of different data types. 
### 8. What is a Data Type? 
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
 
### d. Sequenced data: list, tuple 
**List:** A list is an ordered collection of data with elements separated by a 
comma and enclosed within square brackets. Lists are mutable (changeable) and can be modified after creation </br>
 
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
 
### 9. Mapped data: dict (Dictionary) 
dict: A dictionary is an unordered collection of data containing a key:value pair. The 
key:value pairs are enclosed within curly brackets. 
 i.e 
 ``` dict1 = {“name”: “Gull”, “age”: 28, “canVote”: True} 
  Print(dict1) 
 Output 
  {‘name’: ‘Gull’, ‘age’: 28, ‘canVote’: True}
```
### 10. Operators: 
Python has different types of operators for different operations. To create a calculation 
we require arithmetic operators. 
 
 **Arithmetic operators:**   
| Operators | Operators Name | Example |
| :---: | :---: | :---: |
| + | Addition | 15+7 |
| - | Subtraction | 15-7 |
| * | Multiplication | 15*7 |
| ** | Exponential | 15**7 |
| / | Division | 15/7 |
| % | Modulus | 15%7 |
| // | Floor Division | 15//7 |

**Exercise** 
```
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
```
 
## 11. Typecasting in Python: 
The conversion of one data type into the other data type is known as type casting in 
python or type conversion in python. <br />
Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), 
hex(), oct(), tuple(), set(), list(), dict() etc for the type casting in python. 
 
 Two types of Typecasting: 
a. Explicit conversion (Explicit type casting in python) <br />
b. Implicit conversion (implicit type casting in python) <br />
### a. Explicit typecasting: 
The conversion of one data type into another data type, done via developer or 
programmer’s intervention or manually as per the requirement, is known as 
explicit type conversion. 
It can be achieved with the help of Python’s built-in type conversion functions 
such as int(), float(), hex(), oct(), str() etc. <br />
Example 1 of explicit typecasting: 
```
a = "15" 
b = 8 
tcastingofstr = int(a) 
sum = tcastingofstr + b 
print("The Sum of both the numbers is: ", sum) 
Output 
The Sum of both the numbers is:  23
```
Example 2 of explicit typecasting: 
```
a = "15" 
b = 8 
print("The Sum of both the numbers is: ", int(a) + b) 
output 
The Sum of both the numbers is:  23
```
### b. Implicit typecasting: 
Data types in Python do not have the same i.e ordering of data types in not the 
same in Python. Some of the data types of higher-order and same in Python. 
Some of the data types have higher-order, and some have lower order. While 
performing any operations on variables with different data types in Python, one of 
the variable’s data types will changed to the higher data type. According to the 
level, one data type is converted into other by Python interpreter itself 
(automatically). This is called, implicit typecasting in python. <br />
Python converts a smaller data type to a higher data type of prevent data loss. <br />

Example of implicit typecasting: 
``` 
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
```
## Taking User Input in Python: 
 
In python, we can take user input directly by using input() function. This input function 
gives a return value as string / character hence we have to pass that into a variable. 
``` 
 Syntax: 
  Variable=input()
```
 
But input function returns the value as string. Hence we have to typecast them 
whenever required to another datatype. <br />
**Example:** 
 ```
 Variable=int(input()) 
 Variable=float(input())
```
 
We can also display a text using input function This will make input() function take user 
input and display a message as well. 
 
 Example: 
 ```
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
```
  
## What are strings ? 
In Python, anything that you enclosed between single or double quotation marks is 
considered a string. A string is essentially a sequence or array of textual data. Strings 
are used when working with Unicode characters. </br>
**Example** 
```
Name = “Fahim” 
Print(“Hello, ” + Name) 
Output 
Hello, Fahim
```
**Note:** It does not matter whether you enclose your strings in single or double quotes, the 
output remains the same. </br>
Sometimes, the user might need to put quotation marks in between the strings. 
Example, consider the sentence: He said, “I want to eat an apple”. </br>
How we can print this statement in python?: He said, “I want to eat an apple”. We will 
definitely use single quotes for convenience.  
### Multiline strings : 
If our strings has multiple lines, we can create them like this: </br>
**Example:** </br>
Assalamualaikum, Everybody my name is FahimUllah. I am a permanent dweller of 
Distt Peshawar. In fact I am a Muslim, and being a Muslim I pray to Almighty Allah to 
forgive all my sins, moreover may Almighty Allah makes me as just like he wants. May 
Almighty Allah blessed me to worship Him, and I intend myself to obey all the principles 
of Islam whether my heart and brain accepts or not. 
```
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
```
### Accessing Characters of a string: 
In Python, string is like an array of characters. We can access parts of string by 
using its index which starts from 0. <br /> 
Square brackets can be used to acces elements of the string. 
 
 **i.e** 
 ```
  print(name[0]) 
  print(name[1])
```
 
### Looping through the string 
We can loop through strings using a for loop like this: </br>
 
 **i.e** 
 ```
  for character in name: 
   print(character)
```
 
 The above code prints all the characters in the string name one by one 
 
### String slicing & Operations on String: 
 
**Length of a String:** We can find the length of string using len() function. 
 
**Example:** 
```
fruit= “Mango” 
len1= len(fruit) 
print(“Mango is a”, len1, “letter word.”) 
 
 Output: 
  Mango is a 5 letter word.
```
 
### String as an array 
  
 A string is essentially a sequence of characters also called an array, thus we can   
 access the elements of this array. </br>
 
 **Example:**  
 ```
  Pie = “ApplePie” 
  print(pie[:5]) 
  print(pie[6]) #returns character at specified index 
 
 Output: 
  Apple 
  i 
 ```
**Note:** This method of specifying the start and end index to specify a part of a 
string s called slicing. 
 
**Slicing Example:** 
``` 
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
``` 
 
**Example 2:** 
``` 
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
ghaa
------------------- 
Fahim 
khan 
himk 
a 
``` 
### Loop through a String: 
 
Strings are arrays and arrays are iterable. Thus we can loop through strings. </br>
 
**Example:**
```
alphabets = “ABCDE” 
  for i in alphabets: 
  print(i) 
 
Output: 
A 
B 
C 
D 
E 
``` 
### String Methods: 
 
Python provides a set of built-in methods that we can use to alter and modify the 
strings. 
 
 **upper():** </br> 
  The upper() method converts string to upper case. </br>
 
 Example:
 ```
  Str1 = “AbcDef” 
  print(str1.upper()) 
 
 Output: 
  ABCDEF
``` 
 
 **lower()** </br>
  The lower() method convert a string to lower case 
  
 Example: 
 ```
  str1 = “AbcDef” 
  print(str1.lower())
```
 
**rstrip() :** </br> 
 
The rstrip() removes any trailing characters. It will removes only the characters after out 
text in our program not before characters. </br>
 
 i.e 
``` 
  str3 = “Hello !!!!” 
  print(str3.rstrip(“!”))    
Output: 
 Hello
```
**replace() :** </br> 
 
The replace() method replaces all occurrences of a string with another string. </br>
 
 i.e 
 ```
  str2 = “Silver Spoon” 
  print(str2.replace(“Sp” , “M”)) 
 
 Output: 
  Silver Moon 
 ```
**split() :** </br> 
 
The split() method splits the given string at the specified instance and returns the 
separated strings as list items. </br>
 
 Example : 
 ```
   str2 = “Silver Spoon” 
   print(str2.split(“ “)) #Its splits the string at the whitespace. 
 
 Output: 
   [‘Silver’, ‘Spoon’]
```
There are various other string methods that we can use to modify 
our strings. </br>
 
**capitalize() :** </br>
 
The capitalize() method turns only the first character of the string to uppercase and the 
rest other characters of the string are turned to lowercase. The string has no effect if the 
first character is already uppercase. </br>
 
 i.e 
 ```
  str1 = “hello” 
  print(str1.capitalize()) 
 
 Output : 
  Hello 
 ```
 i.e  
 ```
  str1 = “hello” 
  capstr1 = str1.capitalize() 
  print(capstr) 
  str2 = “hello world” 
  capstr2 = str2.capitalize() 
  print(capstr2) 
 
 Output : 
  Hello 
  Hello world
``` 
**center() :** </br> 
  
The center() method aligns the string to the center as per the parameters given by the 
user. </br>
 
 i.e 1 : 
 ```
  str1 = “welcome to the console!!!” 
  print(str1.center(50)) 
 
 Output : 
   Welcome to the console!!! 
```  
We can also provide padding character. It will fill the rest of the fill characters 
provided by the user. </br>
 
i.e 2 : 
```
  str1 = “welcome to the console!!!” 
  print(str1.center(50, “.”)) 
 
Output : 
  …………….welcome to the console!!!............... 
 ```
**count() :** </br> 
 
The count() method returns the number of times the given value has occurred within the 
given string. </br>
 
 i.e
 ```
  str2 = “AbdulSalam” 
  countStr = str2.count(“a”) 
  print(countStr) 
 
 Output : 
 
  3 
``` 
**endswith() :** </br> 
 
The endswith() method checks if the string ends with a given value. If yes then return 
True, else return False. </br>
 
 i.e 
 ```
  str1 = “welcome to the Console !!!” 
  print(str1.endswith(“!!!”)) 
  
Output : 
 True 
``` 
 
We can even also check for a value in-between the string by providing start and 
end index positions. </br>
 
i.e 
```
 str2 = “welcome to the console !!!” 
 print(str2.endswith(“to”, 4, 10)) 
 
Output: 
 True 
 ```
**find() :**  </br>
 
The find() method searches for the first occurrence of the given value and returns the 
index where it is present. It given value is absent from the string then return -1. </br>
 
 i.e 
 ```
  str1 = “He’s name is Dan. He is an honest man.” 
  Print(str1.find(“is”))  
 
 Output : 
   10 
``` 
**Index() :** </br> 
 
The index() method searches for the first occurrence of the given value and returns the 
index where it is present. If given value is absent from the string then it raise and 
exception. </br>
 
 i.e : 
 ```
  str1 = “He’s name is Dan. Dan is an honest man.” 
  Print(str1.index(“Dan”)) 
 
 Output: 
  13 
``` 
As we can see, this method is somewhat similar to the find() method. The major 
difference being that index() raises an exception if value is absent whereas find() 
does not.  </br>
 
i.e: 
```
  str1 = “He’s name is Dan. Dan is an honest man.” 
  Print(str1.index(“Daniel”)) 
 
 Output: 
  ValueError: substring not found 
``` 
**isalnum() :** </br> 
 
The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. 
If any other characters or punctuations are present, then it returns False. </br>
 
 i.e :
 ```
  str1 = “WelcomeToTheConsole” 
  print(str1.isalnum()) 
 
 Output: 
  True 
``` 
**isalpha():** </br> 
 
The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If 
any other characters or punctuation or number (0-9) are present, then it returns False. </br>
 
 i.e: 
 ```
  str1 = “Welcome” 
  print(str1.isalpha()) 
  
 Output: 
   True 
``` 
**islower() :** </br> 
 
The islower() method returns True if all the characters in the string are in lower case, 
else it returns False. </br>
 
 i.e: 
 ```
  str1 = “hello world” 
  print(str1.islower()) 
 
 Output : 
   True 
``` 
**Isprintable() :** </br> 
 
The isprintable() method returns True if all the values whithin the given string are 
printable, if not then returns False. </br>
 
 i.e 1:
 ```
  str1 = “We wish you a happy Eid Mubarrak” 
  print(str1, isprintable()) 
 
 Output: 
   True
```
 i.e 2 : 
 ```
  str1 = “We wish you a happy Eid Mubarrak \n” 
  print(str1, isprintable()) 
  
 Output: 
   False  
```   
**Isspace() :** </br> 
 
The isspace() method returns True only and only if the string contains white spaces, 
else returns False. </br>
 
 i.e :
 ```
  str1 = “          ”  #Using spacebar 
  print(str1.isspace()) 
  str2 = “ ”  #Using Tab 
  print(str2.ispace())  
 
 Output : 
   True 
   True 
``` 
**Istitle() :** </br> 
 
The istitle() returns True only if the first letter of each word of the string is captalized, 
else it returns False. </br>
 
 i.e : 
 ```
  str1 = “World Health Organization” 
  print(str1.istitle()) 
 
 Output : 
   True 
 ```
 i.e 2 : 
 ```
  str2 = “To kill a Mocking bird” 
  print(str2.istitle()) 
 
 Output : 
   False           
``` 
**Isupper() :** </br> 
 
The isupper() method returns True if all the characters in the string are upper case, else 
it returns False. </br>
 
 i.e:
 ```
  str1 = “WORLD HEALTH ORGANIZATION” 
  print(str1.isupper()) 
 
 Output: 
   True 
 ```
  
**Startswith() :** </br>  
The startswith() method checks if the string starts with a given value. If yes then return 
True, else return False. </br>
i.e. 
```
str1 = “Python is a Interpreted Language” 
print(str1.startwith(“Python”)) 
Output : 
True
```
**swapcase()** </br>
The swapcase() method changes the character casing of the string, Upper case and 
converted to lower case to upper case. </br>
i.e : 
```
str1 = “Python is a Interpreted Language” 
print(str1.swapcase()) 
Output:
pYTHON IS A iNTERPRETED lANGUAGE
```
**title() :**  </br>
 
The title() method captalizes each letter of the word within the string. </br>
i.e: 
```
str1 = “He’s name is Dan. Dan is an honest man.” 
Print(str1.title()) 
Output : 
He’s Name Is Dan. Dan Is an Honest Man.
```
# Operators, if-else - elif Statements:
### 1.	Logical Operators:
| Category | Operator | Keyword/Symbol | Function | Primary Use Case |
| :---: | :---: | :---: | :---: | :---: |
| **Boolean Logical Operators** |
| Boolean Logic | AND | and | Returns True if both operands are True. | Program control flow 
(e.g., if statements). |
| Boolean Logic | OR | or | Returns True if at least one operand is True. | Program control flow (e.g., if statements). |
| Boolean Logic | NOT | not | Inverts the truth value of the operand (True becomes False). | Program control flow (e.g., if statements). |
| **Bitwise Logical Operators** |
| Bitwise Logic | Bitwise AND | & | Performs logical AND on the individual bits of the integers. | Low-level manipulation, setting/clearing bits, masking. |
| Bitwise Logic | Bitwise OR | ∣ | Performs logical OR on the individual bits of the integers. | Low-level manipulation, combining flags. |
| Bitwise Logic | Bitwise XOR | ^ | Performs logical Exclusive OR on the individual bits. | Swapping numbers without a temporary variable, encryption. |
| Bitwise Logic | Bitwise NOT | ~ | Inverts all the bits of the integer (unary operator). | Advanced number manipulation (less common). |

### 2.	Comparison Operators:
| Operator | Meaning | Example | Result | Analogy |
| :---: | :---: | :---: | :---: | :---: |
| > | Greater than | 10>5 | TRUE | Is your age more than 18? |
| < | Less than | 10<5 | FALSE | Is the temperature less than freezing? |
| == | Equal to | 10==10 | TRUE | Does this key exactly match that lock? |
| != | Not equal to | 10!=5 | TRUE | Is this door different from that window? |
| >= | Greater than or equal to | 10>=10 | TRUE | Can you attend if you are 18 or older? |
| <= | Less than or equal to | 10<=9 | FALSE | Can you carry a bag 5 kg or lighter? |

### 3.	if-else Statements:
   Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path then it would have if the expression had evaluated to True. </br>
   Based on this, the conditional statements are further classified into following types: </br>

(a)	if </br>
(b)	if-else </br>
(c)	if-else-elif </br>
(d)	nested if-else-elif </br>

An if….else statement evaluates like this: </br>

**if the expression evaluates True:** </br>
				Executes the block of code inside if statement. After execution it return to the code out of the if…..else block. </br>

**if the expression evaluates False:** </br>
					Executes the block of code inside else statement. After execution return to the code out of the if…..else block. </br>

**i.e**
```
appleprice = 210
budget = 205
if (appleprice <= budget):
  print(“Alexa, add 1 kg Apples to the cart.”)
else:
  print(“Alexa, do not add Apples to the cart.”)
	
Output:
		Alexa, do not add Apples to the cart.
```

### 4.	elif Statements:
Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement. </br>

**Working on an elif Statement:** </br>
Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block. </br>
Execute the block of code inside the first elif statement if the expression inside if evaluates True. After execution return to the code out of the if block. </br>
Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block. </br>
**.** </br>
**.** </br>
**.** </br>
**.** </br>
**.** </br>
**.** </br>
Execute the block of code inside the nth elif statement if the expression inside if evaluates True. After execution return to the code out of the if block. </br>

 
**i.e:**
```
num = 0
if (num < 0):
		print(“Number is negative.”)
elif (num == 0):
		print(“Number is Zero.”)
elif (num >= 1000):
		print(“Number reaches thousand figure”)
else:
		print(“Number is positive.”)
print(“Python Programming”)

Output
	Number is Zero.
	Python Programming
```

### 5.	Nested if Statements:
We can use it, if-else, elif statements inside other if statements as well. </br>
	
**i.e:**	
```
num = 18
if (num < 0):
  print(“Number is negative.”)
elif (num > 0):
	if (num <= 10):
		print(“Number is between 1 to 10.”)
	elif (num > 10 and num <= 20):
		print(“Number is between 11 to 20.”)
 	else:
		print(“Number is greater than 20.”)
else:
	print(“Number is zero.”)
print(Python Programming)

		Output:
			
			Number is between 11 to 20.
			Python Programming
```
### Practicing Python Programming 1:
```
Stdname = input("Write the name of a person")
Substudied = input("Which subject he Studied")
qulifyexam = int(input("Write the qualification"))
Marksobt = int(input("Write the Persentage"))
if (qulifyexam < 14):
    print(Stdname, "may be eligible for the job but needs to focus on the skill")
elif (qulifyexam == 14):
    print(Stdname, "qualified the Bechelor program in the field of" , Substudied)
    if (Marksobt >= 70):
          print ("He is eligible for the job")
    elif (Marksobt >= 80):
          print("He is perfect for the job")
    elif (Marksobt > 60 & Marksobt < 70):
         print ("He may get the job but he needs to work hard for getting experience")
elif (qulifyexam == 16):
    print(Stdname, "qualified the Bechelor program in the field of" , Substudied)
    if (Marksobt >= 70):
          print ("He is eligible for the job")
    elif (Marksobt >= 80):
          print("He is perfect for the job")
    elif (Marksobt > 70):
         print ("He may get the job but he needs to work hard for getting experience")
elif (qulifyexam > 16):
     print(Stdname, "qualified M-Phil or PHD in the field of", Substudied)
     print("He need not to apply for any job, whereas the job itself coming towards", Stdname)
else:
     print("I just practicing Python programming.......")

Output:

    Ali Raza qualified the Bechelor program in the field of Artifical Intelligence
    He is eligible for the job
    I just practicing Python programming………
```


 
### Practicing Python Programming 2:
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you: </br>
import time </br>
timestamp = time.strftime(‘%H:%M:%S’) </br>
print(timestamp) </br>
timestamp = time.strftime(‘%H’) </br>
print(timestamp) </br>
timestamp = time.strftime(‘%M’) </br>
print(timestamp) </br>
timestamp = time.strftime(‘%S’) </br>
print(timestamp) </br>

**Practice 1:**
```
import time
tmst = time.strftime("%H:%M:%S")
tmst1 = int(time.strftime("%H"))
tchname = input("Write the name of teacher")
if (tmst1 >= 5) & (tmst1 < 9):
     print("Good Morning Sir :", tchname)
elif (tmst1 >= 9) & (tmst1 < 16):
     print("Good Afternoon Sir :", tchname)
elif (tmst1 >= 16) & (tmst1 < 20):
     print("Good Evening Sir:", tchname)
elif (tmst1 >= 20):
     print("Good Night Sir:", tchname)


Output:

Good Night Sir: Abdul Salam
```
# Match Cases, Loops, range(), break & Continue Statements:
### 1.	Match Cases:
To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. It’s like a C, C#, C++ or Java like language, you must have heard of switch-case statements. </br>
A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present pattern until it fits into one. </br>
The match case consists of three main entities: </br>
	
1.	The match keyword </br>
2.	One or more case clauses </br>
3.	Expression for each case </br>

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches. </br>

**i.e 1:**
```
	x = 4								# x is the variable to match
	match x:
		case 0:							#if x is 0
			print(“x is zero”)
		case 4 if x % 2 == 0:
			print(“x % 2 == 0 and case is 4”)	
		case_ if x < 10:
			print(“x is < 10”)			#default case will only be matched if the above cases were not matched. So its basically just like else statement.
		case_:							
			print(x)
	Output:
			x % 2 == 0 and case is 4
```			
**i.e 2:**
```
x = int(input("Write your number.."))
match x:
     case _ if x == 0:
        print("x value is equal to :", x)
     case _ if x > 50:
        print("x value is smaller than :", x+1)
     case _ if x == 49:
        print("x value is equal to :", x)
     case _:
        print(x)

Output:

    x value is smaller than : 12135465647
```
### 2.	Loops in python:
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following types; for loop, while loop, nested loops. 

**1.	for Loop:**
for loops can iterate over a sequence of iterable ojects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries. </br>

**Example: iterating over a string:**
```		
name = “Gulkhan”
for i in name:
	print(I, end=”, “)

Output:
	G,u,l,k,h,a,n,
```
**Example: iterating over a list:**
```	
Colors = [“Red”, “Green”, “Blue”, “Yellow”]
for x in colors:
	print(x)

Output:
		Red
		Green	
		Blue
		Yellow
```		
Similarly we can use loops for list, sets and dictionaries. </br>
**i.e**
```
name = ["Red", "Blue", "Green", "Yellow"]
for i in name:
    print(i)
    for x in i:
        print(x,end="\n")

Output:

Red
R
e
d
Blue
B
l
u
e
Green
G
r
e
e
n
Yellow
Y
e
l
l
o
w
```
### 2.	while loop in python:
As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop. </br>
		
**Example 1:**
```
Count = 5			
While (count > 0):
	Print(count)
	Count = count -1

Output:
		5
		4
		3
		2
		1 
```
Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.

**Example 2:**
```
x=int(input("Write the Number.."))
while (x <= 7):
    print(x)
    x=x+1

Output:
    1
    2
    3
    4
    5
    6
    7
```

**4.	Else with While loop:**
We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

**Example:**
```
x = 5
while (x > 0):
	print(x)
	x = x-1
else:
	print(“I am inside else statement”)
	
Output:
		5
		4
		3	
		2
		1
		I am inside else statement
```

### 5.	Do-While loop in python:
do-while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop’s body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop. </br>
**How to emulate do while loop in python?** </br>
To create a do while loop in python, we need to modify the while loop a bit in order to get similar behaviors to a do while loop. </br>
The most common technique to emulate a do-while loop in Python is to use n infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true: </br>

**Example 1:**
```
while True:
	number = int (input(“enter a positive number: ”))
	print(number)
	if not number > 0:
		break

Output:
	Enter a positive number: 1
	1
	Enter a positive number: 4
	4
	Enter a positive number: -1
	-1
```	
**Explanation:** </br>
This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path.
			
**Example 2:**	
```
x=int(input("Write a number.."))
while (x >= 7):
    print(x)
    x=x+1
    if x >= 15:
        break

Output:
    8
    9
    10
    11
    12
    13
    14
```
### 3.	range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times ?
Here, we can use the range() function. </br>

**Example:1**
```		
for k in range(5):
	print(k)
	
Output:
		0
		1
		2	
		3
		4
```	
**Example:2** 
```		
for k in range(5):
	print(k+1)
	
Output:
		1		
		2	
		3
		4
		5
```
**Example:3**
```			
for k in range(4,9):
	print(k)

Output:
		4
		5	
		6	
		7
		8
```
If we use three numbers in range() method as mentioned in below example:
```
for x in range(5, 19, 3):
   print(x)

Output:
        5
        8
        11
        14
        17
```  
### 4.	break Statement:
The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within. </br>
**i.e**
```
for i in range(1, 101, 1):
	print(i ,end=” “)
	if(i==50):
		break
	else:
		print(“Mississippi”)
print(“Thank you”)

	Output:

	1 Mississippi
	2 Mississippi
	3 Mississippi
	4 Mississippi
	5 Mississippi 
	.
	.	
	.
	.
	50 Mississippi 
```
### 5.	Continue Statement
The continue statement skips the rest of the loop statements and causes the next iteration to occur. </br>
**i.e**
```
for i in [2,3,4,5,6,8,0]:
	if (i%2!=0):
		continue
		print(i)


Output

		2
		4
		6
		8	
		0
```
**Example of continue & break statements:**
```
for i in range(1, 21):
    if i == 10:
       print("Here continue statement starts its working")
       continue
   print("2 x", i, "=", 2*i)
   if i== 15:
       print("Here break statement starts its working")
       break

Output:

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
Here continue statement starts its working
2 x 11 = 22
2 x 12 = 24
2 x 13 = 26
2 x 14 = 28
2 x 15 = 30
Here break statement starts its working
```
# Python Functions, Arguments:
### 1.	Python Functions:
A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat. </br>
There are two types of functions: </br>
1.	Built-in functions </br>
2.	User-defined functions </br>

**1.	Built-in functions:** </br>
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows. </br>
		min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(),
		set(), print(), etc.

**2.	User-defined functions:** </br>
We can create functions to perform specific tasks as per out needs. Such functions are called user-defined functions. </br>		Syntax: </br>
```
def function_name(parameters):
	pass
# Code and statements
```
(a)	Create a function using the def keyword, followed by a function name, followed by a parenthesis (()) and a colon(:). </br>
(b)	Any parameters and arguments should be placed within the parentheses. </br>
(c)	Rules to naming function are similar to that of naming variables. </br>
(d)	Any statements and other code within the function should be indented. </br>

### Calling a function:
We call a function by giving the function name, followed by parameters (if any), in the parenthesis.	

**i.e**
```
			def name(fname, lname):
				print(“Hello, ”, fname, lname)	
			name(“Abdul”, “Salam”)

		Output:
			Hello, Abdul Salam		
```
**Example:** 
```
def solutionof(name, obtmarks, Totalmarks):
    solution = (obtmarks/Totalmarks) * 100
    print(name, "got percentage =", solution,"% Marks")

a = input("Enter the name of Student")
b = int(input("Enter the total marks obtained by :"))
c = int(input("Enter the total marks"))
solutionof(a,b,c)

Output:
Fahim Ullah got percentage = 79.52380952380952 % Marks
```

### 2.	Function Arguments and return Statement:
Here are four types of arguments that we can provide in a function: </br>
	(a).	Default Arguments </br>
	(b).	Keyword Arguments </br>
	(c).	Required Arguments </br>
	(d).	Variable length Arguments </br>
		
**(a).	Default Arguments:**
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument. </br>

**Example:**
```
def name(fname, mname = “Fahim”, lname=”Ullah”):
	print(“Hello,”, fname, mname, lname)
			
name(“Muhammad”)

Output:

	Hello, Muhammad Fahim Ullah
```
**(b).	Keyword Arguments:** </br>
We can provide arguments with key=value, this way the Interpreter recognizes the arguments by the parameter name. Hence, the order in which the arguments are passed does not matter. </br>
**Example:**
```
def name(fname, mname, lname):
	print(“Hello,”, fname, mname, lname)
			
	name(mname=”Muhammad”, lname=”Ullah”, fname=”Fahim”)
	
Output:
	Hello, Muhammad Fahim Ullah
```
**(c).	Required Arguments:** </br>
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition. </br>
**Example 1:** </br>
When number of arguments passed does not match to the actual function definition. 
```				
		def name(fname, mname, lname):
			print(“Hello,”, fname, mname, lname)
		name(“Fahim”, “Ullah”)

		Output:
		name(“Fahim”, “Ullah”)\
		TypeError: name() missing 1 required positional
		argument: “lname” 
```
**Example 2:** </br>
When number of arguments passed matches to the actual function definition.		
```
		def name(fname, mname, lname):
			print(“Hello,”, fname, mname, lname)
		name(“Muhammad”, “Fahim”, “Ullah”)

		Output:
		
		Hello, Muhammad Fahim Ullah
```
**(d).	Variable-length Arguments:** </br>
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments. </br>
There are two ways to achieve this: </br>
**(i).	Arbitrary Arguments:** </br>
While creating a function, pass a * before the parameter name while defining the function. The function access the arguments by processing them in the form of tuple. </br>
**Example:**
```
def name(*name):
	print(“Hello,”, name[0], name[1], name[2])
name(“Muhammad”, “Fahim”, “Ullah”)

Output:
	Hello, Muhammad Fahim Ullah
```
**(ii).	Keyword Arbitrary Arguments:** </br>
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary. </br>
**Example:**
```
def name(**name):
	print(“Hello,”, name[“fname”], name[“mname”], name[“lname”])
name(mname=”Fahim”, lname=”Ullah”, fname=”Muhammad”)

Output:

Hello, Muhammad Fahim Ullah
```
### 3.	return Statement:
The return statement is used to return the value of the expression back to the calling function. </br>
**Example:**
```
def name(fname, mname, lname):
	return”Hello, ” + fname + “ “ + mname + “ “ + lname
print(name(“Muhammad”, “Fahim”, “Ullah”))

Output:

Hello, Muhammad Fahim Ullah
```
**Example 1:**
```
def average(*numbers):
    num = 0
    for i in numbers:
        num=num+i
    print("The average of numbers is:", num/len(numbers))
average(16, 17, 18)

Output:

The average of numbers is: 17.0
```
**Example 2:**
```
def name(fname,mname,lname):
    print("Salam", fname, mname, lname, "Bhai")
a = input("Enter your first name")
b = input("Enter your middle name")
c = input("Enter your last name")
name(a, b, c)

Output:

Salam Muhammad Fahim Ullah Bhai
```
**Example 3:**
```
def fc(food,color):
    for food, color in zip(food, color):
        print(food,"color is", color)
a = ["Apple", "Banana", "Carrot"]
b = ["Red", "Yellow", "Orange"]
fc(a,b)

Output:

Apple color is Red
Banana color is Yellow
Carrot color is Orange
``` 
**Example 4:**
```
def fc(food,color):
    lu=[]
    for food, color in zip(food, color):
        lu.append((food,"color is", color))
    return(lu)
a = "Apple", "Banana", "Carrot"
b = "Red", "Yellow", "Orange"
print(fc(a, b))

Output:

[('Apple', 'color is', 'Red'), ('Banana', 'color is', 'Yellow'), ('Carrot', 'color is', 'Orange')]
```
**Example 5:**
```
def name(fname, mname, lname):
    return"Hello" +" "+ fname + " " + mname + " " + lname + " "+ "Bhai"
print(name("Muhammad", "Fahim", "Ullah"))

Output:

Hello Muhammad Fahim Ullah Bhai
``` 
# Python Lists, List Index, List Methods (list.sort(), reverse(), index(), count(), copy(), append(), insert(), extend()):
### 1.	Python Lists:
Lists are ordered collection of data items. </br>
They store multiple items in a single variable. </br>
List items are separated by commas and enclosed within square brackets [ ]. </br>
Lists are changeable meaning we can alter them after creation. </br>
**Example 1:**
```
			list1 = [1, 2 ,2, 3, 5, 4, 6]
			list2 = [“Red”, “Green”, “Blue”]
			print(list1)
			print(list2)

	Output:

			[1, 2 ,2, 3, 5, 4, 6]
			[‘Red’, ‘Green’, ‘Blue’]
```
**Example 2:**
```
			details = [“Khan”, 18, “Gul”, 9, 8]
			print(details)

	Output:
			[‘Khan’, 18, ‘Gul’, 8]
```
As we can see, a single list can contain items of different data types.

### 2.	List Index:
Each item / element in a list has its own unique index. This index can be used to access any particular item from the list. </br> The first item has index [0], second item has index [1], third item has index [2] and so on.
	
**Example:**
```
			Colors = [“Red”, “Green”, “Blue”, “Yellow”, “Green”]
				     #[0]         [1]         [2]           [3]          [4]
```
**Accessing list items** </br>
We can access list items by using its index with the square bracket syntax [ ]. For example colors[0] will give “Red”, color[1] will give “Green” and so on… </br> </br>
 
**Positive Indexing:** </br>
As we have seen that list items have index, as such we can access items using these indexes. </br>
**Example:**
```
			Colors = [“Red”, “Green”, “Blue”, “Yellow”, “Green”]
			print(colors[2])
			print(colors[4])
			print(colors[0])

	Output:
			Blue
			Green
			Red
```
**Negative Indexing:** </br>
Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index[-1], second last item has index [-2], third last item has index [-3] and so on. </br>	
**Example:**
```
			Colors = [“Red”, “Green”, “Blue”, “Yellow”, “Green”]
			print(colors[-1])
			print(colors[-3])
			print(colors[-5])

	Output:
			Green
			Blue
			Red
```
**Note:** We can convert negative index into positive index in the following way: </br> </br>
	
**Example:**
```
			Colors = [“Red”, “Green”, “Blue”, “Yellow”, “Green”]
			print(colors[len(colors)-1])		#This is equal to print(colors[4])
			print(colors[len(colors)-3])		#This is equal to print(colors[2])
			print(colors[len(colors)-5]) 		#This is equal to print(colors[0])

		Output:
				Green
				Blue
				Red
```	
 

**We can check whether an item is present in the list?** </br>
We can check if a given item in the list. This is done using the “in” keyword. </br>
**Example:**
```
			colors = [“Red”, “Green”, “Blue”, “Yellow”, “Green”]
			if “Yellow” in colors:
				print(“Yellow is present.”)
			else:
				print(“Yellow is absent.”)

	Output:
			Yellow is present.
```
**Range of Index:** </br>
We can print a range of list items by specifying where you want to start, where do we want to end and if we want to skip elements in between the range. 
**Syntax:**
```
			listName[start : end : jumpIndex]
```
**Note:**	jump Index is optional. We will see this in later examples. </br> </br>

**Example: printing elements within a particular range:**
```	
		animals = [“cat”, “dog”, “bat”, “mouse”, “horse”, “buffalo”, “donkey”, “goat”, “cow”]
		print(animals[3:7])			#Using positive indexing
		print(animals[-7:-2])		#Using negative indexing

	Output:
		[‘mouse’, ‘horse’, ‘buffalo’, ‘donkey’, ‘goat’]
		[‘bat’, ’mouse’, ‘horse’, ‘buffalo’, ‘donkey’]
```
Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values. </br>

**Note:** The element of the end index provided will not be included. </br> </br>

**Example: printing all element from a given index till the end:**
```
		animals = [“cat”, “dog”, “bat”, “mouse”, “horse”, “buffalo”, “donkey”, “goat”, “cow”]
		print(animals[4: ])			#Using positive indexing
		print(animals[-4: ])		#Using negative indexing 

	Output:
		[‘horse’, ‘buffalo’, ‘donkey’, ‘goat’, ‘cow’]
		[‘buffalo’, ‘donkey’, ‘goat’, ‘cow’]
```
When no end index is provided, the interpreter prints all the values till the end. </br> </br>
 
**Example: printing alternate values:** 
```
		animals = [“cat”, “dog”, “bat”, “mouse”, “horse”, “buffalo”, “donkey”, “goat”, “cow”]
		print(animals[ : : 2])		
		print(animals[-8:-1:2])	 

	Output:
		[‘cat’, ‘bat’, ‘horse’, ‘donkey’, ‘cow’]
		[‘dog’, ‘mouse’, ‘buffalo’, ‘goat’]
```
Here, we have not provided start and index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed. </br> </br>

**Example: printing every 3rd consecutive value within a given range:**
```
		animals = [“cat”, “dog”, “bat”, “mouse”, “horse”, “buffalo”, “donkey”, “goat”, “cow”]
		print(animals[1:8:3])

	Output:
		[‘dog’, ‘horse’, ‘goat’]
```
Here, jump index is 3. Hence it prints every 3rd element within given index.	 

### 3.	List Comprehension:
List comprehension are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
**Syntax:**
```
	List = [Expression(item) for item in iterable if Condition]
	Expression: It is the item which is being iterated.
	Iterable: It can be list, tuples, dictionaries, sets and even in arrays and strings.
	Condition: Condition checks if the item should be added to the new list or not.
```	
**Example 1: Accepts items with the small letter “a” in the new list:**
```
  	 names = [“AbdulSalam, “Fahimullah”, “MuhammadYousaf”, “Waqar”, “Aziz”, “Habib”]
	 namesWith_0 = [item for item in names if “a” in items]
	 print(namesWith_0)

	Output:
		[‘AbdulSalam’ ‘Fahimullah’, ‘MuhammadYousaf’, ‘Waqar’, ‘Habib’]
```
 
**Example 2: Accepts items which have more than 4 letters:**
```		
	  names = [“AbdulSalam, “Fahimullah”, “MuhammadYousaf”, “Waqar”, “Aziz”, “Habib”]
	  namesWith_0 = [item for item in names if (len(item) > 4]
	  print(namesWith_0)

	Output:
	 
	[‘AbdulSalam’ ‘Fahimullah’, ‘MuhammadYousaf’, ‘Waqar’, ‘Habib’]
```
### 4. 	List Methods:
**(a).	list.sort():** </br>
This method sorts the list in ascending order. The original list is updated.
**Example 1:**
```
				colors = [“voilet”, “indigo”, “blue”, “green”]
				colors.sort()
				print(colors)

				num=[4,2,5,3,6,1,2,1,2,8,9,7]
				num.sort()
				print(num)

		Output:
				[‘blue’, ‘green’, ‘indigo’, ‘voilet’]\
				[1,1,2,2,2,3,4,5,6,7,8,9]
```
What if we want to print the list in descending order ? We must give reverse-True as a parameter in the sort method. </br>

**Example:**
```
			Colors = [“voilet”, “indigo”, “blue”, “green”]
			Colors.sort(reverse=True)
			Print(colors)

			num = [4,2,5,3,6,1,2,1,2,8,9,7]
			num.sort(reverse=True)
			print(num)

	Output:
			[‘voilet’, ‘indigo’, ‘green’, ‘blue’]
			[9,8,7,6,5,4,3,2,2,2,1,1]
```
The reverse parameter is set to False by default. </br>
**Note:** Do not mistake the reverse parameter with the reverse method. </br> </br>
 
**(b).	reverse()** </br>
This method reverses the order of the list. </br>
**Example:**
```
			colors = [“violet”, “indigo”, “blue”, “green”]
			colors.reverse()
			print(colors)

			num = [4,2,5,3,6,1,2,1,2,8,9,7]
			num.reverse()
			print(num)

	Output:
			[‘green’, ‘blue’, ‘indigo’, ‘voilet’]
			[7,9,8,2,1,2,1,6,3,5,2,4]	.
```
**(c).	index()** </br>
This method returns the index of the first occurrence of the list item. </br>
**Example:**
```
			colors = [“voilet”, “green”, ‘indigo’, “blue”, “green”]
			print(colors.index(“green”))

			num = [4,2,5,4,6,1,2,1,3,2,8,9,7]
			print(num.index(3))

	Output:
			1
			4	
```	
**(d).	count()** </br>
Returns the count of the number of items with the given value. </br>
**Example:**
```
			colors = [“voilet”, “green”, ‘indigo’, “blue”, “green”]
			print(colors.count(“green”))
			num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
			print(num.count(3))
		
		
		Output:
				2
				3
```
**(e)	copy():** </br>
Returns copy of the list. This can be done to perform operations on thelist without modifying the original list. </br>
**Example:**
```
			colors = [“voilet”, “green”, ‘indigo’, “blue”, “green”]
			newlist = colors.copy()
			print(colors)
			print(newlist)
		
		Output:
				[‘voilet’, ‘green’, ‘indigo’, ‘blue’]
				[‘voilet’, ‘green’, ‘indigo’, ‘blue’]
```
**(f)	append():** </br>
This method appends items to the end of the existing list. </br>
**Example:**
```
				colors = [“voilet”, “indigo”, “blue”]
				colors.append(“green”)
				print(colors)

		Output:
				[‘voilet’, ‘indigo’, ‘blue’, ‘green’]
```
**(g)	insert():** </br>
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method. </br>
**Example:**
```
				colors = [“voilet”, “indigo”, “blue”]
				   #	     [0]      [1]       [2]

				colors.insert(“green”)		#inserts item at index 1
				# updated list colors = [“voilet”, “green”, “indigo”, “blue”]	
			
				print(colors)

		Output:
				[‘voilet’, ‘green, ‘indigo, ‘blue]
```
**(h)	extend():** </br>
This method adds and entire list or any other collection datatype (set, tuple, dictionary) to the existing list. </br>
**Example 1:**
```
				# add a list in a list
				colors = [“voilet”, “indigo”, “blue”]
				rainbow = [“green”, “yellow”, “orange”, “red”]
				colors.extend(rainbow)
				print(colors)

		Output:
				[‘voilet’, ‘indigo’, ‘blue’, ‘green’, ‘yellow’, ‘orange’, ‘red’]
```
**(j)	Concatenating two lists:** </br>
We can simply concatenate two lists to join two lists. </br>
**Example:**
```
				colors = [“voilet”, “indigo”, “blue”, “green”]
				color2 = [“yellow”, “orange”, “red”]
				print(colors + colors2)

		Output:
				[‘voilet’, ‘indigo’, ‘blue’, ‘green’, ‘yellow’, ‘orange’, ‘red’]
```
# String formatting, f-strings in python:
### String formatting in Python: 
String formatting can be done in python using the format method.
```	
		Txt = “For only {price: .2f} dollars!”	# Here 2f means that only 2 digits after decimal.
		print(txt.format(price = 49.9999))

		Output:
			For only 49.99 dollars!
```
### f-strings in python:
It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as f-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier. </br>
When we prefix the string with letter ‘f’, the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting. </br>
**Example:**
```
				val = ‘Geeks’
				print(f”{val} for {val} is a portal for {val}.”)
				name = ‘Tahir’
				age = 23   
				print(f”Hello, My name is {name} and I’m {age} years old.”)

		Output:
				Hello, My name is Tahir and I’m 23 years old.
```
In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expression in them. </br>

We can use it in a single statement as well. </br>
**Example:**
```
		Print(f”{2*30}”)
Output:
		60
```
Here, if we want to show our curly brackets in our output while using f-strings then we can do this by placing double curly brackets at that place. As we can see in the below example.
**Example:**
```
				val = ‘Geeks’
				print(f”{val} for {val} is a portal for {val}.”)
				name = ‘Tahir’
				age = 23   
				print(f”Hello, My {{name}} is {name} and I’m {age} {{years}} old.”)

		Output:
				Hello, My {name} is Tahir and I’m 23 {years} old.
```
# Docstrings in python, Python Comments vs Docsstrings, Python doc attribute:
### 1.	Docstrings in python:
Python docstrings are the string literals that appear right after the definition of a function, method, class, or module. </br>
**Example:**
```
			def square(n):
				“””Take in a number n, returns the square of n”””
				print(n**2)
				square(5)

	Output:
			25
```
Here, in above example: “””Take in a number n, returns the square of n””” is a docstring which will not appear in output. </br> </br>
				
**Python Comments vs Docsstrings** </br>
**Python Comments** </br>
Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the python interpreter. </br>
**Python docstrings** </br>
As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code. </br>
We can access these docstrings using the doc attribute.	</br> </br>
**Python doc attribute** </br>
Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring. </br>
**Example:** </br>
```
	def square(n):
		“””Takes in a number n, returns the square of n”””
		print(n**2)
		square(5)
		print(square.__doc__)
		Output:
				25
				Takes in a number n, returns the square of n
```	
	So, here in the above example we saw that docstring, that we wrote just after the function def will show in our output. And this will show by running “__doc__” function. So it’s a docstring not a comment because the docstring is written just after the function def or above the function body. If we write it below then it will not remain docstring. It will be a comment.

### 2.	PEP 8 (Python Enhancement Proposal):
PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code. </br>
PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposal for Python and documents aspects of Python, like design and style, for the community.

### 3.	The Zen of Python:
Lone time Pythoneer Tim Peters succinctly channels the BDFL’s guiding principles for Python’s design into 20 algorithms, only 19 of which have been written down.

**The below is a Poem named as “Easter Egg”. It appear when we write: import this in the terminal.**

Explicit is better than implicit. </br>
Simple is better than complex. </br>
Complex is better than complicated. </br>
Flat is better than nested. </br>
Sparse is better than dense. </br>
Readability counts. </br>
Special cases aren’t special enough to break the rules. </br>
Although practicality beats purity. </br>
Errors should never pass silently. </br>
Unless explicitly silenced. </br>
In the face of ambiguity, refuse the temptation to guess. </br>
There should be one—and preferably only one –obvious way to do it. </br>
Although that way may not be obvious at first unless you’re Dutch. </br>
Now is better than never. </br>
Although never is often better than *right* now. </br>
If the implementation is hard to explain, It’s a bad idea. </br>
If the implementation is easy to explain, It’s a good idea. </br>
Namespaces are one honking great idea –lets do more of those! </br>
```
		Easter egg

		Import this	
```
