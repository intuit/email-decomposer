# email-decomposer
**Decomposition of email to first name, last name, and host**
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