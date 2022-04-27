# Testing
In the following we will describe in detail how testing is designed on the 
`imktk` module together with on how to add your tests and requirements.

The testing framework is based on [pytest](https://docs.pytest.org) framework.
It is recommended that you first read and understands how tests are organized
and executed before you write your own tests.


## Framework
In addition, this toolkit already implements most of the methods that you
would generally need for testing. Read and follow the next sections to
learn how you can write simple and maintainable code for testing your methods.

The tests package should follow the following structure:
```bash
$ tree tests
tests
├── dataarrays_data     # Folder for dataarray test data
│   ├── __init__.py       # Init file to import data generators
│   └── ...               # Methods, files and generators
├── datasets_data       # Folder for dataset test data
│   ├── __init__.py       # Init file to import data generators
│   └── ...               # Methods, files and generators
├── __init__.py         # Init file to allow test imports
├── __test_template.py  # Template file for your tests
├── conftest.py         # File with generic fixtures 
├── README.md           # Readme with test instructions and tips
├── test_method_1.py    # File containing tests for methods
├── test_method_2.py    # File containing tests for methods
├── ...
└── test_method_n.py    # File containing tests for methods
```

#### __init__.py
This file contains the class `ImktkRequirements` together with other generic
utilities to generally use in your tests.

#### __test_template.py
Use this file as template to create your test requirements. The test files
should be divided between the following sections:

 - Module fixtures section: Individual fixtures for your tests.
 - Requirements section: List of tests and assertions with reduced setup.
 - Parametrization section: Test generation with parametrized calls.  

Access the file for more detailed comments and descriptions about each of
the classes and sections.

#### conftests.py
This tests framework is build in a way that you probably have already available
the required fixtures for your tests. You should not write fixtures but rather
try to reuse the already existing ones.

If you need specific fixtures and parametrization, you can create them into
your `test_` file as it is shown at the `__test_template.py` file.

#### test data packages
You have two folders available where to save and write your test data:

 - `datarrays_data`: Package for your dataarray test methods and files.
 - `datasets_data`: Package for your dataset test methods and files.

Avoid creating long code in your `test_` file for generating datasets
or dataarrays for testing. This makes tests and requirements more readable
and understandable. Use the defined folders for this purpose.

In addition, note the speed of the tests is related to the size of your
data. Try always to a minimum size example that match your requirements
when testing.


## Running only your method tests
As the toolkit grows, it is expected that testing time will increase.
It is not required that you run all tests every time you want to check
one of your specific tests passes. To execute tests on a specific test
module you can use:
```bash
$ pytest tests/test_anomalies
```
Where you would replace `test_anomalies` by your tests module.


## Running tests with multiple processors
You can use [pytest-xdist ](https://pypi.org/project/pytest-xdist) to
reduce the testing time by dividing the test queue into multiple processors.
To execute tests using xdist you can use:
```bash
$ pytest -n auto
```
This will automatically detect the number of processors available at your
machine. However, you can replace `auto` by an integer indicating the
amount of processors you want to dedicate in the testing.
