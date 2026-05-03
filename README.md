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
# Recursion in python, Python Recursive Functions:
### Recursion in python:
Recursion is the process of defining something in terms of itself. A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively. </br> </br>
**Python Recursive Functions:**
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions. </br>
**Example:** </br>
```
		def factorial(num):
			if (num ==1 or num == 0):
				return 1
		else:
			return(num * factorial(num - 1))
		# Driver Code
		num = 7;
		print(“Number: ”, num)
		print(“Factorial: ”, factorial(num))
Output:
		Number: 7
		Factorial: 5040
```
Here, we have to know that the factorial is a recursion (repeated) process of defining something in terms of itself. As we can see below:
```
factorial(7) = 7*6*5*4*3*2*1
factorial(6) = 6*5*4*3*2*1
factorial(5) = 5*4*3*2*1
factorial(4) = 4*3*2*1
factorial(3) = 3*2*1
factorial(2) = 2*1
factorial(1) = 1		#Here, in this case both factorial(1) = 1 and factorial(0) =1
factorial(0) = 1		#Here, in this case both factorial(1) = 1 and factorial(0) =1
```
**Practice:**
```
def factorial(n):
    if (n == 0) or (n==1):
        return 1
    else:
        return (n * factorial(n-1))
n = int(input("Enter the number for finding factorial"))
print("Number : ", n)
print("Factorial of Number is :", factorial(n))

Output:
        Number :  5
        Factorial of Number is : 120
```		
**Practice of finding the Fibonacci series of any number:** </br>
```
def fabonacci(n):
    if n<=1:
        return n
    else:
        return fabonacci(n-1) + fabonacci(n-2)
n = int(input("Enter the number for finding fabonacci"))
print("Number : ", n)
print("fabonacci of Number is :", fabonacci(n))

Output:
        Number :  6
        fabonacci of Number is : 8
```
As, we know that the Fibonacci series is:	
	
**f(n) = f(n-1) + f(n-2)** </br> </br>
f(0) = 0 </br>
f(1) = 1 </br>
f(2) = 1 	f(1) + f(0) = 1 (because value of  f(1) is 0 and f(0) is 0) </br>
f(3) = 2	f(2) + f(1) = 2 (because value of f(2) is 1 and f(1) is 1) </br>
f(4) = 3	f(3) + f(2) = 3 (because of value of f(3) is 2 and f(2) is 1) </br>
f(5) =5		f(4)+ f(3) = 5 (because value of f(4) is 3 and f(3) is 2) </br>
f(6) =	8	f(5) + f(4) = 8 (because value of f(5) is 5 and f(4) is 3) </br>
f(7) =13 	f(6) + f(5) = 13 (because value of f(6) is 8 and f(5) is 5) </br>
	. </br>
	. </br>
	. </br>
	and so on… </br> </br>

Hence, the fabonacci series is the addition of previous two numbers which becomes the next coming number. </br> </br>
	i.e    0,     1,    1,     2,    3,    5,    8,    13,   21….. </br>
	      f(0),  f(1), f(2),  f(3), f(4), f(5), f(6), f(7),  f(8)….. </br> </br>
**Practice** </br>
```
def f(n):
    if n<=1:
        return n
    else:
        return f(n-1)+f(n-2)
n=8
for i in range(n):
    print(f(i))

Output:
0
1
1
2
3
5
8
13  
```
# Python Sets, Joining Sets (Union, Intersection & Update), Sets Methods (isdisjoint, issuperset, issubset, add, update, remove discard, pop, del, clear methods):
### 1.	Python Sets:
Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable / replaceable, meaning you cannot change / replace items of the set once created. However, we do everything with sets as we do with list (like we can add etc). Sets do not contain duplicate items, but can put items having different data types and the result will unordered, means there is no order of items in the sets. </br>
**Example:**
```
			info = {“Carla”, 19, False, 5.9, 19}
			print(info)
	Output:
			{“Carla”, 19, False, 5.9}
```
Here, we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.</br> </br>

**Quick Quiz:** Try to create an empty set. Check using the type() function whether the type of you variable is a set. i.e
```
set = { }
print(type(set))

Output:
        <class 'dict'>
```
As we see in the above program when we checks an empty set with type() function, its show us its type as dictionary data type. Because the syntax of sets and dictionary data types are same, so { } is an empty dictionary not an empty set. The empty set is set = set( ). </br>
But when we add some items in it shows us a set mentioned in below example.
```
set = {1,2,3,4,3}
print(type(set))

Output:
        <class 'set'>
```
**Accessing sets items:** </br>
We can access items of set using a for loop. </br>
**Example:**
```
			info = {“Carla”, 19, False, 5.9}
			for item in info:
				print(item)
	Output:
			Carla
			19
			False
			5.9
```
### 2.	Joining Sets:
Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.	</br> </br>

**a.	union() and update():** </br>
The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.</br>
**Example:** 
```
				cities = {“Tokyo”, “Istanbul”, “Berlin”, “Peshawar”}
				cities2 = {“Tokyo”, “Islamabad”, “Rawalpindi”, “Karachi’}
				cities3 = cities.union(cities2)
				print(cities3)
		Output:

		{“Tokyo”, “Istanbul”, “Berlin”, “Peshawar”, “Islamabad”, “Rawalpindi”, “Karachi’}
```	
So, if we use **update()** function then all the items of one variable will comes in another variable. i.e in above example if we want make changes in cities, then we have to write **cities.update(cities2)**. By this all the items of **cities2** will comes in **cities**. On the other hand if we want to update **cities2** then we have to write **cities2.update(cities)**. As we can the **update()** function in below example. </br> </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Berlin”, “Peshawar”}
				cities2 = {“Tokyo”, “Islamabad”, “Rawalpindi”, “Karachi’}
				cities.update(cities2)
				print(cities)
		Output:

		{“Tokyo”, “Istanbul”, “Berlin”, “Peshawar”, “Islamabad”, “Rawalpindi”, “Karachi’}
```
**b.	intersection and intersection_update():** </br>
The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set. </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				cities2 = {“Tokyo”, “Islamabad”, “Rawalpindi”, “Karachi’}
				cities3 = cities.intersection(cities2)
				print(cities3)
		Output:
				{“Tokyo”, “Islamabad”}
```	
Hence, in **intersection_update()** it will add only the common items of both variables, means if we want to change cities variable then we have to write **cities.intersection_update(cities2)** and if we want to change **cities2** then we have to write **cities2.intersection_update(cities)**. As we can see in the below example: </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				cities2 = {“Tokyo”, “Islamabad”, “Rawalpindi”, “Karachi’}
				cities.intersection_update(cities2)
				print(cities)
	Output:
				{“Tokyo”, “Islamabad”}
```
**c.	symmetric_difference and symmetric_difference_update():** </br>
The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas the symmetric_difference_update() method updates into the existing set from another set. </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				cities2 = {“Tokyo”, “Islamabad”, “Rawalpindi”, “Karachi’}
				cities3 = cities.symmetric_difference(cities2)
				print(cities3)
		Output: 
			{“Istanbul”, “Peshawar”, “Rawalpindi”, “Karachi’}
```
Similarly the **symmetric_difference_update()** is used to change the set. So when we write the **cities.symmetric_difference_update(cities2)** it will change the cities variable and stores all the uncommon items of **cities** and **cities2** in **cities** in it and vice versa. As we can see in below example. </br> </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				cities2 = {“Tokyo”, “Islamabad”, “Rawalpindi”, “Karachi’}
				cities.symmetric_difference_update(cities2)
				print(cities)
		Output: 
			{“Istanbul”, “Peshawar”, “Rawalpindi”, “Karachi’}
```
**d.	difference() and difference_update():** </br>
The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set. </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				cities2 = {“Tokyo”, “Islamabad”, “Rawalpindi”, “Karachi’}
				cities3 = cities.difference(cities2)
				print(cities3)
		Output: 
			{“Istanbul”, “Peshawar’}
```

### 3.	Sets Methods:
There are several in-built methods used for the manipulation of set. They are explained below. </br> </br>

**a.	isdisjoint():** </br>
The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True. </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				cities2 = {“Tokyo”, “Islamabad”, “Rawalpindi”, “Karachi’} 
				print(cities.isdisjoint(cities2))
		Output:
				False
```	
**b.	issuperset():** </br>
The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False. </br>
**Example:**
```
			cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
			cities2 = {“Tokyo”, “Islamabad”, “Rawalpindi”, “Karachi’}
			print(cities.issuperset(cities2))
			cities3 = {“Tokyo”, “Istanbul”, “Islamabad”}
			print(cities.issuperset(cities3))
	Output:
			False
			True
```
**c.	issubset():** </br>
The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False. </br>
**Example:**
```
			cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
			cities2 = {“Tokyo”, “Islamabad”}
			print(cities2.issubset(cities))
	Output:
			True
```		
**d.	add():** </br>
If we want to add a single item to the set use the add() method. </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				cities.add(“Kabul”)
				print(cities)
		Output:
				{“Tokyo”, “Istanbul”, “Kabul”, “Islamabad”, “Peshawar”}
```
**e.	update():** </br>
If we want to add more than one item, then we have to simply create another set or any other iterable object (i.e list, tuple, dictionary), and use the update() method to add it into the existing set. </br>
**Example:**
```
			cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
			cities2 = {“Karachi”, “Kabul”, “Multan”}
			cities.update(cities2)
			print(cities)
	Output:
			{“Tokyo”, “Istanbul”, “Karachi”, “Islamabad”, “Kabul”, “Peshawar”, “Multan”}
```
**f.	remove() / discard():** </br>
We can remove() and discard() methods to remove items from the list. </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				cities2 = {“Karachi”, “Kabul”, “Multan”}
				cities.remove(“Tokyo”)
				cities2.remove(“Islamabad”)
				print(cities)
				print(cities2)

		Output:
				{“Istanbul”, “Islamabad”, “Peshawar”}
				KeyError:’Islamabad’
```	
The main difference between remove and discard is that, if we try to delete and item which is not present in set, then remove() raises an error, where discard() dies not raise any error. </br>

**g.	pop():** </br>
This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assigned the pop() method to a variable. </br>
**Example:** </br>
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				item = cities.pop()
				print(cities)
				print(item)
		Output:
				{“Istanbul”, “Islamabad”, “Peshawar”} 
				Tokyo     # This is the random popped / removed item
```
**h.	del:** </br>
del is not a method, rather it is a keyword which deletes the set entirely. </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				del.cities
				print(cities)
		Output:
			NameError: name ‘cities’ is not defined.
```
We get and error because our entire set has been deleted and there is no variable called cities which contains a set. </br>

What if we don’t want to delete the entire set, we just want to delete all items within that set? Then here we have a clear() method explained below. </br> </br>
**j.	clear():** </br>
This method clears all items in the set and prints an empty set. </br>
**Example:**
```
				cities = {“Tokyo”, “Istanbul”, “Islamabad”, “Peshawar”}
				cities.clear()
				print(cities)
		Output:
				set()
```
**k.	Check if item exists:** </br>
We can also check if an item exists in the set or not. </br>
**Example:**
```
				info = {“Carla”, 19, False, 5.9, 19}
				if “Carla” in info:
					print(“Carla is present.”)
				else:
					print(“Carla is absent.”)
		Output:
				Carla is present.
```		
 
**Practice 1 :** </br>
```
cities = {"Tokyo", "Istanbul", "Berlin", "Peshawar"}
cities2 = {"Tokyo", "Islamabad", "Rawalpindi", "Karachi"}
cities3 = {"Tokyo", "Berlin", "Kabul", "Multan"}
cities4 = {"Tokyo", "Istanbul", "Berlin", "Peshawar"}
cities5 = {"Tokyo", "Islamabad", "Rawalpindi", "Karachi"}
cities6 = {"Tokyo", "Istanbul", "Berlin", "Peshawar"}
cities7 = {"Tokyo", "Islamabad", "Rawalpindi", "Karachi"}
union1 = cities.union(cities2)
cities.update(cities2)
Intersect1 = cities2.intersection(cities3)
cities2.intersection_update(cities3)
symdif = cities4.symmetric_difference(cities5)
cities4.symmetric_difference_update(cities5)
dif = cities6.difference(cities7)
cities6.difference_update(cities7)
print("The union of cities and cities2 is :", union1)
print("When we write cities.update(cities2) the update method applied on cities set i.e:", cities)
print("The intersection between cities2 and cities3 is :", Intersect1)
print("The intersection_update changes the cities2 items when we write cities2.intersection_update(cities3)", cities2)
print("The symetric_difference of cities4 and cities5 is :", symdif)
print("When we write cities4.symmetric_difference_update(cities5) is changes cities4 :", cities4)
print("The difference method between cities6 and cities7 is :", dif)
print("The difference_update method applied on cities6 when we write cities6.difference_update(cities7):", cities6)

Output:

