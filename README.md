# Egytech API
A simple python wrapper for [Egytech's API](https://api.egytech.fyi/).


## Description

* This python wrapper leverages the type safety and input validity checking of pydantic. 
It creates enums for all user-side inputs, making sure that all outgoing api requests are correct.
It also leverages request pooling offered by httpx. This leads to more performant api requests
when making multiple requests in a short period of time. This is my first project with pydantic. 
Feedback is appreciated.
* It also allows the user to extract the api call results as a pandas dataframe, making
any visualization or data manipulation easier to do.
* You can extract the data in csv, or xslx format immediately. This uses pandas under the hood.
However, you can extract a pandas dataframe and do whatever you want with it.

## Getting Started

### Dependencies

* This project uses **python 3.11**, any newer python version should work.
* This project is os-agnostic, it should work on any os with a python interpreter.

### Installing

* To install with pip, run the following command:
```
pip install egytech_api
```

### Quickstart
To make a simple API request that fetches survey data of participants who have a computer science
degree and a "backend" job title, you can do the following:
```python
from egytech_api.core import Participants

# Create a Participants object
participants = Participants(title="backend", cs_degree=True)

# Fetch the data
df = participants.get_df()

# Print the first 5 rows of the dataframe
df.head()
```

### Full Documentation
The full documentation can be found [here](https://abdulrahman-mustafa.gitbook.io/egytech-api/).


## License

This project is licensed under the MIT License - see the LICENSE file for details
