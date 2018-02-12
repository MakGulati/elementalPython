So, how are lists different from strings? The obvious difference is that strings are sequences of letters, while list elements can be any type of object. A more subtle difference is that lists can be modified, but strings can't be:

>>> sample_list[3] = 'Eric'
>>> print(sample_list)
['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
>>> sample_string[8] = 'f'
TypeError: 'str' object does not support item assignment
The technical term for whether an object can be modified is mutability. Lists are mutable, while strings are immutable. Next we'll explore the methods and functions that work on lists, and we'll take advantage of list mutability in our programs.