The union of cities and cities2 is : {'Istanbul', 'Tokyo', 'Peshawar', 'Rawalpindi', 'Berlin', 'Karachi', 'Islamabad'}
When we write cities.update(cities2) the update method applied on cities set i.e: {'Istanbul', 'Tokyo', 'Peshawar', 'Rawalpindi', 'Berlin', 'Karachi', 'Islamabad'}
The intersection between cities2 and cities3 is : {'Tokyo'}
The intersection_update changes the cities2 items when we write cities2.intersection_update(cities3) {'Tokyo'}
The symetric_difference of cities4 and cities5 is : {'Istanbul', 'Peshawar', 'Rawalpindi', 'Karachi', 'Berlin', 'Islamabad'}
When we write cities4.symmetric_difference_update(cities5) is changes cities4 : {'Istanbul', 'Peshawar', 'Rawalpindi', 'Berlin', 'Karachi', 'Islamabad'}
The difference method between cities6 and cities7 is : {'Istanbul', 'Berlin', 'Peshawar'}
The difference_update method applied on cities6 when we write cities6.difference_update(cities7): {'Istanbul', 'Berlin', 'Peshawar'}
```
**Practice 2:**
```
cities = {"Tokyo", "Istanbul", "Berlin", "Peshawar"}
cities2 = {"Tokyo", "Islamabad", "Rawalpindi", "Karachi"}
cities3 = {"Multan", "Lahore", "Karachi", "Faisalabad"}
cities4 = {"Tokyo", "Istanbul", "Peshawar"}
cities5 = {"Charsadda", "Wah", "Sawabi"}
cities6 = {"Charsadda", "Wah", "Sawabi"}
cities7 = {"Charsadda", "Wah", "Sawabi"}
isdisjoint1 = cities.isdisjoint(cities2)
isdisjoint2 = cities.isdisjoint(cities3)
issuperset1 = cities.issuperset(cities2)
issuperset2 = cities.issuperset(cities4)
issubset1 = cities4.issubset(cities)
cities4.add("Kabul")
cities5.update(cities)
cities3.remove("Multan")
popi = cities6.pop()
cities7.clear()
print("When we apply isdisjoint method and write cities.isdisjoint(cities2) :", isdisjoint1)
print("When we apply isdisjoint method and write cities.isdisjoint(cities3) :", isdisjoint2)
print("when we apply issuperset method and write cities.issuperset(cities2): ", issuperset1)
print("When we apply issuperset method and write cities.issuperset(cities4): ",issuperset2)
print("When we apply issubset method and write cities4.issubset(cities) :",issubset1)
print("When we add Kabul in cities4 with add method :", cities4)
print("When we apply update method and write cities5.update(cities): ", cities5)
print("""When we apply remove method and write cities3.remove("Multan") : """, cities3)
print("When we apply pop method on cities6 it removes the last item : ", popi)
print("when we apply clear method on cities7 it wil clear all the set and return an empty set : ", cities7)

Output:
When we apply isdisjoint method and write cities.isdisjoint(cities2) : False
When we apply isdisjoint method and write cities.isdisjoint(cities3) : True
when we apply issuperset method and write cities.issuperset(cities2):  False
When we apply issuperset method and write cities.issuperset(cities4):  True
When we apply issubset method and write cities4.issubset(cities) : True
When we add Kabul in cities4 with add method : {'Istanbul', 'Kabul', 'Tokyo', 'Peshawar'}
When we apply update method and write cities5.update(cities):  {'Istanbul', 'Berlin', 'Sawabi', 'Charsadda', 'Tokyo', 'Wah', 'Peshawar'}
When we apply remove method and write cities3.remove("Multan") :  {'Faisalabad', 'Karachi', 'Lahore'}
When we apply pop method on cities6 it removes the last item :  Sawabi
when we apply clear method on cities7 it wil clear all the set and return an empty set :  set()
```
# Python Dictionaries, Dictionary Methods(update, Clear, pop, popitem):
### Python Dictionaries:
Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}. </br>
**Example:** 
```
			info = {‘name’ : ‘Tahir’, ‘age’ : 19, ‘eligible’ : True}
			print(info)

 	Output:
			{‘name’ : ‘Tahir’, ‘age’ : 19, ‘eligible’ : True}
```
### 1.	Accessing Dictionary items: </br> </br>
	
**a.	Accessing single values:** </br>
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioned keys either in square brackets or by using get method. </br>
**Example:**
```
				info = {‘name’ : ‘Tahir’, ‘age’ : 19, ‘eligible’ : True}
				print(info[‘name’])
				print(info.get(‘eligible’))
		Output:
				Tahir
				True
```
Here, in the above example we print the name and eligibility of Tahir. So we used to print the values by using their keys in [ ] bracket i.e we write “print(info[‘name’])” and also using get method i.e we write “print(info.get(‘eligible’))”. Both the usage is valid but if we used to print [ ] and we writes wrong key name then its throw an error, whereas if we use get method and writes wrong key name its prints the output as “none” and does’nt throws any error. So its depends upon our use case that whether we wants to throw an error or not by writing wrong key name.

**b.	Accessing multiple values:** </br>
We can print all the values in the dictionary using values() method. </br>
**Example:**
```
				info = {‘name’ : ‘Tahir’, ‘age’ : 19, ‘eligible’ : True}
				print(info.values())
		Output:
				dict_values([‘Tahir, 19, True’])
```
 
Here, we can also access the key or values by using the for loop. as we can see in the below example.

**Example:**
```
				info = {‘name’ : ‘Tahir’, ‘age’ : 19, ‘eligible’ : True}
				for key in info.keys():
					print(info[key])
Output:
		Tahir
		19
		True
```	
And, we can also write it in below form for finding its values by using for loop.
```
info = {'name' : 'Tahir', 'age' : 19, 'eligible' : True}
for i in info.values():
   print(i)

Output:
        Tahir
        19
        True
```
And, we can also write it in below form for finding its keys by using for loop.
```
info = {'name' : 'Tahir', 'age' : 19, 'eligible' : True}
for i in info.keys():
   print(i)

Output:
        name
        age
        eligible
```
And, we can also write it in below form by finding its keys by using for loop in f-strings.
```
info = {'name' : 'Tahir', 'age' : 19, 'eligible' : True}
for i in info.keys():
   print(f"The values corresponding to the key {i} is :", info[i])

Output:
        The values corresponding to the key name is : Tahir
        The values corresponding to the key age is : 19
        The values corresponding to the key eligible is : True
```
**c.	Accessing keys:** </br>
We can print all the keys in the dictionary using keys() method. </br>
**Example:**
```
				info = {‘name’ : ‘Tahir’, ‘age’ : 19, ‘eligible’ : True}
				print(info.keys())
		Output:
				dict_keys([‘’name], ‘age’, ‘eligible’)
```
**d.	Accessing key-value pairs:** </br>
We can print all the key-value pairs in the dictionary using item() method. </br>
**Example:**
```
				info = {‘name’ : ‘Tahir’, ‘age’ : 19, ‘eligible’ : True}
				print(info.item())
		Output:
				dict_items([(‘name’, ‘Tahir’), (‘age’, 19), (‘eligible’, True)])
```
Here we can also print it in the below mentioned way also.
```
info = {'name' : 'Tahir', 'age' : 19, 'eligible' : True}
for key, values in info.items():
    print(f"The corresponding value of key {key} is :", values)

Output:
        The corresponding value of key name is : Tahir
        The corresponding value of key age is : 19
        The corresponding value of key eligible is : True
```
### 2.	Dictionary Methods:
Dictionary uses several built-in methods for manipulation. They are listed below. </br> </br>
**a.	update():** </br>
The update() method updates the value of the key provided to it if the item already exists in thedictionary, elseit creates a new key-value pair. </br>
**Example:**
```
			info = {‘name’ : ‘Tahir, ‘age’ : 19, ‘eligible’ : True}
			print(info)
			info.update(‘age’ : 20)
			info.update(‘DOB’ : 2001)
			print(info)
	Output:
			{‘name’ : ‘Tahir, ‘age’ : 19, ‘eligible’ : True}
			{‘name’ : ‘Tahir, ‘age’ : 20, ‘eligible’ : True, ‘DOB’ : 2001}
```
**b.	Removing items from dictionary :** </br>
There are few methods that we can use to remove items from dictionary. </br> </br>

**i.	Clear():** </br>
The clear() method removes all the items from the list. </br>
**Example:**
```
			Info = {‘name’ : ‘Tahir, ‘age’ : 19, ‘eligible’ : True}
			info.clear()
			Print(info)
	Output:
			{ }
```
**ii.	pop():** </br>
The pop() method removes the key-value pair whose key is passed as a parameter. </br>
**Example:**
```
			info = {‘name’ : ‘Tahir, ‘age’ : 19, ‘eligible’ : True}
			info.pop(‘eligible’)
			print(info)
	Output:
			{‘name’ : ‘Tahir, ‘age’ : 19}
```
**iii.	popitem():** </br>
The popitem() method removes the last key-value pair from the dictionary. </br>
**Example:**
```
		info = {‘name’ : ‘Tahir, ‘age’ : 19, ‘eligible’ : True, ‘DOB’ : 2003}
		info.popitem()
		print(info)
	
	Output:
		{‘name’ : ‘Tahir, ‘age’ : 19, ‘eligible’ : True}
```
**iv.	del:** </br>
We can use the del keyword to remove a dictionary item. </br>
**Example:**
```
		info = {‘name’ : ‘Tahir, ‘age’ : 19, ‘eligible’ : True, ‘DOB’ : 2003}
		del info[‘age’]
		print(info) 

	Output:
			{‘name’ : ‘Tahir, ‘eligible’ : True, ‘DOB’ : 2003}
```
If key is not provided, then the del keyword will delete the dictionary entirely and it will throws us an error. </br>
As we can see in the below example. </br>
**Example:**
```
		info = {‘name’ : ‘Tahir, ‘age’ : 19, ‘eligible’ : True, ‘DOB’ : 2003}
		del info
		print(info)

	Output:
		NameError:name ‘info’ is not defined.
```
**Note: We have to go through the latest documentation of python in which we can see the difference types of methods etc. that we didn’t see or used yet. This documentation can be seen in “[docs.python.org](https://docs.python.org/3/)”.**

# Python – else in Loop:
As we have learned before, the else clause is used along with the if statement. </br>
Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exists the loop on after the else block is executed. </br>
**Syntax:** 
```
			for counter in sequence:
				# Statements inside for loop block
			else:
				# Statements inside else block
```	
**Example:**
```
			for x in range(5):
				print(“iteration no { } in for loop”.format(x+1))
			else:
				print(“else block in loop”)
			print(“Out of loop”) 

	Output:
			iteration no 1 in for loop
			iteration no 2 in for loop
			iteration no 3 in for loop
			iteration no 4 in for loop
			iteration no 5 in for loop
			else block in loop
			Out of loop
```
Now, here in below example there is an important note, that if we uses if in for loop with also else condition and uses break keyword. </br> </br>
**Example:**
```
		for i in range(6):
			print(i)
			if i==4:
			    break
		else:
			print(“Sorry no i”)
Output:
		0
		1
		2
		3
		4
```
Here in above example we used break method which breaks the loop when if condition becomes true and our else condition will not be executed. </br>
We can also do the same thing while using while loop, as shown in below example. </br> </br>
**Example:**
```
		i = 0
		while i<7:
		     print(i)
		     i=i+1
		else:
		    print(“Sorry no i”)
Output:
		0
		1
		2	
		3
		4
		5
		6
		Sorry no i
```
# Exception Handling, Python try… except, Finally Clause, Raising Custom errors, Custom exceptions:
### Exception Handling:
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, an without this process, exceptions would disrupt the normal operation of a program. </br> </br>
**1.	Exceptions in Python:** </br>
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong). </br>
When these exceptions occur, the Python interpreter stops the current process and   passes it to the calling process until it is handled. If not handled, the program will crash. </br> </br>
**2.	Python try… except:** </br>
		    try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed. </br>
**Syntax:**
```
			try:
				#statements which could generate 
				#exception
			except:
				#Solution of generated exception
```
**Example:**
```
			try:
				num = int(input(“Enter an integer: ”))
				except ValueError:
					print(“Number entered is not an integer. ”)
	Output:
			Enter an integer: 6.022
			Number entered is not an integer.
```
Here, in the above example when we the input as integer then the output will become valid and the try block will executes, whereas when we input any string then the except block will executes. Here below some more examples. </br>
**Example 1: (While executing try block)**
```
try:
    a = int(input("Enter the Number for finding its table :"))
    for i in range(1, 11):
        print(a, "x", i, "=", a*i)
except:
    print("You entered and invalid number")

Output:
        123 x 1 = 123
        123 x 2 = 246
        123 x 3 = 369
        123 x 4 = 492
        123 x 5 = 615
        123 x 6 = 738
        123 x 7 = 861
        123 x 8 = 984
        123 x 9 = 1107
        123 x 10 = 1230
