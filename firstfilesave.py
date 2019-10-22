Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=3
>>> b=2
>>> print(a*b,a-b,a+b,a**b,a/b,a//b)
6 1 5 9 1.5 1
>>> z=false
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    z=false
NameError: name 'false' is not defined
>>> type(z)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(z)
NameError: name 'z' is not defined
>>> is_android=false
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    is_android=false
NameError: name 'false' is not defined
>>> z=False
>>> type(z)
<class 'bool'>
>>> print(10//4)
2
>>> 
>>> print(z==True)
False
>>> print(z==False)
True
>>> name='iPhone'
>>> print(name + 'supports android')
iPhonesupports android
>>> for i in range(5):
	print(i,i**2)

	
0 0
1 1
2 4
3 9
4 16
>>> range?
SyntaxError: invalid syntax
>>> i=0
>>> while i<5 :
	print(i,i**2)
	i+=1

	
0 0
1 1
2 4
3 9
4 16
>>> 
>>> def print_squares(s_val):
	for i in range(s_val):
		print(i,i**2)

		
>>> print_squares(6)
0 0
1 1
2 4
3 9
4 16
5 25
>>> print_squares(2)
0 0
1 1
>>> def print_square_with_startval(s_val,st_val=0):
	for i in range(s_val,st_val):
		print(i,i**2)

		
>>>  print_square_with_startval(5,8)
SyntaxError: unexpected indent
>>>  print_square_with_startval(5,8)
SyntaxError: unexpected indent
>>> print_square_with_startval(5,8)
5 25
6 36
7 49
>>> myphone=[name,is_android,screem_size]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    myphone=[name,is_android,screem_size]
NameError: name 'is_android' is not defined
>>> is_android=yes
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    is_android=yes
NameError: name 'yes' is not defined
>>> 
>>> is_android='yes'
>>> screensize=6.0
>>> myphone=[name,is_android,screem_size]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    myphone=[name,is_android,screem_size]
NameError: name 'screem_size' is not defined
>>> myphone=[name,is_android,screensize]
>>> type(myphone)
<class 'list'>
>>> print(myphone)
['iPhone', 'yes', 6.0]
>>> print(myphone[0])
iPhone
>>> type(myphone[])
SyntaxError: invalid syntax
>>> type(myphone[0])
<class 'str'>
>>> type(myphone[2])
<class 'float'>
>>> print(myphone[0:2])
['iPhone', 'yes']
>>> mynphone=myphone
>>> print(mynphone)
['iPhone', 'yes', 6.0]
>>> print(myphone)
['iPhone', 'yes', 6.0]
>>> print(mynphone)
['iPhone', 'yes', 6.0]
>>> myphone[2]=5.8
>>> print(myphone)
['iPhone', 'yes', 5.8]
>>> print(mynphone)
['iPhone', 'yes', 5.8]
>>> mynphone=list(myphone)
>>> myphone[2]=4.5
>>> print(myphone)
['iPhone', 'yes', 4.5]
>>> print(mynphone)
['iPhone', 'yes', 5.8]
>>> len(myphone)
3
>>> len/
SyntaxError: invalid syntax
>>> len?
SyntaxError: invalid syntax
>>> len ?
SyntaxError: invalid syntax
>>> myphone.append(3g)
SyntaxError: invalid syntax
>>> myphone.append('3g')
>>> print(myphone)
['iPhone', 'yes', 4.5, '3g']
>>> len(myphone)
4
>>> myiphone=['ssim',3600]
>>> myphone+=myiphone
>>> print(data)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(data)
NameError: name 'data' is not defined
>>> print(myphone)
['iPhone', 'yes', 4.5, '3g', 'ssim', 3600]
>>> a=list(range(5))
>>> print(a)
[0, 1, 2, 3, 4]
>>> b=list(map(lambda x:x**2,a))
>>> print(b)
[0, 1, 4, 9, 16]
>>> 
