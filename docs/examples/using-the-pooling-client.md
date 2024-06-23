# Using The Pooling Client

In this example, we explain how the egytech_api PoolingClient can be used to leverage connection pooling and make
multiple requests at once by just specifying the request parameters in a dictionary.

## Create Your Queries

In order to use the Pooling Client for making multiple API calls, we have to prepare our queries first as such:

### First Method (Recommended):

In this method, we create multiple `ParticipantsQueryParams` objects and compile them into a list:

```python
from egytech_api.models import ParticipantsQueryParams

# Prepare your queries as ParticipantsQueryParams instances

# Method 1:
# This method is better in the sense that it allows auto-completion and linters to
# check input validity
query1 = ParticipantsQueryParams(title="backend", cs_degree=True)
query2 = ParticipantsQueryParams(title="frontend", gender="female")
queryn = ParticipantsQueryParams(title="fullstack", include_relocated=False)

# Create a list of your queries
params_objs = [query1, query2, queryn]
```

### Second Method:

In this method, we simply create a list of dictionaries, each of which represent one query. This will unfortunately
not be compatible with code auto-complete and your IDE won't be able to check if you have made the right inputs as
you type. Instead, you'll find out during run-time.

```python
from egytech_api.models import ParticipantsQueryParams

# Prepare your queries as ParticipantsQueryParams instances

# Method 2:
query_list = [
    {"title": "backend", "cs_degree": True},  # first query
    {"title": "frontend", "gender": "female"},  # second query
    {"title": "fullstack", "include_relocated": False},  # Nth query
]

# Create a list of your queries as ParticipantsQueryParams objects
params_objs = [ParticipantsQueryParams(**query) for query in query_list]
```

> - While both of the above methods will produce the same output (a list of `ParticipantsQueryParams` instances),
    it's always advisable to use the linter-friendly method, as it prevents many minor issues
    (because of typos for example) ahead of run-time.
> - It's also notable that the second method is more compatible with an external form of query
    storage (a local json file for example) as well as being more compatible with larger scale
    queries (more than 10 for example).

## Initialize A PoolingClient Instance & Fetch The Data

Here, we initialize an instance of egytech_api.core.PoolingClient. This client automatically executes the api
calls with the given parameters, leveraging connection pooling, a feature provided by httpx. The client then aggregates
the resulting data into a pandas.DataFrame instance which you can use for whatever you want.

```python
from egytech_api.core import PoolingClient

# Initialize PoolingClient instance with the params_objs list created above
client = PoolingClient(queries=params_objs)

# Export resulting data to a pandas.DataFrame instance
df = client.get_df()

# Do awesome things with the DataFrame
```

> While connection pooling is a very cool feature that could potentially cut the runtime of your code significantly,
> its use on the scale of this project is a bit of an overkill as its scale is not that large. However, I did it
> as a personal project, and that's where most of the wrapper features come from.

You can find a full notebook with a couple of simple visualizations
[here](https://deepnote.com/app/abdulrahmans-workspace/EgyTech-FYI-Wrapper-b29d75ab-a623-4f8b-96df-b8c7c8e89535).
