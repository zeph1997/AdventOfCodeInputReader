# AdventOfCodeInputReader

# <p align="center">AdventOfCodeInputReader</p>

<p align="center">A python package to get the input for Advent Of Code challenges as a list</p>

## Getting Started

* Installation using pip (Python Package Index):

```
$ pip install AdventOfCodeInputReader
```

## Using AdventOfCodeInputReader

### Import and Initialise

The AdventOfCode class (defined in __init__.py) has one mandatory parameter (`session_id`) and two optional parameters (`year` and `day`). To get `session_id`, you need to log into Advent of Code and retreieve the session id from your browser cookies. Your session id is required as the challenge input is different for each user.

```python
from AdventOfCodeInputReader import AdventOfCodeInputReader

# Initialize with only session_id
reader = AdventOfCodeInputReader("your_session_id")

# Initialize with session_id and year only
reader = AdventOfCodeInputReader("your_session_id",2021)

# Initialize with session_id and year and day
reader = AdventOfCodeInputReader("your_session_id",2021,1)

```

## Methods

The AdventOfCode class has three methods: `get_input()`, `get_input_by_day()`, `get_input_by_year_and_day()`. All three methods will return a list of strings, with each line of the input as an element in the list.

### get_input()

The `get_input(day=None, year=None)` method has two optional parameters, `day` and `year`. If you have specified the values for `day` and `year` at initalization, you can use this method without any arguments. If you have included values for `day` and `year` at initization but included `day` and `year` arguments for `get_input()`, the method will override and use the arguments provided in `get_input()` for this specific run only. It will not update the class value.

```python
# Using get_input() with year and day specified at initalization
reader = AdventOfCodeInputReader("your_session_id",2021,1)
input = reader.get_input()

# Using get_input() with only year specified at initalization
reader = AdventOfCodeInputReader("your_session_id",2021)
input = reader.get_input(day=1)

# Using get_input() without year and day specified at initalization
reader = AdventOfCodeInputReader("your_session_id")
input = reader.get_input(day=1,year=2021)

```

This method returns a list of strings, with each line of the input as an element in the list.

If the input from Advent of Code looks like:
```
line 1
line 2
line 3
```
The method will return:
```
["line 1", "line 2", "line 3"]
```

### get_input_by_day()

The `get_input_by_day(day)` method requires the `year` to be declared at initialization. If you have included value for `day` at initization but included `day` argument for `get_input_by_day()`, the method will override and use the argument provided in `get_input_by_day()` for this specific run only. It will not update the class value.

```python
reader = AdventOfCodeInputReader("your_session_id",2021)
input = reader.get_input_by_day(1)

```

This method returns a list of strings, with each line of the input as an element in the list.

If the input from Advent of Code looks like:
```
line 1
line 2
line 3
```
The method will return:
```
["line 1", "line 2", "line 3"]
```

### get_input_by_year_and_day()

The `get_input_by_year_and_day(year, day)` method requires the `year` and `day` arguments to be specified when using the method. If you have included value for `year` or `day` at initization, the `year` and `day` arguments provided will be used instead of the values specified at initalization for this specific run only. It will not update the class value.

```python
reader = AdventOfCodeInputReader("your_session_id")
input = reader.get_input_by_year_and_day(year=2021,day=1)

```

This method returns a list of strings, with each line of the input as an element in the list.

If the input from Advent of Code looks like:
```
line 1
line 2
line 3
```
The method will return:
```
["line 1", "line 2", "line 3"]
```