```
**Example 2: (While executing except block)**
```
try:
    a = int(input("Enter the Number for finding its table :"))
    for i in range(1, 11):
        print(a, "x", i, "=", a*i)
except:
    print("You entered an invalid number")

Output:
        You entered an invalid number
```
**3.	Finally Clause:** </br>
The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing the resources or closing database connection or may be ending the program execution with a delightful message. </br>
**Syntax:**
```
			try:
				#Statement which could generate
				#exception
			except:
				#solution of generated exception
			finally:
				#block of code which is going to 
				#execute in any situation
```
The finally block is executed irrespective of the outcome of try…..except…..else blocks. </br>
One of the important use cases of finally block is in a function which returns a value. </br> </br>
**Example 1: (When the user entered valid input)**
```
try:
    a = int(input("Enter the Number for finding its table :"))
    for i in range(1, 11):
        print(a, "x", i, "=", a*i)
except:
    print("You entered an invalid number")
finally:
    print("All weather thundering, i will be executed..")

Output:
        5 x 1 = 5
        5 x 2 = 10
        5 x 3 = 15
        5 x 4 = 20
        5 x 5 = 25
        5 x 6 = 30
        5 x 7 = 35
        5 x 8 = 40
        5 x 9 = 45
        5 x 10 = 50
        All weather thundering, i will be executed..
```
Here, in the above example we saw that the finally block will executed and similarly when the error occurs its always be executes. But here a question arises that if we didn’t uses finally block the code inside it will also be executed whether the error occurs or not, then what is its use case. The answer is that, when we define any function then inside the function the code written without finally block will not be executed. However, if the finally block used then the code inside it will be executed. As we can see in the below example. </br> </br>
**Example 2: (When the user put invalid input)**
```
def func():
    try:
        a = int(input("Enter the Number for finding its table :"))
        for i in range(1, 11):
            print(a, "x", i, "=", a*i)
    except:
        print("You entered an invalid number")
    finally:
        print("All weather thundering, i will be executed..")
func()

Output:
        You entered an invalid number
        All weather thundering, i will be executed..
```
**Note:** Here some misconception is arises the execution of code without finally block while using the function will be executed whether the user input is valid or not, however the concept of not showing the code became valid in that case when we use the return function in our code. </br> </br>
**Example 3: (When the user put valid input while using return function without finally block)**
```
def func():
    try:
        a = int(input("Enter the Number for finding its table :"))
        for i in range(1, 11):
            print(a, "x", i, "=", a*i)
            return 
    except:
        print("You entered an invalid number")
    print("All weather thundering, i will be executed..")
func()

Output:
        5 x 1 = 5
```
**Example 4: (When the user put valid input while using return function with finally block)**
```
def func():
    try:
        a = int(input("Enter the Number for finding its table :"))
        for i in range(1, 11):
            print(a, "x", i, "=", a*i)
            return 
    except:
        print("You entered an invalid number")
    finally:
        print("All weather thundering, i will be executed..")
func()

Output:
        5 x 1 = 5
        All weather thundering, i will be executed..
```
The same case is with the invalid input by the user while using return function. </br>
**4.	Raising Custom errors:** </br>
In python, we can raise custom errors by using the raise keyword. </br>
**Syntax:**
```
				salary = int(input(“Enter salary amount”))
				if not 2000 < salary < 5000:
					raise Value Error(“Not a valid salary”)
```
In the previous topics, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose. </br> </br>
**5.	Defining Custom exceptions:**
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class. </br>
Here below the syntax to define custom exceptions. </br>
**Syntax:**
```
		class CustomError(Exception):
			#Code….
			Pass
		Try:
			#Code…

		except CustomError:
			#Code…
```
This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an API, etc.	</br> </br>
```
salary = int(input("Enter salary amount"))
if not 80000 < salary:
    raise ValueError("Wife : Shutup its not true, tell me your actual income")
else:
    print("Yes you are write husband give me all the money. hurry up...")

Output:
        ValueError                                Traceback (most recent call last)
        Cell In[61], line 3
      1 salary = int(input("Enter salary amount"))
      2 if not 80000 < salary:
----> 3     raise ValueError("Wife : Shutup its not true, tell me your actual income")
      4 else:
      5     print("Yes you are write husband give me all the money. hurry up...")

        ValueError: Wife : Shutup its not true, tell me your actual income
```

Here, in the below example we did’nt used raise custom error unless for a practice only. </br>
```
a = input("Enter your obtained Marks percentage or write quit to leave...")
if a.lower() == "quit":
    print("Good bye....")
else:
    try:
        a = int(a)
        if a > 70 and a < 100:
            print("You are eligible for the job")
        else:
            print("You are not eligible for job")
    except:
        print("Invalid Entry: enter your total obtained marks between 70 and 100")

Output:
        Invalid Entry: enter your total obtained marks between 70 and 100
```
## Here, in the below example we again wrote a program, just for practice purpose. </br> </br>
**Task:** </br>
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language. </br> </br>
**Rules:** </br>
Encoding:
i. if the word contains at least 3 characters, remove the first letter and append it at the end. </br>
ii. now append three random characters at the starting and the end. </br>
else: </br>
iii. simply reverse the string. </br> </br>
Decoding: </br>
i. if the word contains less than 3 characters, reverse it. </br>
else: </br>
ii. remove 3 random characters from start and end. Now remove the    last letter and append it to the beginning. </br>
 
### Practice program for ENCODING of word:
```
print("======== Encoding ========")
word = input("Enter your secret word...")
word1 = list(word)
word3 = word1[0]
word1.pop(0)
word1.append(word3)
word4 = input("Enter any three random words....")
word5 = list(word4)
if ((len(word5)) == 3):
    word1.extend(word5)
    word5.extend(word1)
    for i in word5:
        print(i, end="")
else:
    word1.reverse()
    for i in word1:
        print(i, end="")

Output:
        ======== Encoding ========
        EFGBCDAEFG
```
### Practice program for DECODING of word:
```
print("======== Decoding ========")
word = input("Enter your Encoded words...")
word_ = input("Enter your three Random encoded words...")
wordn = list(word_)
word1 = list(word)
if (len(wordn) == 3):
    del word1[0:3]
    del word1[-3: ]
    word2 = list(word1[-1])
    word1.pop(-1)
    word2.extend(word1)
    for i in word2:
        print(i, end="")
else:
    word1.reverse()
    word3 = list(word1[-1])
    word1.pop(-1)
    word3.extend(word1)
    for i in word3: 
       print(i, end="")

Output:
        ======== Decoding ========
                  ABCD
```		
### Practice program for ENCODING and DECODING of word:
```
st = input("Enter message")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      r1 = "dsf"
      r2 = "jkr"
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3] # Remove the 3 random letters from start and end
      stnew = stnew[-1] + stnew[:-1] # Take the last letter and move it to the front
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
```
# Short hand if else statements, if….Else in One line, Enumerate function in python, Changing the start index:
### 1.	if….Else in One line:
There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here’s an example: </br>
**Example:**
```
				a = 2
				b = 330
				print(“A”) if a > b else print(“B”)
		Output:
				B
```
We can also have multiple else statements on the same line:</br>
**Example:** </br>
One line if else statement, with 3 conditions:
```		
				a = 330
				b = 330
				print(“A”) if a > b else print(“=”) if a==b else print(“B”)
		Output:
				=
```
In the above example its gives us the output as **=**, if the **a** variable is greater than **b** then it will prints us **A** in capital as output, because it’s written in double quotes. And if it’s not written in double quotes its will not give us the value of **a** but it gives us a syntax error because it is case sensitive. </br>
**Another Example:**
```			
			#result = value_if_true if condition else value_if_false

			#This syntax is equivalent to the following if-else statement:

			if condition:
				result = value_if_true
			else:
				result = value_if_false
```
**Conclusion:** </br>
The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition. However, it’s not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it’s best to use the full if-else syntax. </br> </br>
### 2.	Enumerate function in python:
The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here’s a basic example of how it works: </br>
**Example:**
```
			#loop over a list and print the index and value of each statement.
			fruit = [‘apple’, ‘banana’, ‘mango’]
			for index, fruits in enumerate(fruit):
				print(index, fruits)
	Output:
			0 apple
			1 banana
			2 mango
```
We can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. We can use the for loop to unpack these tuples and assign them to variables, as shown in the example above. </br>
**Example:**
```
			marks = [32, 98, 42, 96, 54, 82, 80]
			for index, mark in enumerate(marks):
				if(index == 3):
				print(“owesome…!”)
	Output:
			32
			98
			42
			96
			owesome…!
			54
			82
			80
```
### 3.	Changing the start index:
By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function: </br>
**Example:**
```
			#Loop over a list and print the index (starting at 1)
			fruits = [‘apple’, ‘banana’, ‘mango’]
			for index, fruit in enumerate(fruits, start=1):
				print(index, fruit)
	Output:
			1 apple
			2 banana
			3 mango
```
The enumerate function is often used when we need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way: </br>
**Example:1**
```
			fruits = [‘apple’, ‘banana’, ‘mango’]
			for index, fruit in enumerate(fruits):
				print(f’{index+1}: {fruit}’)
	Output:
			1: apple
			2: banana
			3: mango
```
**Example:2**
```
fruit = ['apple', 'banana', 'mango']
for index, fruits in enumerate(fruit):
    print(f"{index+1} delicious fruit is : {fruits}")
    
Output:
          1 delicious fruit is : apple
          2 delicious fruit is : banana
          3 delicious fruit is : mango
```
In addition to lists, you can use the enumerate function with any other sequence type in Python such as tuples and strings. </br> Here’s an example with a tuple: </br>
**Example:**
```
			#Loop over a tuple and print the index and value of each element.
			colors = (‘red’, ‘green’, ‘blue’)
			for index, color in enumerate(colors):
				print(index, color)
```
**Example with tuples:**
```
fruit = ('apple', 'banana', 'mango')
for index, fruits in enumerate(fruit):
    print(f"{index+1} delicious fruit is : {fruits}")
    
Output:
          1 delicious fruit is : apple
          2 delicious fruit is : banana
          3 delicious fruit is : mango
```
**And here’s an example with a string:** </br>
**Example:1**
```
			# loop over a string and print the index and value of each character
			s = 'hello'
			for index, c in enumerate(s):
    			print(index+1, c)

			Output:
		        1 h
		        2 e
		        3 l
		        4 l
		        5 o
```
**Example:2**
```
s = 'hello'
for index, c in enumerate(s):
    print(index+1, c, end=", ")

Output:
        1 h, 2 e, 3 l, 4 l, 5 o,
```
# Virtual Environment, How importing in python works, if __name__ == “__main__” in Python:
### 1.	Virtual Environment:
A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing us to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other. </br>

To create a virtual environment in Python, you can use the venv module that comes with Python. Here’s an example of how to create a virtual environment and activate it: </br> </br>
```
		#create a virtual environment
		Python –m venv myenv

		#Activate the virtual environment (This for Linux/macOS)
		Source myenv/bin/activate

		#Activate the virtual environment (This for windows)
		Myenv\Script\activate.bat
```
Once the virtual environment is activated, any package that we install using pip will be installed in the virtual environment, rather than in the global Python environment. This allows us to have a separate set of packages for each project, without affecting the packages installed in the global environment.
```
		# Deactivate the virtul environment
		Deactivate
```
</br>

**The “requirements.txt” file:** </br>
In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment. </br> 

To create a requirements.txt file, we can use the pip freeze command, which outputs a list of installed packages and their versions. For example: </br>
```
		# Output the list of installed packages and their versions to a file
		pip freeze > requirements.txt
```
</br>
To install the packages listed in the requirements.txt file, we can use the pip install command with the –r flag:
```
		# Install the packages listed in the requirements.txt file.
		pip install –r requirements.txt
```
Using a virtual environment and a requirements.txt file can help you manage the dependencies for your Python projects and ensure that your projects are portable and can be easily set up on a new machine. </br> </br>

### 2.	How importing in python works:
Importing in Python is the process of loading code from a python module into the current script. This allows us to use the functions and variables defined in the module in our current script, as well as any additional modules that the imported module may depend one. </br> 
To import a module in Python, we can use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement: </br>
```
		import math
```
Once a module is imported, we can use any of the functions and variables defined in the module by using dot notation. For example, to use the sqrt function from the math module, you would write:
```
		import math
		result = math.sqrt(9)
		print(result)			# Its output is : 3.0
```
**a.	from keyword:** </br>
We can also import specific functions or variables from a module using the from keyword. For example, to import only the sqrt function from the math module, we would write: </br>
```
			from math import sqrt
			result = sqrt(9)
			print(result)			# Its output is : 3.0
