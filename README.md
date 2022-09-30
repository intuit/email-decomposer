
<!--[![codecov](https://codecov.io/gh/intuit/email-decomposer/branch/main/graph/badge.svg)](https://codecov.io/gh/intuit/email-decomposer)
[![CircleCI](https://circleci.com/gh/intuit/email-decomposer.svg?style=shield)](https://circleci.com/gh/intuit/email-decomposer)
[![License](https://img.shields.io/github/license/intuit/email-decomposer)](https://raw.githubusercontent.com/intuit/email-decomposer/master/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/email-decomposer)](https://pypi.org/project/email-decomposer)
[![Downloads](https://pepy.tech/badge/email-decomposer)](https://pepy.tech/project/email-decomposer)-->

# email-decomposer
**Decomposition of email address to first name, last name, and host.**
### How to use
#### Install
```
pip install email_decomposer
```
#### Import
```
from email_decomposer.EmailDecomposer import EmailDecomposer
```
#### Decompose emails list
```
EmailDecomposer().decompose(data=['johndue@intuit.com'], get_host=True).head()
```

|    | first_name   | last_name   | host                    |
|---:|:-------------|:------------|:------------------------|
|  johndue@intuit.com | John       | Due        | intuit.com |
#### Decompose a single email
```
EmailDecomposer().decompose(data='johndue@intuit.com', get_host=True)
```
{'first_name': 'John', 'last_name': 'Due', 'host': 'intuit.com'}
### Contributing

See [CONTRIBUTING.md](https://github.com/intuit/email-decomposer/blob/main/CONTRIBUTING.md).
