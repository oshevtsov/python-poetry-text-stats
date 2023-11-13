# Sample Poetry Application: Text Stats

This is a sample Python application managed with
[Poetry](https://python-poetry.org/). This complements the [blog
post](https://oshevtsov.com/blog/python-project-management-with-poetry-and-tox)
that I wrote.

## Usage

Clone the repository and follow the commands below.

```shell
cd text-stats
poetry shell
poetry install
```

Test running the command-line utility.

```shell
text-stats -h
text-stats -c -w -l "Hello, World!"
```
