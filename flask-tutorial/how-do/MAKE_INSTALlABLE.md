## Describe the Project

The setup.py file describes your project and the files that belong to it.

```python3
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
```

Python needs another file named MANIFEST.in to tell what this other data is.

```
MANIFEST.in
include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

## Install the Project

```bash
$ pip install -e .
```
