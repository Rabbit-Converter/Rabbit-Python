# Rabbit-Python

Another Zawgyi <=> Unicode Converter as a Python module. Written in [Python](https://www.python.org).

Current minimum requirements: Python 2.7.x or 3.3+

## Installation

You can include rabbit.py directly:

```python
from rabbit import Rabbit
```

TODO: pip and easy_install

## Usage

```python
from rabbit import Rabbit

Rabbit.uni2zg("မင်္ဂလာပါ")  # returns zg strings "မဂၤလာပါ"

Rabbit.zg2uni("မဂၤလာပါ")   # returns unicode strings "မင်္ဂလာပါ"
```

## Contributing

1. Fork it ( https://github.com/Rabbit-Converter/Rabbit-Python )
2. Create your feature branch (`git checkout -b my-new-feature`)
  - Install python 2.x and python 3.x
  - Run `python test.py` and `python3 test.py`
  - Add a test case to test.py
  - Implement the code.
  - Make the tests pass.
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## License
MIT
