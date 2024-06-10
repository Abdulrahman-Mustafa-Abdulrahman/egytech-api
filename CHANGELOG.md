# CHANGELOG.md

## 1.0.2 (2024-06-10)

### Features:

- Added tests in tests.py to validate model initialization and
  parsing -> [1cbb92b](https://github.com/Abdulrahman-Mustafa-Abdulrahman/egytech-api/commit/1cbb92badc522fd1c6dec2bd2f5fd7b4ede850b4)
- Converted tests to parameterized tests to reduce boilerplate and enhance interpretability
  -> [88cc3dd](https://github.com/Abdulrahman-Mustafa-Abdulrahman/egytech-api/commit/88cc3dd2e39aa6016293b3fb45b2a44dc1c854ed)
- Added docstrings for the entire package making it more compatible with code linters and IDE auto-completion features
  -> [7bddb9f](https://github.com/Abdulrahman-Mustafa-Abdulrahman/egytech-api/commit/7bddb9fa74b9e71540df6dc9ea06e11491e096ff)
  , [267ec6f](https://github.com/Abdulrahman-Mustafa-Abdulrahman/egytech-api/commit/267ec6fab78c6ae834ddd5b87cdfaa5a9f9eeab1)

### Fix:

- Fixed a bug where API query models could be initialized with extra
  fields -> [ee81b86](https://github.com/Abdulrahman-Mustafa-Abdulrahman/egytech-api/commit/ee81b860738e84704157669829ae3703e88e7a46)
- Fixed a bug where serialization of a model containing `min_yoe` or `max_yoe` would create incorrect query parameters
  -> [8cf48ed](https://github.com/Abdulrahman-Mustafa-Abdulrahman/egytech-api/commit/8cf48edda23aee34c09f1cb946054ae80eb53199)

### Documentation:

#### README.md

- Updated the file to have a To-Do
  section -> [3a02e73](https://github.com/Abdulrahman-Mustafa-Abdulrahman/egytech-api/commit/3a02e73fe8050777fae823fc7e8948776deb9494), [4519b9f](https://github.com/Abdulrahman-Mustafa-Abdulrahman/egytech-api/commit/4519b9f80a37a96ad62b97874356dfb591187d1b)
- Updated the file to have an Examples
  section -> [af9ea77](https://github.com/Abdulrahman-Mustafa-Abdulrahman/egytech-api/commit/af9ea77c4aea8d1d9a88d2ff343824052ebecdc1)
- Added a Colab notebook to demonstrate the performance benefits of using connection pooling alone or
  with making API calls
  asynchronously -> [94ee330](https://github.com/Abdulrahman-Mustafa-Abdulrahman/egytech-api/commit/94ee3302bab30494422478c3baefe0e4997827cf)

#### Gitbook Full Documentation:

- Added a section on the `PoolingClient` usage in the docs.
- Added sections on `ParticipantsQueryParams` and `StatsQueryParams` in the docs.
- Added hyperlinks across different classes to improve interpretability.
- Fixed a typo in the Quickstart code sample.