# 🐍 Python Course Tips

A practical collection of Python learning tips, examples, and resources for beginners and intermediate learners.

## 📚 Table of Contents

- [Overview](#overview)
- [Learning Tips](#learning-tips)
- [Modules](#modules)
- [Code Examples](#code-examples)
- [Docstring Example](#docstring-example)
- [Common Mistakes](#common-mistakes)
- [Useful Resources](#useful-resources)
- [Practice Checklist](#practice-checklist)

## Overview

This repository contains notes and advice gathered while learning Python.

Topics include:

- Variables
- Functions
- Loops
- OOP

## 💡 Learning Tips

- Practice every day, even 20 minutes.
- Focus on understanding concepts instead of memorizing.
- Debug code yourself before searching online.
- Build mini projects.
- Read other people's code.
- Write comments and docstrings.

## Modules

### Data Types

- There are only two types of data:
    - Primitive: `str`, `int`, `float`, `bool`
        - These are immutable data types
        - End result of a data processing is always primitive.
    - Non-primitive (collections): `list`, `tuple`, `set`, `dict`
        - These are collective datas.
        - Elements of a collection is always primitive data types
        - **List**
            - Represented by `[]`
            - Elements are separated by `,`
            - List contains primitive and non-primitive data types.
            - List is mutable, ordered, reliable and indexed.
            - Index starts from 0.
            - Since list is mutable, supported methods are: `append()`, `pop()`, `remove()`, `count()`, `insert()` etc.
            - Used for sequence of operations where order matters such as rocket science, shopping cart etc.
            - Example: `my_list = ["name", 12, 2.02, True, ["apple", "grape"], (), {}]`
        - **Tuple**
            - Tuple is same as list, but immutable.
            - So, only `count()` & `index()` is supported
            - Ordered, indexed, reliable.
            - Used for immutable use cases such as IMEI data in phones, Chasis number in vehicles, Founder name etc.
            - Example: `my_tuple = ("name", 12, 2.02, True, [], {})`
        - *SET*
            - Unlike list, set is disordered, non index, unreliable, but elements are unique.
            - This dataset can be used if your data should be unique, like the voter id system
            - Since its disordered and unique,  no `index()`, no `count()`, no `append()`,  methods.
            - Since there is no index, cannot edit any elements in a certain index position. Thereby, mutable elements such as <mark>list, set or dict cannot be an element of set</mark>.
            - Example: `my_set = {"string", 12, 3.5, True, ()}`
        - *DICT*
            - These are called as `json` in other languages.
            - This data type doesn't have indexes.
            - The elements are key-value pairs.
            - The keys are always string and should be unique. The value can be any data type.
            - The key and value are separated by `:`
            - The keys makes the data meaningful
            - Unlike list, to get the value, we need to know the key.
            - Example: {"name": "abuharis"}

### CRUD Operations on Data Types

- Since primtives and tuple are immutable, no CRUD available for them.
- CRUD is only applicable to mutable data types.
- CRUD stands for Create, Read, Update, Delete. The only 4 methods to manipulate any data.

**CRUD on List**
```python
my_list = ["apple", 12, 2.3, True, ["phones", "laptops"]]

# Read by Index. Index starts from 0. So first element is in 0th position.
print(my_list[0])

# This can be sliced to get a range of values.
print(my_list[:3])


# Update Operation does update the element in a certain index.

my_list[0] = "new value"
my_list.append("last element")
my_list.insert(0, "add element to the first position")

# Delete

my_list.remove("element)
my_list.pop()
my_list.clear()
del my_list # This deletes the entire list object
```

**CRUD on Set**

```python
# Since no index in set, cant read an element.

# Update: Since no index, append wont work, only add()

my_set = {}

my_set.add("add this")

# Delete
my_list.pop()
my_set.clear()
```

**CRUD on Dict**

```python
# Read: To get the value, need the key.

my_dict = {"name": "Nexverse", "found_on": 2025}

my_dict["name"]

# Update: There are two methods. 

# If only one element change, use the following syntax.
my_dict["name"] = "New Name"

# If there is multiple data, use update()

my_dict.update({"location": "Calicut", "industry": "IT"})

# Delete based on the key
my_list.remove("location")
my_list.clear()
```

### Operators

- There are only 6 operators in python:
    - Arithmetic: To do mathematical calculations
    - Assignment: Value assignments. `a = b`, `a += b`
    - Comparison: Compare values  
    - Logical: When multiple conditions occurs and concatinated by `and ` `or` or `not`. `1 > 2 and 2 < 4`
    - Memebership: To check an element is inside a collection. `"abuharis" in register`
    - Identity: To check if the values points to the same memory location. `a is b`
- The last 4 only returns `bool` as response, so that can be used inside the decision-making statements

### Loops
- Two loops: `for` and `while`
- Use `for`, when the data is finite.
- Use `while`, when the iteration is based on a condition. 

### Functions

- Variables and functions are used for flexibility and reusability.
- `retrun` keyword is used with the functions only.
- Any type of data can be returned.
- The `return` keyword exits the function. So placement should be on the right place.
- If a condition is used, return when you get an answer
```python
def test_function():
    if True:
        return "success"
    return "failure"
```
- If the condition is within a loop, return when you get what you want.
```python
def return_inside_loop():
    reception = ["apple", "orange", "grape"]
    result = []
    for name in reception:
        if name == "apple":
            result.append(name)
    return result
```
- Function becomes flexible when it takes parameters.
- Parameters are passed inside the paranthesis.
- Paramaters are variables passed during the definition and Arguments are values passed during the execution.
- The order of parameters is as: `positional`, `default`, `*args`, `keyword-only`, `**kwargs`
- The keyword arguments are passed as key=value.
```python
def param_func(**kwargs):
    print(kwargs)

param_func("name"="nexverse")
```

### Modules & Packages

#### Modules
- Module is any file with `.py` extension
- Module contains variables, functions, classes. These are called as attributes.
- These attributes are stored inside a `dict` called as namespaces.
- Namespaces are of  types: two main ns are global and local
- local namespace contains the attributes defined inside a function and this namespace is ephemeral.
- global namespace is a live dicy, which is the default namespace of a module.
- locals() becomes globals() when local doesnt contain anything.

#### Packages

- When two or more modules inside a folder is called packages.
- `__init__.py` controls a package
- Custom packages must created in the root folder of a project.

#### Types of Import

- Modules makes the code organized into smaller units, which makes python modular.
- To reuse a module, we use `import` keyword to load into another module.
- There are 4 types of import:
    - `import module`: This loads the entire attributes. No name conflicts here.
    - `from module import feature`: This takes only the feature, but can cause name conflicts
    - `from module import feature as f`: This solves the above problem by aliasing the conflict.
    - `import module as m`: This is used to use conventions or to shorten the module name
    - `from module import *`: This is not recommended since the conflicts are complex to manage.

### OOP

- This technique is used when:
    - data and behavior is tightly couples
    - data protection is required
    - need to avoid duplication
- When OOP is used, it must be SOLID compliant.
- `class` is a design and objects are the realities
- `self` is the object itself and used wherever object behavior is used.
- class attributes are global contained in each object while object attributes are only limited to objects.
- The data can only be accessed throgh methods. This is called as encapsulation.
- `__init__()` method is used to configure the objects during the initial execution.
```python
class Phone:
    brand = "apple"
    def __init__(self, color):
        self.color = color
    
    def find_the_brand(self):
        print(__class__.brand)
```

# Nomenclature Standards in Python
- variables and functions must be:
    - In lowercase
    - Descriptive
    - Do not use reserved keywords
    - Words separated by `_`
```python
this_is_my_variable = 12
def this_is_my_function():
    pass
```
- Class must be named of PascalCode
```python
class MyClass:
    pass
```

## Useful Resources

- https://www.youtube.com/watch?v=m6AX0NkUxGM&list=PLsCyGxgcysDHPwNw8448VzcFncne_JWuC