```
We can also import multiple functions or variables at once by separating them with a comma: </br>
```
			from math import sqrt, pi
			result = sqrt(9)
			print(result)			# Its output is : 3.0
			print(pi)			# its output is : 3.141592653589793
```
**b.	importing everything:** </br>
It’s also possible to import all functions and variables from a module using the *wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.
```
			from math import *
			result = sqrt(9)
			print(result)			# Its output is : 3.0
			print(pi)			# its output is : 3.141592653589793
```
Python also allows us to rename imported modules using the as keyword. This can be useful if we want to use a shorter or more descriptive name for a module, or if we want to avoid naming conflicts with other modules or variables in our code.

**c.	The “as” keyword:** </br>
```			
			import math as m
			result = m.sqrt(9)		# Its output is : 3.0
			print(m.pi)			# its output is : 3.141592653589793
```
Or, we can write it in below form:
```
			import math pi, sqrt as s
			result = s.(9) * pi
			print(result)			# Its output is : 9.42477796076938 
```
Or, we can also write it in more explanatory form that any could understand as mentioned below:
```
			import math as math_builtin_python
			result = math_builtin_python.sqrt(9) * math_builtin_python.pi
			print(result)			# Its output is : 9.42477796076938		
```
**d.	The dir function:** </br>
Finally, python has a built-in function called dir that we can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module. </br>
```
import math
print(dir(math))
```
This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants. </br>

In summary, the import statement in Python allows us to access the functions and variables defined in a module from within our current script. We can import the entire module, specific functions or variables, or use the *wildcard to import everything. We can also use the “as” keyword to rename a module, and the dir function to view the contents of a module.
 
### 2.	if __name__ == “__main__” in Python:
The if __name__ == “__main__” idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script. </br> </br>
In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set ot the name of the module. </br>

Here’s an example of how the if __name__ == __main__ idiom can be used: </br>
**Example:**
```
			def main():
				# Code to be run when the script is run directly
				print(“Running script directly”)
			if __name__ == “__main__”:
				main()
```
In this example, the main function contains the code that should be run when the script is run directly. The if statement at the bottom checks whether the __name__ variable is equal to __main__. If it is, the main function is called. </br> </br>

**a.	Why is it useful ?** </br>
This idiom is useful because it allows us to reuse code from a script by importing it as a module into another script, without running the code in the original script. For example, consider the following script: </br> </br>
**Example:**	
```
			def main():
				print(“Running script directly”)
			if __name__ == “__main__”:
				main()
```
If we run this script directly, it will output “Running script directly”. However, if you import it as a module into another script and call the main function from the imported module, it will not output anything: </br>
```
	import script
	script.main()		# Output: “Running script directly”
```
This can be useful if you have code that we want to reuse in multiple scripts, but we only want it to run when the script is run directly and not when it’s imported as a module. </br> </br>

**b.	Is it necessary ?** </br>
It’s important to note that the if __name__==”__main__” idiom is not required to run a Python script. We can still run a script without it by simply calling the functions or running the code we want to execute directly. However, the if__name__==”__main__” idiom can be a useful tool for organizing and separating code that should be run directly from code that should be imported and used as  a module. </br> </br>

In summary, the if__name__==”__main__” idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script. It allows us to reuse code from a script by importing it as a module in to another script, without running the code in the original script. </br> </br>
	Hence, the if__name__ == “__main__” idiom is used to run the specific part of the code in a function not all the code inside the function. That’s why we should be carefully and conscious while importing any other function in any other script, and if__name__==”__main__” will be useful at that time. </br>
# os Module in Python, Interacting with the file system, Running system commands:
### os Module in Python:
The os module in Python is built-in library that provides functions for interacting with the operating system. It allows us to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands. </br> </br>
Here, are some common tasks we can perform with the os module: </br> </br>
Reading and writing files. The os module provides functions for opening, reading and writing files. For example, to open a file for reading, we can use the open function: </br>
**Example:**
```
			import os

			# Open the file in read only mode
			f = os.open(“myfile.txt”, os.0_RDONLY)
		
			# Read the contents of the file
			contents = os.read(f, 1024)

			# Close the file
			os.close(f)
```
To open a file for writing, we can use the os.O_WRONLY flag: </br> </br>
**Example:**	
```
			import os
			
			# Open the file in write-only mode
			f = os.open(“myfile.txt”, os.0_WRONLY)
	
			# Write to the file
			os.write(f, b”Hello, world!”)
	
			# Close the file
			os.close(f)
```
**1.	Interacting with the file system:** </br>
The os module also provides functions for interacting with the file system. For example we can use the os.listdir to get a list of the files in a directory: </br>
**Example:**		
```
		# Get a list of the files in the current directory
		files = os.listdir(“.”)
		print(files)			# Output : [‘myfile.txt’, ‘otherfile.txt’]
```
We can also use the os.mkdir function to create a new directory: </br>
```
		Import os

		# Create a new directory
		os.mkdir(“newdir”)
```
**2.	Running system commands:** </br>
Finally, the os module provides functions for running system commands. For example, we can use the os.system function to run a command and get the output: </br>
**Example:**
```
				# Run the “ls” command and print the output
				output = os.system(“ls”)
				print(output)		# Output: [‘myfile.txt’, ‘otherfile.txt’]
```
We can also use the os.popen function to run a command and get the output as a file like object: </br> </br>
**Example:**		
```
		import os
		# Run the “ls” command and get the output as a file-like object
		f = os.popen(“ls”)

		# Read the contents of the output
		output = f.read()
		print(output)		# Output : [‘myfile.txt’. ‘otherfile.txt’]

		# Close the file-like object
		f.close()
```
In summary, the os module in Python is a built-in library that provides a wide variety of functions for interacting with the operating system. It allows you to perform tasks such as reading and writing files, interacting with the file system, and running system command. </br> </br>
**The below code is used for creation of folders**
```
		import os
		if (not os.path.exists("data")):
		    os.mkdir("data")
		for i in range(0, 100):
		    os.mkdir(f"data\Practice {i+1}")
```
</br>

**The below code is used for renaming our folders that we created on name “Practice”**
```
		import os
		if (not os.path.exists("data")):
		    os.mkdir("data")
		for i in range(0, 100):
		    os.rename(f"data\Practice {i+1}", f"data\Pract {i+1}")
```
</br>  

**To find out how many folders are there in our existing folder**
```
		import os
		Folders = os.listdir("Pract")
		print(Folders)
		for Folder in Folders:
		    print(Folder)
```
</br>

**To find out that how many folders we are:**
```
		import os
		Folders = os.listdir("Pract")
		# print(Folders)
		for Folder in Folders:
		    print(Folder)
		    print(os.listdir(f"data/{Folder}"))
```
</br> </br>
# Local and global variables:
**1.	Local and global variables:** </br>
A variable is named location in memory that stores a value. In Python, we can assign values to variables using the assignment operator **=** For example: </br>
**Example:**			
```
			x = 5
			y = “Hello, World!”
```
A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns. </br> </br>
On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in our code. Here below example shows the difference: </br>
**Example:** </br>
```
			x = 10				# global variable
			def my_function():
				y = 5			# local variable
				print(y)
			my_function()
			print(x)
			print(y)	# this will cause an error because y is a local variable and is not accessible outside the function.
```
In the above example, we have a global variable x and a local variable y. We can access the value of the global variable x from within the function, but we cannot access the value of the local variable y outside of the function. </br> </br>

**2.	The global keyword:** </br>
If we want to modify a global variable from within a function? This is where the global keyword comes in.
The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope. </br> 
**Here’s example:**
```
			x = 10				# global variable
			def my_function():
				global x 
				x = 5			# this will change the value of the global variable x
				y = 5 			# local variable

			my_function()
			print(x)			# It prints 5
			print(y)			# This will cause an error because y is a local 
							variable and is not accessible outside the function.
```
In the above example, we used the global keyword to declare that we want to modify the global variable x from within the function. As a result, the value of x is change to 5. </br> </br>
It is important to note that its generally considered good practice to avoid modifying global variable from within functions, as it can lead to unexpected behavior and make our code harder to debug. </br> </br>
**Example of accessing local and global variable without using “global” keyword:**
```
		x = 10 # global variable
		
		def my_function():
		  y = 5 # local variable
		  print(y)
		
		my_function()
		print(x)
		print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
```
</br>

**Example of accessing local and global variable by using “global” keyword:**
```
		x = 10 # global variable
		
		def my_function():
		  global x
		  x = 5 # this will change the value of the global variable x
		  y = 5 # local variable
		
		my_function()
		print(x) # prints 5
		print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
```
</br>
Hence, as we learned earlier that using of global keyword inside the function should avoided because its changes the scope of variable inside the function from local to global. </br>

# File IO in Python (File Handling), Opening a File, Modes in file (read, write, append, create, text, binary): 
### 1.	File IO in Python (File Handling):
Python provides several ways to manipulate files and how to handle files in python. </br> </br>

**a.	Opening a File:** </br>
Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be ‘r’ for reading, ‘w’ for writing, or ‘a’ for appending. </br>
Here’s an example of how to open a file for reading: </br>
```	
				f = open(‘myfile.txt’, ‘r’)
```
By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode. </br> </br>
**b.	Modes in file:** </br>
There are various modes in which we can open files.</br>

**i.	read (r):** This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter. </br> </br>

**ii.	write (w):** This mode opens the file for writing only and creates a new file if the file does not exist. </br> </br>

**iii.	append (a):** This mode opens the file for appending only and creates a new file if the file dies not exist. </br> </br>

**iv.	create (x):** This mode creates a file and gives an error if the file already exists. </br> </br>

**v.	text (t):** Apart from these modes we also need to specify how the file must be handled. ‘t’ mode is used to handle text files. ‘t’ refers to the text  mode. There is no difference between ‘r’ and ‘rt’ or ‘w’ and ‘wt’ since text mode is the default. The default mode is ‘r’ (open for reading text, synonym of ‘rt’). </br> </br>

**vi.	binary (b):** This mode is used to handle binary files (i.e images, pdfs, etc) </br> </br> </br>

**b.	Reading from a File:** </br>
Once we have a file object, we can use various methods to read from the file. </br>
The read() method reads the entire contents of the file and returns it as a string. </br>
**Example:**		
```
				f = open(‘myfile.txt’, ‘r’)
				contents = f.read()
				print(content)
```		
In the above example we used the read() method. So for using the read() method we must	have the file, then we can be able to read the file. In the above example we first create the 	‘myfile.txt’ file, then we can use the read() method. </br> </br>

**c.	Writing to a File:** </br>
To write to a file, we first need to open it in write mode. </br>
**Example:**				
```
				f = open(‘myfile.txt’, ‘w’)
				f.write(‘Hello, World!’)
				f.close()	
```
</br>
In the above example we used write() method in write ‘w’ mode. It is write the text that we have provided as ‘Hello, World!’ will be written in the file.txt file. If there is already any text available in myfile.txt file and then we use write() method, then it will overwrite the previous text. So, we have to keep in mind that writing to a file will overwrite its contents. If we want to append to a file instead of overwriting it, we can open it in append ‘a’ mode. As we can see below: </br>

**Example:** </br>
```
				f = open(‘myfile.txt’, ‘a’)
				f.write(‘Hello, World!’)
				f.close()
```
Now, in the above example we used the append ‘a’ mode with write() method, it will append the text ‘Hello, World!’ at the end of our already existing text, here we must have to close our file by using the close() method. </br> </br>

**d.	Closing a File:** </br>
It is important to close a file after we are done with it. This releases the resources used by the file and allows other programs to access it. </br>
To close a file, we can use the close() method as we used in the above examples. </br> </br>

**e.	The ‘with’ statement:** </br>
Alternatively, we can use the ‘with’ statement to automatically close the file after we are done with it. </br>
**Example:**				
```
				with open(‘myfile.txt’, ‘a’) as f:
				f.write(‘Hello, World!’)
```
In the above example we used the **‘with’** statement and we write the variable **‘f’** at its end with **‘as’** keyword. We used the append **‘a’** mode with **write()** method, so it will append our text ‘Hello, World!’ and closed it automatically and we did not need write the **close()** method. </br> </br>
**Example of reading from a file:**
```
f = open('myfile.txt', 'r')
contents = f.read()
print(contents)
contents.close()

#Its output is:  Hello bro, how are you >>>>?      # This the content of 'myfile.txt' file
```
</br> </br>

**Example of writing a file using ‘w’ mode:**
```
f = open('myfile.txt', 'w')
contents = f.write("Hello bro Hey!!!!!!!!")
print(contents)
contents.close()

#Output:
      #Here we overwrite the already existing text in 'myfile.txt' with 'Hello bro #Hey!!!!!!!' by using the write() method with write 'w' mode
```
</br> </br>
**Example of writing from a file using append ‘a’ mode:**
```
f = open('myfile.txt', 'a')
contents = f.write("Hello bro Hey!!!!!!!!")
print(contents)
contents.close()


