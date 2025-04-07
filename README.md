# Pandas example

This project is an usage example of `pandas`' library in Python.

We will see the differences between `Series` and `DataFrame`:

  - `Series`: Is a unidimensional array with indexation. Similar to dictionary.
  - `DataFrame`: Data structure similar to Excel or SQL table.

For this example, I used the "MovieLens" data set that contains information of users, films and ratings.


## Requirements

`pandas` and `numpy` libraries are necessary. You can install them with `pip`:

```bash
$ pip install pandas
$ pip install numpy
```

- Option 1 : lors du chargement des données avec
  pandas.read_csv()

- Option 2 : en utilisant la fonction replace()

df.replace(['XXXX', 'XX'], pd.NA, inplace=True)
