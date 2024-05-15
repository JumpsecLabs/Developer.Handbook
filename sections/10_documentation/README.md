# Documentation
## Code Documentation
- python must use type hints

Instead of 
```python
def greet(user, age):
    return greeting.format(user, age)
```

use 

```python
def greet(user: str, age: int) -> str:
    return greeting.format(user, age)
```

you can make use of `from typing import Dict, Optional, Union`, though that depends on the python intepreter that you are using. 

- Consider [mypy](https://github.com/python/mypy) for typing enforcing

- use docstrings, these can be constructed automatically with [Autodocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) in VSCode for python

- to check for missing docstrings you can use [interrogate](https://interrogate.readthedocs.io/en/latest/#why-do-i-need-this)

- we follow the Google Docstrings format
  
```python
"""Gets and prints the spreadsheet's header columns

Args:
    file_loc (str): The file location of the spreadsheet
    print_cols (bool): A flag used to print the columns to the console
        (default is False)

Returns:
    list: a list of strings representing the header columns
"""
```

## Project Documentation

- Every repository must have a `README.md`

- if a README.md is not enough, consider an automatic documentation for developers by using Sphynx

- If the project leaves the PoC stage and more people get involved it must have a `HOW_TO_CONTRIBUTE.md` file or section within the `README.md` 

- in case the repository is public, it also needs  
  - CONTRIBUTORS
  - LICENSE