#Output:
        #Here we used append 'a' mode with write() method. so it will append the text as #much time we are running our program.
```
</br> </br>
**Example of writing from a file using append ‘a’ mode with ‘with’ statement:**
```
with open('myfile.txt', 'a') as f:
  f.write("Hello bro Hyyyy!")

#Output:
          #Here we used 'with' statement, so here we did not need to use close() method #because its authomatically close our program after execution.
```				
</br> </br>
	
### 2.	readlines() method:
The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop. </br>
**Example:**			
```
			f = open(‘myfile.txt’, ‘r’)
			while True:
				line = f.readline()
				if not line:
				      break
				print(line)
```
The readlines() method reads all the lines of the file and returns them as a list of strings. </br> </br>

### 3.	writelines() method:
The writelines() method in python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple. </br> </br>
Here’s an example of how to use the writelines() method: </br>
**Example:**		
```
			f = open(‘myfile.txt’, ‘w’)
			lines = [‘line 1\n’, ‘line 2\n’, ‘line 3\n’]
			f.writelines(lines)
			f.close()
```
This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string. </br>
Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately: </br> </br>
**Example:**
```
			f = open(‘myfile.txt’, ‘w’)
			lines = [‘line 1’, ‘line 2’, ‘line 3’]
			for line in lines:
				f.write(line + ‘\n’)
			f.close()
```
It is also a good practice to close the file after you are done with it. </br> </br>
		
 
**Example of writeline() method:** 
```
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
```
</br> </br>

**Example of write method:**
```
f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()
```
</br> </br>
**Example (Elaborated each line of code comment):**
```
f = open("myfile.txt", "r")       # Here it will read the file i created
i = 0 # Here i starting the indexing of my file element with will denote the student name
while True: # Here i am starting a while loop, so it will continue when the subsequence condition remains true.
    i = i+1 # Here i am starting the index number from 1 by adding i with 1.
    line = f.readline() # Here i using readline() method which will be applied on my created file
    if not line: # Here if no more element exists means here a condition says that the line will continue till the last element in line.
        break # Here if no more element found, then it will breaks the while from further execution.
    m1 = line.split(",")[0] # Here its splits very first element which is on 0 index seperated by "," from each line and apply it to every subject.
    m2 = line.split(",")[1] # Here its splits second element which is on 1 index seperated by "," from each line and apply it to every subject.
    m3 = line.split(",")[2] # Here its splits third element which is on 2 index seperated by "," from each line and apply it to every subject.
    print(f"The marks of student {i} in English is : {m1}") # Now here we used the "f" string print the students with marks
    print(f"The marks of student {i} in Math is : {m2}")
    print(f"The marks of student {i} in Physics is : {m3}")

 Output:
          The marks of student 1 in English is : 70
          The marks of student 1 in Math is :  80   
          The marks of student 1 in Physics is :  90

          The marks of student 2 in English is : 75 
          The marks of student 2 in Math is :  85   
          The marks of student 2 in Physics is :  95

          The marks of student 3 in English is : 78 
          The marks of student 3 in Math is :  88   
          The marks of student 3 in Physics is :  98
```
</br> </br>
 
**Example (Without elaboration of each line of code):**
```
f = open("myfile.txt", "r")       
i = 0 
while True: 
    i = i+1 
    line = f.readline() 
    if not line: 
        break 
    m1 = line.split(",")[0] 
    m2 = line.split(",")[1] 
    m3 = line.split(",")[2] 
    print(f"The marks of student {i} in English is : {m1}") 
    print(f"The marks of student {i} in Math is : {m2}")
    print(f"The marks of student {i} in Physics is : {m3}")

 Output:
          The marks of student 1 in English is : 70
          The marks of student 1 in Math is :  80   
          The marks of student 1 in Physics is :  90

          The marks of student 2 in English is : 75 
          The marks of student 2 in Math is :  85   
          The marks of student 2 in Physics is :  95

          The marks of student 3 in English is : 78 
          The marks of student 3 in Math is :  88   
          The marks of student 3 in Physics is :  98
```
</br>

# seek() and tell() functions, truncate() function, Lambda Functions in Python, Map, Filter and Reduce:
### 1.	seek() and tell() functions:
In python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent Interface for reading and writing to various file-like objects such as files, pipes, and in-memory buffers.  </br>

**a.	seek() functions:** </br>
The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and we can move either forward or backward from the current position. </br>
**Example:**
```
				with open (‘file.txt’, r) as f:
					f.seek(10)	# Move to the 10th byte in the file
				data = f.read(5)	# Read the next 5 bytes
```
</br> </br>

**b.	tell () function:** </br>
The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of our location within the file or for seeking to a specific position relative to the current position. </br>
**Example:**
```
				with open(‘file.txt’, ‘r’) as f:   	
				      data = f.read(10)	   	# Read the first 10 bytes
      			current_position = f.tell()	# Save the current position
      			f.seek(current_position)	# Seek to the saved position
```
**c.	truncate() function:** </br>
When we open a file in Python using the open function, we can specify the mode in which we want to open the file. If we specify the mode as ‘w’ or ‘a’, the file is opened in write mode and we can write to the file. However, if we want to truncate the file to a specific size, we can use the truncate function. </br>

Here is an example of how to use the truncate function: </br>
**Example:**
```
				with open(‘sample.txt’, ‘w’) as f:
			    		 f.write(‘Hello World!’)
			    		 f.truncate(5)
				with open(‘sample.txt’, ‘r’) as f:
			     		print(f.read())
```
 
**2.	Lambda Functions in Python:** </br>
In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax: 
```
		lambda arguments: expression
```
Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order function, such as map, filter, and reduce. </br>

Here, is an example of how to use a lambda function: </br>
**Example:**
```
			def double(x):	# Function to double the input
			    return x * 2
			lambda x: x * 2	# Lambda function to double the input
```
The above lambda function has the same functionality as the double function defined earlier. However, the lambda function is anonymous, as it does not have a name. </br>

Lambda functions can have multiple arguments, just like regular functions. Here is an example of a lambda function with simple arguments: </br>
**Example:**
```
			def multiply(x, y):	# Function to calculate the product of two numbers 
			    return x * y
			lambda x, y: x * y	# Lambda function to calculate the product of two numbers
```
</br>

Lambda functions can also include multiple statements, but they are limited to a single expression. For example:
**Example:**
```
			# Lambda function to calculate the product of two numbers, 
			# with additional print statement
			lambda x, y: print(f’{x} * {y} = {x * y}’)
```

In the above example, the lambda function includes a print statement, but it is still limited to a single expression. </br>

Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce which we will look into later. </br>

So, the lambda function is an anonymous function or mini function used for a short period of time. We can use it if we have to build multiple functions in our program so there in that case lambda function can become feasible. </br>

As we see in the above example of lambda function we can have a look in code editor. </br> </br>
 
**We know that when we can create a normal regular function in under mentioned way by using “def” keyword**
```
def fun(x, y):
    return x * y
print(fun(5, 10))

Output:
        50
```

**OR** </br>

```
def fun(x):
    return x * x
print(fun(5))

Output:
        25
```
</br> </br>

**So, when we use a lambda function inside def function as mentioned below, we called and defined a function into function:**
```
def fun(fx, x):
    return 6 + fx(x)
y = lambda x: x*x*x
print(fun(y, 3))

Output:
        33
```
</br>  </br>

**So, When we use lambda function only, and here we did’nt need define a function using “def” keyword. As mentioned below:**
```
cube = lambda x: x*x*x
Avg = lambda x, y, z: (x+y+z)/3
double = lambda x: x * 2 * 3 
print(cube(2))
print(Avg(2, 3, 4))
print(double(5))

Output:
            8
            3.0
            30
```

 
### 3.	Map, Filter and Reduce:
In Python, the map, filter, and reduce functions are built-in functions that allow us to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments. Here, the higher-order functions means that we can call a function inside a function.

**a.	map:** </br>
The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:
```
			map(function, iterable)
```
The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object. </br> </br>

As we know that when we want to find the cube of our list we can do so by defining any function and can call that function by the help of for loop as we can see in the below example:
```
def myfunc(x):
    return x*x*x
l = [1, 2, 3, 4, 5, 7, 8]
li = []
for i in l:
    li.append(myfunc(i))
print(li)

Output:
        [1, 8, 27, 64, 125, 343, 512]
```
</br> </br>
But the above process became little bit complex and we can do the same thing by the help of map function As we can see in the below example. 
```
def myfunc(x):
    return x*x*x
l = [1, 2, 3, 4, 5, 7, 8]
li = list(map(myfunc, l))
print(li)

Output:
        [1, 8, 27, 64, 125, 343, 512]
```
</br> </br>
So, in the above example we used map function, moreover we can make the above code more readable and simple by using lambda function as we can see in the below example:
```
l = [1, 2, 3, 4, 5, 7, 8]
li = list(map(lambda x: x * x * x, l))
print(li)

Output:
        [1, 8, 27, 64, 125, 343, 512]
```

In the above example, the lambda function “lambda x: x * x” is used to square each element in the numbers list. The map function applies the lambda function to each element in the list and returns a new list containing the square of numbers. </br> </br>

**b.	filter:** </br>
The filter function filters a sequence of elements based on a given predicate (a function that returns a Boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:
```
filter(predicate, iterable)
```

The predicate argument is a function that returns a Boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object. </br> </br>

So, the filter function is used to filter our list according our defined condition. As we can see in the below example:
```
def myfunc(x):
    return x > 2
l = [1, 2, 3, 4, 5, 7, 8]
li = list(filter(myfunc, l))
print(li)

Output:
        [3, 4, 5, 7, 8]
```
</br> </br>
In the above example we used filter function inside the defined function. We can also do the same thing by using the lambda function.
```
l = [1, 2, 3, 4, 5, 7, 8]
li = list(filter(lambda x: x > 2, l))
print(li)

Output:
        [3, 4, 5, 7, 8]
```
And here, below one more example:
```
l = [1, 2, 3, 4, 5, 7, 8]
li = list(filter(lambda x: x % 2 == 0, l))
print(li)

Output:
        [2, 4, 8]
```
In the above example, the lambda function lambda “x: x % 2 == 0” is used to filter the numbers list and return only the even numbers. The filter function applies the lambda function to each element in the list and returns a new list containing only the even numbers. </br> </br>

**c.	reduce:** </br>
The reduce function is a higher-order function that applies function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax: </br>
```
reduce(function, iterable)
```
</br>
The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple. </br> </br>

The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result. </br> </br>

Here is an example of how to use the reduce function:
```
from functools import reduce
def myfunc(x, y):
    return x + y
l = [1, 2, 3, 4, 5, 7, 8]
li = reduce(myfunc, l)
print(li)

Output:
        30
```
</br> </br>
So, in the above example we used the reduce function by defining a function, and we know that while using the reduce function we have to first import it from functools otherwise it will throw error. The same thing can be done by using the lambda function, as we can see in the below example:
```
from functools import reduce
l = [1, 2, 3, 4, 5, 7, 8]
li = reduce(lambda x, y: x + y, l)
print(li)

Output:
        30
```
</br> 

In the above example, the reduce function applies the lambda function “lambda x, y: x + y” to the elements in the numbers list. The lambda function adds the two arguments x and y and returns the result. The reduce function applies the lambda function to the first two elements in the list (1 and 2), then applies the function to the result (3) and the next element (3), and so on. The final result is the sum of the elements in the list which is 15. </br>

It is important to note that the reduce function requires the functools module to be imported in order to use it. </br>
</br>
# ‘is’ vs ‘==’ in Python & Snake, Water, Gun Game:
### 1.	‘is’ vs ‘==’ in Python:
In Python, “is” and “==” are both comparison operators that can be used to check if two values are equals. However, there are some important differences between the two that you should be aware of. </br>
The “is “ operator compares the identity of two objects, while the “==” operator compares the value of the objects. This means that “is” will only return True if the object being compared are the exact same object in memory, while “==” will return True if the objects have the same value. </br>
**For example:**
```
			a = [1, 2, 3]
			b = [1, 2, 3]
			print(a == b)		# True
			print(a is b)		# False
```
In this case, a and b are two separate lists that have the same values, so “==” returns True. However, a and b are not the same object in memory, so is returns False. </br> </br>
One important thing to note is that, in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed. This means that, for strings and integers, “is” and “==” will always return the same result: </br>
**For example:**
```
			a = “hello”
			b = “hello”
			print(a == b)		# True
			print(a is b)		# True

			a = 5
			b = 5
			print(a == b)		# True
			print(a is b)		# True
