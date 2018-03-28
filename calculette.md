# Python interpreter

- IDLE or cmd and type `py` (or `py -3` or `py -3.6`) or <em>anywhere</em>, you always have it.
- Begins with `>>>`
- `_` for last
- Up Down for history (except in IDLE where you can move the cursor, **then** press `Enter` to copy current line, or use shortcut `Alt+P`)
- Enter to execute (the cursor can be anywhere)
- On limac, type `python3` (because `python` is generally `python2`, can create an alias like `py`)
- Home et End are useful
- `help(...)` and `<Tab>` to autocomplete stuffs

# ipython install
Ipython is a better interactive python,
but can also be used for basic interactive python
(meaning you can start with this one, it's just that it will not always be there 
because you must install it or run it [online](http://www.techbeamers.com/best-python-interpreter-execute-python-online/)).

Embedded in scientific python environments, like Anaconda (and therefore the Spyder IDE).

Loads a little bit slower than the classic interpreter, but you rarely need two tabs opened anyway.

## windows
- run `py -3 -m pip install ipython`
- type execute > appdata > Local > Programs > Python > Python36-32 > Scripts > ipython.exe
- double click to launch, can create shortcut and attach it to windows bar
- font 16
- copy with right click only, paste with ctrl+v

## limac (linux & macOS)
- run `python3 -m pip install ipython`
- Open terminal, type ipython (or ipython3)

## android
- termux and then follow limac instructions

# ipython functionalities

- `_` for last
- `_n` for out number N (eg. `_18`)
- `__` `___` for over last and over over last
- `_8` `_i8`
- `In `, `Out` instead of `>>>`
- Up/Down for history prev/next
- Type `a =` UpDown for quick find in history (otherwise use the `%hist -g` hack)

# See also

- http://ipython.org/ipython-doc/stable/interactive/reference.html#input-caching-system
- http://ipython.org/ipython-doc/stable/interactive/reference.html#output-caching-system
- https://www.ics.uci.edu/~dock/manuals/IPython/node6.html
- http://www.techbeamers.com/best-python-interpreter-execute-python-online/
