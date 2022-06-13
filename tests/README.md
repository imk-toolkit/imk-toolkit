# testing
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
├── dataarrays_tests     # Folder for dataarray test data
│   ├── _template.py      # Test template for dataarray methods
│   └── ...               # Tests, files and generators
├── datasets_tests       # Folder for dataset test data
│   ├── _template.py      # Test template for dataset methods
│   └── ...               # Tests, files and generators
└── README.md           # Readme with test instructions and tips 
```

### _template.py
Use this file as template to create your test requirements. The test files
should be divided between the following sections:

 - Module fixtures section: Individual fixtures for your tests.
 - Tests section: List of tests and assertions with reduced setup.

Access the file for more detailed comments and descriptions about each of
the classes and sections.

### test data packages
You have two folders available where to save and write your tests:

 - `datarray_tests`: Folder for your dataarray test methods and files.
 - `dataset_tests`: Folder for your dataset test methods and files.

Tests must always start by `test_` so pytest can find and execute them.

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
$ pytest tests/dataarray_tests/test_anomalies
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