```
In these cases, a and b are both pointing to the same object in memory, so “is” and “==” both return True. </br>
For mutable objects such as lists and dictionaries, **“is”** and **“==”** can behave differently. In general, we should use **“==”** when we want to compare the values of two objects, and use **“is”** when we want to check if two objects are the same object in memory. </br>

Hence, the “is” keyword locates the exact location of an object inside the memory, whereas the “==” compares the values of our object. </br> </br>
 
## Exercise: Creating a game:
Snake, Water and Gun is a variation of the children’s game “rock-paper-scissors” where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a snake, water, gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win. </br> </br>
**Game solution (Using if-else statements):**
```
import random
try:
    choices = {0 : "Snake", 1 : "Water", -1 : "Gun"}
    Sn = input("Choose your selection: For Snake press 0, for Water press 1, and for Gun press -1")
    snn = int(Sn)
    cin = random.choice([0, 1, -1])
    print(f"Your selection is : {choices[snn]} , and computer selection is : {choices[cin]}")
    if (snn == cin):
        print("Game is : draw")
    elif (snn == 0) and (cin == 1) or (snn == 1) and (cin == -1) or (snn == -1) and (cin == 0):
        print ("You Win the game")
    else:
        print("Your loss the game")
except KeyError:
    print("You entered an incorrect command, please enter the correct choices")
```
</br> </br>

**Game solution (Without using if-else statements):**
```
import random
try:
    gamere = [["Draw", "Win", "Loss"], ["Loss", "Draw", "Win"], ["Win", "Loss", "Draw"]]
    game = ["Snake", "Water", "Gun"]
    usinp = int(input("Enter Your choice 0 for snake, 1 for Water and 2 for gun : \n"))
    compinp = random.randint(0, 2)
    fingame = gamere[usinp][compinp]
    print(f"\n Your selection is : {game[usinp]}, and Computer selection is : {game[compinp]}")
    print(f"\n You : {fingame}")
except KeyError:1
print("You entered an incorrect command, please enter the correct choices")
```
</br> </br> 
**Game solution (In While-Loop)**
```
import random
try:
    while True:
        gamere = [["Draw", "Win", "Loss"], ["Loss", "Draw", "Win"], ["Win", "Loss", "Draw"]]
        game = ["Snake", "Water", "Gun"]
        usinp = int(input("Enter Your choice 0 for snake, 1 for Water and 2 for gun : \n if You Want to Quit the game press Q \n"))
        compinp = random.randint(0, 2)
        fingame = gamere[usinp][compinp]
        print(f"\n Your selection is : {game[usinp]}, and Computer selection is : {game[compinp]}")
        print(f"\n You : {fingame}")
except ValueError:
    print("Thanks for playing the Game")
except Exception as e:
    print(f"Thanks for playing the Game {e}")
```
</br> </br>
 # Introduction to Object-oriented programming, Classes and Objects in Python, Constructors:
 ### 1.	Introduction to Object-oriented programming:
In programming languages, mainly there are two approaches that are used to write program or code. </br> </br>
1.	Procedural Programming </br>
2.	Object-Oriented Programming </br> </br>
The procedure we are following till now is the “Procedural Programming” approach. So, in this session, we will learn about Object Oriented Programming (OOP). The basic idea of object-oriented programming (OOP) in Python is to use classes and objects to represent real world concepts and entities. </br> </br>
A class is a blueprint or template for creating objects. It defines the properties and methods that an object of that class will have. Properties are the date or state of an object and methods are the actions or behaviors that an object can perform. </br> </br>
An object is an instance of a class, and it contains its own data and methods. For example, we could create a class called “Person” that has properties such as name and age, and methods such as speak() and walk(). Each instance of the Person class would be a unique object with its own name and age, but they would all have the same methods to speak and walk. </br> </br>
One of the key features of OOP in Python is encapsulation, which means that the internal state fo an object is hidden and can only be accessed or modified through the objects methods. This helps to protect the object’s data and prevent it from being modified in unexpected ways. </br> </br>
Another key feature of OOP in Python in inheritance, which allows new classes to be created that inherit the properties and methods of an existing class. This allows for code reuse and makes it easy to create new classes that have similar functionality to existing classes. </br> </br>
Polymorphism is also supported in Python, which means that objects of different classes can be treated as if they were objects of a common class. This allows for greater flexibility in code and makes it easier to write code that can work with multiple types of objects. </br> </br>
In summary, OOP in Python allows developers to model real-world concepts and entities using classes and objects, encapsulate data, reuse code through inheritance, and write more flexible code through polymorphism. </br> </br>
### 2.	Classes and Objects in Python:
A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword. </br> </br>
**a.	Creating a Class:** </br>
Let us now create a class using the class keyword. </br>
**Example:**
```
			Class Details:
				name = “Zeeshan”
				age = 20
```
</br>

**b.	Creating an Object:** </br>
Object is the instance of the class used to access the properties of the class.  </br>
**Example:**
```
			obj1 = Details()
```
</br>
Now we can print the values of the class by the help object. </br>

**Example:**
```
			class Details:
			name = “Zeeshan”
			age = 20

			obj1 = Details()
			print(obj1.name)
			print(obj1.age)
	Output:
			Zeeshan
			20
```
**c.	self parameter:** </br>
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. </br>
It must be provided as the extra parameter inside the method definition. </br>
**Example:**
```
			class Details:
				name = “Zeeshan”
				age = 20

				def desc(self):
					print(“My name is”, self.name, “and I’m”, self.age, “years old.”)
			obj1 = Details()
			obj1.desc()
	Output:
			My name is Zeeshan and I’m 20 years old.
```
</br>

**Practice:**
```
class banda():
    name = "Zeeshan"
    age = 35
    occupation = "developer"
    def insan(self):
        print("The employee name is",self.name, "he is ", self.age, "years old. And he is working as a", self.occupation,".")
a = banda()
b = banda()
b.name = "Fahim Ullah"
b.age = 37
b.occupation = "programmer"
c = banda()
c.name = "Abdul Salam"
c.age = 37
c.occupation = "Entrepreneur"
a.insan()
b.insan()
c.insan()

Output:
        The employee name is Zeeshan he is  35 years old. And he is working as a developer .       
        The employee name is Fahim Ullah he is  37 years old. And he is working as a programmer .  
        The employee name is Abdul Salam he is  37 years old. And he is working as a Entrepreneur .
``` 
</br> </br> 
### 3.	Constructors:
A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when a object of a class is created. </br>
A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of the class. It cannot return any value other than None. </br>
**Syntax of Python Constructor:**
```
							def __init__(self):	# initializations (Dendor method)
```
</br>
init is one of the reserved functions in python. In object oriented programming, it is known as a constructor. We can also create constructor by defining the function name with same class name. </br>

**Syntax:**
```
				Class ABC:
				def ABC(self):	# initializations
```
**Types of Constructors in Python:** </br> 
There are two types of constructors. </br> </br>
a.	Parameterized Constructor </br> 
b.	Default Constructor </br> </br>

**a.	Parameterized Constructor in Python:-** </br>
When the constructor accepts arguments along with self, it is known as parameterized constructor. </br>
These arguments can be used inside the class to assign the values to the data members. </br>
**Example:-**
```
			class Details:
				def __init__(self, animal, group)
					self.animal = animal
					self.group = group
			obj1 = Details(“Crab”, “Crustaceans”)
			print(obj1.animal, “belongs to the”, obj1.group, “group.”)
	Output:
			Crab belongs to the Crustaceans group.
```
**b.	Default Constructor in Python:** </br>
When the constructor doesn’t accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor. </br>
**Example:**
```
			class Details:
				def __init__(self):
					print(“animal Crab belongs to Crustaceans group”)
			obj1 = Details()

	Output:
			Animal Crab belongs to Crustaceans group
```
</br> </br>
**Example 1 of parameterized constructor :**
```
class banda():
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.occupation = c
    def insan(self):
        print("The employee name is",self.name, "he is ", self.age, "years old. And he is working as a", self.occupation,".")
ab = banda("Fahim Ullah", 37, "Developer")
bb = banda("Zeeshan", 38, "developer")
cb = banda("Abdul Salam", 38, "HR")
ab.insan()
bb.insan()
cb.insan()

Output:
        The employee name is Fahim Ullah he is  37 years old. And he is working as a Developer .
        The employee name is Zeeshan he is  38 years old. And he is working as a developer .    
        The employee name is Abdul Salam he is  38 years old. And he is working as a HR . 
```
</br> </br>
**Example 2 of parameterized constructor :**
```
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")

Output:
        Crab belongs to the Crustaceans group.
```
</br> </br>
# Python Decorators, Getters and Setters in Python:
### 1.	Python Decorators:-
Python decorators are a powerful and versatile tool that allow us to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code. </br>
A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a “decorated” function. The basic syntax for using a decorator is the following: </br>
**Example:**			
```		
			@decordor_function
			def my_function():
				pass
```	
The @decorator_function notation is just a shorthand for the following code: </br>
**i.e**
```
			def my_function():
				pass
			my_function = decorator_function(my_function)
```
</br>

**Practical use case:** </br>
One common use of decorators is to add logging to a function. For example, we could use a decorator to log the arguments and return value of a function each time it is called: </br>
**Example:**			
```			
			Import logging
				
			def log_function_call(func):
				def decorated (*args, **kwargs):
					logging.info(f”Calling {func.__name__} with args={args}, kwargs={kwargs}”)
					result = func(*args, **kwargs)
					logging.info(f”{func.__name__} returned {result}”)
					return result
				return decorated
			
			@log_function_call
			def my_function(a, b):
				return a+b
``` 
In the above example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called. </br> </br>
**Conclusion:**
Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making our code more readable and maintainable. </br>
In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memorization, access control, and more. They are a powerful tool that can be used to make our code readable, maintainable and extendable.	</br>	
**Example 1:**
```
def hello(ab):
    def ello(*args, **kwargs):
        print("Lets start the program...")
        ab(*args, **kwargs)
        print("Thanks for comming...")
    return ello
@hello    
def add(a, b):
    print(a + b, "is the sum of these numbers")
@hello
def proud():
    print("Hello World...")

add(4, 5) 
proud()

Output:
        Lets start the program...
        9 is the sum of these numbers
        Thanks for comming...        
        Lets start the program...    
        Hello World...
        Thanks for comming...
```
So, in the above example we just create a decorator function hello() and then we just pass the name of this function to every subsequent functions as mentioned with its name i.e @hello. And by doing this we can see that the start and ending of every of this function will shows us the given text. </br> </br>
**Example 2:**
```
import logging
logging.basicConfig(level=logging.INFO)
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
my_function(1, 2)

Output:
        INFO:root:Calling my_function with args=(1, 2), kwargs={}
        INFO:root:my_function returned 3
```

Here, in the above example we used the logging function.
</br> </br> 
### 2.	Getters and Setters in Python:-
**a.	Getters:-** </br>
Getters in Python are methods that are used to access the values of an object’s properties. They are used to return the value of a specific property, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method. </br>
**Example:**
```
		class MyClass:
			def __init__(self, value):
				self.value = value
			
			@perperty
			def value(self):
				return self.value
```
In the above example, the MyClass class has a single property, _value, which is initialized in the __init__ method. The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property. </br>
To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were attribute:
```
		obj = MyClass(10)
		obj.value
		10
```
</br> </br>
**b.	Setters:-**
It is important to note that the getters do not take any parameters and we cannot set the value through getter method. For that we need setter method which can be added by decorating method with @property_name.setter. Here is an example of a class with both getter and setter: </br>
**Example:**
```
		class MyClass:
			def __init__(self, value):
				self._value = value
		
			@property
			def value(self):
				return self.value

			@value.setter
			def value(self, new_value):
				self._value = new_value
```
We can use setter method like this:
```			
			obj = MyClass(10)
			obj.value = 20
			obj.value
			20
```
In conclusion, getters are a convenient way to access the values of and object’s properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation. </br>

**Example:**
```
class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property                # Getting method using @property decorator
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter       # Setter method using getter decorator (its the decorator of getter)
    def ten_value(self, new_value):
        self._value = new_value/10
    
obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()

Output:
        67.0
        Value is 6.7
```
</br> </br>
# Inheritance in python, Types of Inheritance (Single, Multiple, Multilevel, Hierarchical & Hybrid Inheritance in python):
### Inheritance in python:
When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods, this is called as inheritance. </br>
**Python Inheritance Syntax:**
```
		Class BaseClass:
			Body of base class
		Class DerivedClass(BaseClass):
			Body of derived class
```
**Types of Inheritance:** </br> </br>
There are five types of inheritance used in python: </br>
1.	Single inheritance </br>
2.	Multiple inheritance </br>
3.	Multilevel inheritance </br>
4.	Hierarchical inheritance </br>
5.	Hybrid inheritance </br> </br>
We will see the explanation and example of each type of inheritance below. </br> </br>
		
**1.	Single Inheritance:** </br>
Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code. </br>
**Example:**
```
			class Parent:
				def func1(self):
					print(“This function is in parent class.”)
			class Child(Parent):
				def func2(self):
					print(“This function is in child class.”)
			object = Child()
			object = func1()
			object = func2()
	Output:
			This function is in parent class.
			This function is in child class.
