"""
leftovers.py
Author: Olivia Luisi
This file contains pieces of code I deemed unhelpful
because I found better ways.
"""


def add_lat(df):
    """
    This function edits the geometry column values to only
    include the longitude. It adds the new value into a dataset
    and returns the dataset to be added as values into the
    desired dataframe column.

    Before I was able to use my MapBox token I was unable
    to use a geo-json for the maps I wanted. So I decided
    to clean the latitude myself in order to force it to
    work with what I needed it for. Thankfully I aquired
    a MapBox token so this trial and error was for naught.
    """
    new_df = df.copy()
    result = []
    for index, row in new_df.iterrows():
        value = str(row['geometry'])
        first = value.split("(")
        second = first[1].split(" ")
        if len(second) > 1:
            third = second[1]
            fourth = third.replace(")", "")
            fourth = float(fourth)
            result.append(fourth)
        else: 
            result.append(np.nan)
    return result


def add_lon(df):
    """
    This function edits the geometry column values to only
    include the longitude. It adds the new value into a dataset
    and returns the dataset to be added as values into the
    desired dataframe column.

    Before I was able to use my MapBox token I was unable
    to use a geo-json for the maps I wanted. So I decided
    to clean the longitude myself in order to force it to
    work with what I needed it for. Thankfully I aquired
    a MapBox token so this trial and error was for naught.
    """
    new_df = df.copy()
    result = []
    for index, row in new_df.iterrows():
        value = str(row['geometry'])
        first = value.split("(")
        second = first[1].split(" ")
        if len(second) > 1:
            third = second[0]
            result.append(third)
        else: 
            result.append(np.nan)
    return result


"""
Various notes from pulling unique data from the
'year' column I created:
These are the years we're working with now:
1841, 1900, 1901, 1902, 1903, 1904, 1905, 1906,
1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914,
1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922,
1923, 1924, 1925, 1926, 1927, 1928, 1930, 1931
So let's examine these:
1900-1905, 1906-1910, 1911-1915, 1916-1920,
1921-1925, 1926-1930
"""
