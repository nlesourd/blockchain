# Implementation of blockchain system 

This folder covers the implementation of secure transactions using blockchain system. 

There are four python files:
- `rsa.py`: python file containing the implementation of RSA encryption.
- `blockchain.py`: python file containing the implementation of blockchain system.
- `gui.py`: python file containing the implementation of the graphic user interface in order to do use cases of secure transactions using blockchain system. 
- `public_test.py`: python file used to test the correct operation of the algorithms in `blockchain.py` and in `rsa.py`.

## Required libraries

All the libraries in the list below must be on your machine in order to run the two python files.

- pytest
- rsa
- time
- itertools
- hashlib
- customtkinter
- tkinter
- random
- string

If you don't have one of these libraries, you can install it using the python pip package manager.

`pip install <librarie's name>`

Or using requirements.txt like this:

`pip install -r requirements.txt`

## Run the code

Open a terminal in the A3 folder. You can then enter the following instruction to run the graphic user interface:

`python3 gui.py`

## Test the code

In orer to test the code, you have to enter the following intsruction always in a terminal in the A3 folder:

`pytest public_test.py`