```
</br> </br>
**2.	Multiple Inheritance:** </br>
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class. </br>
**Example:**		
```
		class Mother:
			mothername = “ ”
			
			def mother(self):
				print(self.mothername)
		
		class Father:
			fathername = “ “

			def father(self):
				print(self.fathername)

		class Son(Mother, Father):
			def parents(self):
				print(“Father name is :”, self.fathername)
				print(“Mother :”, self.mothername)

		s1 = Son()
		s1.fathername = “Mommy”
		s1.mothername = “Daddy”
		s1.parents()

Output:
		Father name is : Mommy
		Mother name is : Daddy
```
</br> </br>
**3.	Multilevel Inheritance:** </br> 
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather. </br> </br>
**Example:**
```
				class Grandfather:
					def __init__(self, grandfathername):
						self.grandfathername = grandfathername
			
				class Father(Grandfather):
					def __init__(self, fathername, grandfathername):
						self.fathername = fathername
						Grandfather.__init__(self, grandfathername)

				Class Son(Father):
					def __init__(self, sonname, fathername, grandfathername):
						self.sonname = sonname
						Father.__init__(self, fathername, grandfathername)
					def print_name(self):
						print(‘Grandfather name :’, self.grandfathername)
						print(“Father name :”, self.fathername)
						print(“Son name :”, self.sonname)
				s1 = Son(‘Kashif’, ‘Haris’, ‘Saeed’)
				print(s1.grandfathername)
				s1.print_name()

		Output:
				Kashif
				Grandfather name : Kashif
				Father name : Haris
				Son name : Saeed
```
</br> </br>
**4.	Hierarchical Inheritance:** </br>
When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two (derived) classes. </br>
**Example:**	
```
		Class Parent:
			def func1(self):
				print(“This function is in parent class.”)
			
		class Child1(Parent):
			def func2(self):
				print(“This function is in child 1.”)

		class child2(Parent):
			def func3(self):
				print(“This function is in child 2.”)

		object1 = Child1()
		object2 = Child2()
		object1.func1()
		object1.func2()
		object2.func1()
		object2.func3()
Output:
		This function is in parent class.
		This function is in child 1.
		This function is in parent class.
		This function is in child 2.
```
</br> </br>
**5.	Hybrid Inheritance:** </br>
Inheritance consisting of multiple types of inheritance is called hybrid inheritance. </br>
**Example:**
```
		class School:
			def func1(self):
				print(“This function is in school.”)

		class Student1(School):
			def func2(self):
				print(“This function is in student 1. ”)
		
		class Student2(School):
			def func3(self):
				print(“This function is in student 2. ”)

		class Student3(Student1, School):
			def func4(self):
				print(“This function is in student 3. ”)	

		object = Student3()
		object.func1()
		object.func2()
Output:
		This function is in school.
		This function is in student 1.
```
</br> </br>
**Example 1 of Single inheritance:** </br>
```
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
 
object = Child()
object.func1()
object.func2()

Output:
        This function is in parent class.
        This function is in child class.
``` 
In the above example we called the parent class with the object of child class. Because all the functionalities of parent class bears by the child class. </br> </br>
 
**Example 2 of Multiple Inheritance:** </br>
```
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "Mommy"
s1.mothername = "Daddy"
s1.parents()

Output:
        Father name is : Mommy
        Mother : Daddy 
```
In the above example we created two classes of father and mother and then inherit them in the son class. Then we make the object of son class and with the help of son class we can use the functionalities of father and mother class. </br> </br>
 
**Example 3 of Multi level Inheritance:** </br>
```
class Grandfather:
     def __init__(self, grandfathername):
        self.grandfathername = grandfathername
  
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
s1 = Son('Haris', 'Liaqat', 'Saeed')
print(s1.grandfathername)
s1.print_name()

Output:
        Grandfather name : Saeed
        Father name : Liaqat    
        Son name : Haris  
```
</br> </br>
**Example 4 of Hierarchical Inheritance:** </br>
```
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
      
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
 
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

Output:
        This function is in parent class.
        This function is in child 1.     
        This function is in parent class.
        This function is in child 2.
```
</br> </br> 
**Example 5 of Hybrid Inheritance:** </br>
```
class School:
    def func1(self):
        print("This function is in school.")
  
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
  
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
  
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
object = Student3()
object.func1()
object.func2()

Output:
        This function is in school.
        This function is in student 1.
```
</br> </br>
# Access Specifiers – Modifiers (Public, Private, Protected Access Modifier), Name mangling in python:
### Access Specifiers / Modifiers:
Access specifiers or acces modifiers in python programming are used to limit the acces of class variables and class methods outside of class while implementing the concepts of inheritance. </br> </br>
**Types of access specifiers:** </br>
There are three types of access specifiers. </br> </br>
1.	Public access modifiers </br>
2.	Private access modifiers </br>
3.	Protected access modifiers </br> </br>

**1.	Public Access specifier in Python:** </br> </br>
All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword i.e self.var_name are public accessed. </br>
**Example:**
```
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Haris")
print(obj.age)
print(obj.name)

Output:
        21
        Haris
```
</br> </br>
**2.	Private Access Modifiers:** </br>
By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class. </br>
In Python, there is no strict concept of “private” access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a “weak internal use indicator” and it is a convention only, not a strict rule. Code outside the class can still access these “private” variables and methods, but it is generally understood that they should be accessed or modified. </br>
**Example:**	
```
class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Haris")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())

Output:
        AttributeError: 'Student' object has no attribute '__age'
```
Private members of a class cannot be accessed or inherited outside of class. If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error. </br> </br>
**Name mangling:-**		Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively. Note: if want to check about the requirement of name mangling in any variable name then we can do this by printing it as “variable_name.__dir__”. </br>
**Example:**
```
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
```
In the example above, the attribute _nonmangled_attribute is marked as nonmangled by convention, but can still be accessed from outside the class. The attribute __mangled _attribute is private and its name is “mangled” to _MyClass__mangled_attribute, so it can’t be accessed directly from outside the class, but you can access it by calling _MyClass__mangled_attribute. </br> </br>
**3.	Protected Access Modifier:-** </br>
In object-oriented programming (OOP), the term “protected” is used to describe a member (i.e, a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses. </br>
Its important to note that the single underscoreis just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName. </br>
**Example:** 
```
class Student:
    def __init__(self):
        self._name = "Haris"

    def _funName(self):      # protected method
        return "Gullkhan"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())

Output:
            Haris
            Gullkhan
            Haris   
            Gullkhan
```
</br> </br> </br>
## Exercise: </br>
Write a library class with number of books and books as two instance variables. Write a program to create a library from this library class and show how we can print all books, add a book and get the number of books using different methods. Show that our program does not persist the books after the program is stopped. </br>
```
class Library:
    def __init__(self):
        self.nbooks = 0
        self.books = []
     
    def addbooks(self, book):
        self.books.append(book)
        self.nbooks = len(self.books)

    def show(self):
        print(f"The total books in the library is : {self.nbooks}") 
        print("The name of the books are : ")
        for i in self.books:
            print(i)

l1 = Library()
l1.addbooks("Gulistan e Johar")
l1.addbooks("Salam Software")
l1.addbooks("Ek Din Jeo k sath")
l1.show()

Output:
        The total books in the library is : 3
        The name of the books are :
        Gulistan e Johar
        Salam Software 
        Ek Din Jeo k sath
```
</br> </br>
# Static Methods in Python, Instance vs class variables:
### 1.	Static Methods in Python:-
Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don’t need access to create utility functions that don’t need access to instance data. </br>
**Example:**	
```
		class Math:
			@staticmethod 
			def add(a, b):
				return a + b
		
		result = Math.add(1, 2)
		print(result) 		# Output : 3
```
In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the class itself, without the need to create an instance of the class. Hence, if we asked by someone that is there any need of writing self keyword in a method of a class then the answer is No, because if we don’t want to write the self keyword then we can create a static method. </br>
```
class Math:
    @staticmethod
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result)

Output:
        3
```

 
### 2.	Instance vs class variables:
In python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code. </br> </br>
**a.	Class Variables:** </br>
Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created. </br>
**Example**
```
class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2
```
In the example above, the class_variable is shared among all instances of the class MyClass. When we create new instances of MyClass, the value of class_variable is incremented. When we call the print_class_variable method on obj1 and obj2, we get the same value of class_variable. </br> </br>
**b.	Instance Variables:** </br>
Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.	</br>
**Example**
```
class MyClass:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane
```
In the example above, each instance of the class MyClass has its own value for the name variable. When we call the print_name method on obj1 and obj2, we get different values for name. </br> </br>
**Summary:** </br>
In summary, class variables are shared among all instances of a class and are used to store information that is common to all instances. Instance variables are unique to each instance of a class and are used to store information that is specific to each instance. Understanding the difference between class variables and instance variables is crucial for writing efficient and maintainable code in python. </br>
Its also worth noting that, in python class variables are defined outside of any methods and don’t need to be explicitly declared as class variable. They are defined in the class level and can be accessed via classname.variable_name or self.class.variable_name. But instance variables are defined inside the methods and need to be explicitly declared as instance variable by using self.variable_name. </br> </br>
**Example:** </br>
```
class Student:
    Institute = "CSUniversity"  # This is a class variable.
    def __init__(self, name):
        self.name = name
        self.level = 14

    def show(self):
        print(f"The name of student is {self.name} and studying in class {self.level} of {self.Institute}")

s1 = Student("Haris")
s1.show() 
s2 = Student("Rizwan")
s2.level = 16
s2.show()

Output:
        The name of student is Haris and studying in class 14 of CSUniversity
        The name of student is Rizwan and studying in class 16 of CSUniversity
```
As we can see in the above example that just after the class declaration we created a class variable which is used for all the instances of the classes unless we makes any change for any particular object. </br> </br>
# Exercise: (Clear the clutter using os module):
Write a program to clear the clutter inside a folder on our computer. We should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. We have to do the same for other file formats. </br> </br>
### We can create a file in a folder using under mentioned way:
```
import os
os.makedirs(r"D:\folderi", exist_ok=True)
# fst_path = "D:\folderi\abc"
for i in range(0, 100):
    with open(fr"D:\folderi\abc{i+1}.png", "w") as f:
        f.write("Hello this file is in folderi!!")
```

### Now we can rename the already named files in sequential manner:
```
import os
for i in range(0, 100):
    if os.path.exists(fr"D:\folderi\abc{i+1}.png"):
        os.rename(fr"D:\folderi\abc{i+1}.png", fr"D:\folderi\{i+1}.png")
```
</br> </br>
# Python Class Methods, Class Methods as Alternative Constructors, dir(), __dict__ and help() methods in python:
### 1.	Python Class Methods:
In Python, classes are a way to define custom data types that can store data and define functions that can manipulate that data. One type of function that can be defined within a class is called a “method”. </br> </br>
**a.	What are Python Class Methods ?** </br>
A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the “@classmethod” decorator, followed by a function definition. The first argument of the function is always “cls,” which represents the class itself. </br> </br>
**b.	Why Use Python Class Methods ?** </br>
Class methods are useful in several situations. For example, you might want to create a factory method that creates instances of our class in a specific way. We could define a class method that creates the instance and returns it to the caller. Another common use case is to provide alternative constructors for your class. This can be useful if we want to create instances of our class in multiple ways, but still have a consistent interface for doing so. </br> </br>
**c.	How to Use Python Class Methods ?** </br>
To define a class method, we simply use the “@classmethod” decorator before the method definition. The first argument of the method should always be “cls,” which represents the class itself. Here is an example of how to define a class method: </br>
**Example:**		
```
		class ExampleClass:
			@classmethod
			def factory_method(cls, argument1, argument2):
				return cls(argument1, argument2)
```
In this example, the “factory_method” is a class method that takes two arguments, “argument1” and “argument2”. It creates a new instance of the class “ExampleClass” using the “cls” keyword, and returns the new instance to the caller. </br>
It is important to note that class methods cannot modify the class in any way. If we need to modify the class, we should use a class level variable instead. </br> </br>
**Conclusion:**	</br>	
Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class. They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level. With the knowledge of how to define and use class methods, we can start writing more complex and organized code in python. </br> </br>
**Example: (Use of @classmethod):** 
```
class employee:
    company = "Apple"
    def show(self):
        print(f"The employee name is {self.name} and a hardworking in {self.company} company")
    
    @classmethod
    def anothercomp(cls, anocomp):
        cls.company = anocomp
    
emp1 = employee()
emp1.name = "Fahim"
emp1.show()
emp1.anothercomp("Amazon")
emp1.show()
print(employee.company)

Output:
        The employee name is Fahim and a hardworking in Apple company
        The employee name is Fahim and a hardworking in Amazon company
        Amazon
