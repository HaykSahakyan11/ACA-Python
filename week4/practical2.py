import pandas as pd
hh = pd.read_csv('netflix_titles.csv')
print(hh[(hh.release_year > 2015) & ((hh.cast.str.contains("Kevin Spacey")) | (hh.cast.str.contains("Leonardo DiCaprio")))])