```
Here, in the above example we created a simple class and defined a show() method. Here in the class we create a variable company=Apple, so when we access this class with anothermehod() method we can change the company with given changed company name. But here the class variable company name will remains Apple will never effect any change in the class variable. However, if we use the @classmethod decorator we can change the class variable as we can see in the above example the class variable has been changed. </br> </br>
### 2.	Class Methods as Alternative Constructors:
In object-oriented programming, the term “constructor” refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object’s attributes, allowing the object attributes, allowing the object to be fully functional and ready to use. </br>
However, there are times when we may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructors. </br>
A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when we want to create an object from data that is stored in a different format, such as a string or a dictionary. For example, consider a class name “Person” that has two attributes “name” and “age”. The default constructor for the class might look like this: </br> </br>
**Example:**
```
	class Person:
    		def __init__(self, name, age):
        			self.name = name
        			self.age = age
```
But what if we want to create a Person object from a string that contains the person’s name and age, separated by a comma? We can define a class method named “from_string” to do this: </br> </br>
**Example:**
```
		class Person:
    		def __init__(self, name, age):
      			self.name = name
        		self.age = age

    	@classmethod
   		def from_string(cls, string):
        			name, age = string.split(',')
      				return cls(name, int(age))
```
</br>
Now we can create a Person object from a string like this: </br>

**Example:**
```
	person = Person.from_string(“Fahim, 36”)
```
</br>
Another common use case for class methods as alternative constructors is when we want to create an object with a different set of default values than what is provided by the default constructor. For example, consider a class named “Rectangle” that has two attributes: “width” and “height”. The default constructor for the class might look like this: </br>

**Example:**
```
		class Rectangle:
    		def __init__(self, width, height):
        			self.width = width
        			self.height = height
```
</br>
But what if we want to create a rectangle object with a default width of 10 and a default height of 5? We can define a class method named “square” to do this: </br>

**Example:**
```
	class Rectangle:
 		 def __init__(self, width, height):
    			self.width = width
    			self.height = height

  		@classmethod
  		def square(cls, size):
    			return cls(size, size)
```
</br>
Now we can create a square rectangle like this:
```
	rectangle = Rectangle.square(10) 
```
</br> </br>

**Example of Alt Constructors (Alternative Constructors):**
```
class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fstri(cls, stri):
        return cls(stri.split("-")[0], int(stri.split("-")[1]))

emp1 = employee("Fahim Ullah", 36)
print(emp1.name)
print(emp1.age)

stri = ("Haris Jan-30")
emp2 = employee.fstri(stri)
print(emp2.name)
print(emp2.age)

Output:
        Fahim Ullah
        36       
        Haris Jan
        30 
``` 
</br> </br>
### 3.	dir(), __dict__ and help() methods in python:
The above mentioned methods makes it easy for us to understand how classes resolve various functions and executes code. In python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help(). Lets take a look at each of them: </br> </br>
**a.	The dir() method:** </br>
The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what we can do with an object. </br>
**Example:**
```
		x = [1, 2, 3]
		print(dir(x))

Output:

['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', </br>'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```
</br>

**a.	The __dict__ attribute:** </br>
The __dict__ attribute returns a dictionary representation of an object’s attributes. It is a useful tool for introspection. </br>
**Example:**
```
class Person:
    def __init__(self, name, age):
    self.name = name
    self.age = age
 
p = Person("John", 30)
p.__dict__

Output:
		{'name': 'John', 'age': 30}
```
</br> </br>
**3.	The help() method:** </br>
The help() function is used to get help documentation for an object, including a description of its attributes and methods. </br> 
**Example:**
```
help(str)
 	Help on class str in module builtins:

 	class str(object)
 	| str(object='') -> str
 	| str(bytes_or_buffer[, encoding[, errors]]) -> 
str
|
| Create a new string object from the given object. If encoding or
| errors is specified, then the object must expose a data buffer
| that will be decoded using the given encoding and error handler.
| Otherwise, returns the result of object.__str__() (if defined)
| or repr(object).
| encoding defaults to sys.getdefaultencoding().
| errors defaults to 'strict'.
```
</br>
In conclusion, dir(), dict, and help() methods are useful built-in functions in Python that can be used to get information about objects. They are valuable tools for introspection and discovery. </br>
</br>

# Super keyword in Python, Magic - Dunder Method in Python, Method Overriding in Python, Operator Overloading in Python:
### 1.	Super keyword in Python:
In super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and we want to call a method from one of the parent classes. </br> 
When a class inherits from a parent class, it can override or extend the methods defined in the parent class method in the child class. This is where the super() keyword comes in handy. </br> </br>
Here’s an example of how to use the super() keyword in a simple inheritance scenario: </br>
**Example:**
```
			class ParentClass:
    				def parent_method(self):
       				 print("This is the parent method.")

			class ChildClass(ParentClass):
    				def child_method(self):
       				print("This is the child method.")
        				super().parent_method()

			child_object = ChildClass()
			child_object.child_method()

Output:
			This is the child method.
			This is the parent method.
```
In this example, we have a ParentClass with a parent_method and ChildClass that inherits from ParentClass and overrides the child_method. When the child_method is called, its first prints “This is the child method.” and then calls the parent_method using the super() keyword. </br>
The super() keyword is also useful when a class inherits from multiple parent classes. In this case, we can specify the parent class from which we want to call the method. </br>
**Example:**
```
			class ParentClass1:
    				def parent_method(self):
        				print("This is the parent method of ParentClass1.")

			class ParentClass2:
   					def parent_method(self):
        				print("This is the parent method of ParentClass2.")

			class ChildClass(ParentClass1, ParentClass2):
    				def child_method(self):
       					print("This is the child method.")
        				super().parent_method()

			child_object = ChildClass()
			child_object.child_method()
Output:
			This is the child method.
			This is the parent method of ParentClass1.
```
In the this example, the ChildClass inherits both ParentClass1 and ParentClass2. The child_method calls the parent_method of the first parent class using the super() keyword. </br>
In conclusion, the super() keyword is a useful tool in python when we want to call a parent class method in a child class. It can be used in inheritance scenarios with a single parent class or multiple parent classes. </br> </br>
**Example of Super keyword:**
```
class Manager:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class Employee(Manager):
    def __init__(self, name, age, id, lang):
        super().__init__(name, age, id)
        self.lang = lang

a = Manager("Abdul Salam", "38", "1")
print(a.name)
print(a.age)
print(a.id)
print("------------------")
b = Employee("Fahim Ullah", "37", "5", "Python")
print(b.name)
print(b.age)
print(b.id)
print(b.lang)

Output:
            Abdul Salam
            38
            1
            ------------------
            Fahim Ullah
            37
            5
            Python
```
### 2.	Magic / Dunder Method in Python:
These are special methods that we can define in our classes, and when invoked, they give us a powerful way to manipulate objects and their behavior. </br>
Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow us to customize the behavior of our classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties. </br> </br>
Let’s take a look at some of the most commonly used magic methods in Python. </br>
**a.	__init__ methods:** </br>
The init method is a special method that is automatically invoked when we create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where we would typically define any instance variables that we need. Also called “constructor”, we have discussed this method already. </br> </br>
**b.	__str__ and __repr__ methods:** </br>
The str and repr methods are both used to convert an object to a string representation. The Str method is used when we want to print out an object, while the repr method is used when we want to get a string representation of an object that can be used to recreate the object. </br> </br>
**c.	__len__ method:** </br>
The len method is used to get the length of an object. This is useful when we want to be able to find the size of a data structure, such as a list or dictionary. </br> </br>
**d.	__call__ method:** </br>
The call method is used to make an object callable, meaning that we can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows us to create objects that behave like functions. </br>
These are just a few of the many magic methods available in Python. They are incredibly powerful tools that allow us to customize the behavior of our objects, and can make our code much cleaner and easier to understand. So if we are looking for a way to take our python code to the next level, we have to take some time to learn about these magic methods. </br> </br> </br> </br>
### 3.	Method Overriding in Python:
Method overriding is a powerful feature in object-oriented programming that allows us to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When we create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class. </br>
In Python, method overriding is a way to customize the behavior of a class based on its specific needs. For example the following base class. </br> </br>
**Example:**
```
		class Shape:
			def area(self):
				pass
```
In this base class, the area method is defined, but does not have any implementation. If we want to create a derived class that represents a circle, we can override the area method and provide an implementation that calculates the area of a circle:</br> 
**Example:**
```
		class Circle(Shape):
    			def __init__(self, radius):
        				self.radius = radius

    		def area(self):
        			return 3.14 * self.radius * self.radius
```
In this example, the Circle class inherits from the Shape class, and overrides the area method. The new implementation of the area method calculates the area of a circle, based on its radius. </br>
It’s important to note that when we override a method, the new implementation must have the same method signature as the original method. This means that the number and type of arguments, as well as the return type, must be the same. </br>
Another way to customize the behavior of a class is to call the base class method from the derived class method. To do this, we can use the super function. The super function allows us to call the base class method from the derived class method, and can be useful when we want extend the behavior of the base class method, rather than replace it. </br>
**For example, consider the following base class:**
```
		class Shape:
    			def area(self):
       				print("Calculating area...")
```
In this base class, the area method prints a message indicating that the area is being calculated. If we want to create a derived class that represents a circle, and we also want to print a message indicating the type of shape, we can use the super function to call the base class method, and add our own message. </br>
**Example:**
```
			class Circle(Shape):
    			def __init__(self, radius):
        				self.radius = radius

    			def area(self):
        				print("Calculating area of a circle...")
        				super().area()
        				return 3.14 * self.radius * self.radius
```
In this example, the circle class overrides the area method, and calls the base class method using the super function. This allows us to extend the behavior of the base class method, while still maintaining its original behavior. </br>
In conclusion, method overriding is a powerful feature in Python that allows us to customize the behavior of a class based on its specific needs. By using method overriding, we can create more robust and reliable code, and ensure that our classes behave in the way that we need them to. Additionally, by using the super function, we can extend the behavior of a base class method, rather than replace it, giving us even greater flexibility and control over the behavior of our classes. </br> </br>
 
## Exercise : 
Write a program to manipulate pdf files using pyPDF. Our programs should be able to merge multiple pdf files into a single pdf. We are welcome to add more functionality. </br> </br>
Pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. Pypdf can retrieve text metadata from PDFs as well. </br>
```
from pypdf import PdfWriter

merger = PdfWriter()
pdfs = ["Deep-01.pdf", "Deep-02.pdf"]
for pdf in pdfs:
    merger.append(pdf)

merger.write("finalpdf.pdf")
merger.close()
print("Your merger is successfully done...")
```
In the above example we have two files “Deep-01.pdf” and “Deep-02.pdf”. So with the help of pypdf library we import PdfWriter which is used to access the pdf module. How with such simple lines of code we can merge our pdf files. </br> </br>
 
### 4.	Operator Overloading in Python:
Operator overloading is a feature in Python that allows us to redefine the behavior of mathematical and comparison operators for custom data types. This means that we can use the standard mathematical operators (+, -, *, / etc) and comparison operators (>, <, ==, etc) in our own classes, just as we do for built-in data types like int, float, and str. </br> </br>
**a.	Why do we need operator overloading ?**
Operator overloading allows us to create more readable and intuitive code. For instance, consider a custom class that represents a point in 2D space. We could define a method called ‘add’ to add two points together, but using the + operator makes the code more concise and readable.
```
			p1 = Point(1, 2)
			p2 = Point(3, 4)
			p3 = p1 + p2
			print(p3.x, p3.y)	 # prints 4, 6
```
</br>

**b.	How to overload an operator in Python ?** </br>
We can overload an operator in python by defining special methods in our class. These methods are identified by their names, which start and end with double underscores ( __ ). Here are some of the most commonly overloaded operators and their corresponding special methods. </br> </br>
```
			+ : __add__
			- : __sub__ 
			* : __mul__
			/ : __truediv__
			< : __lt__
			> : __gt__
			== : __eq__
```	
For example, if we want to overload the + operator to add two instances of a custom class, we would define the add method. </br>
**Example:**
```
			class Point:
    				def __init__(self, x, y):
        					self.x = x
        					self.y = y

    				def __add__(self, other):
        					return Point(self.x + other.x, self.y + other.y)	
```
It’s important to note that operator overloading is not limited to the built-in operators, we can overload any user-defined operator as well. </br> </br>

**Conclusion:** </br>
Operator overloading is a powerful feature in python that allows us to create more readable and intuitive code. By redefining the behavior of mathematical and comparison operators for custom data types, we can write code that is both concise and expressive. However, its important to use operator overloading wisely, as overloading the wrong operator or using it inappropriately can lead to confusing or unexpected behavior. </br> </br>

## Exercise:
```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return (f"{self.x}, {self.y}")

a = Point(2, 3)
print(a)
b = Point(4, 5)
print(b)
print(a + b)

Output:
            2, 3
            4, 5
            6, 8
```
</br> </br>
