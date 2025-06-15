import pandas as pd

# Wczytaj dane z pliku CSV
df = pd.read_csv('movies.csv', sep=';', encoding = "ISO-8859-1", skiprows=[1])
# Wyświetl pierwsze 3 wiersze tabeli
print(df.head(3).to_string())

# Wyświetl statystyki opisowe dla kolumny "Popularity"
df['Popularity'].describe()
# Wyświetl informacje o typach danych i ilości niepustych wartości w każdej kolumnie
df.info()

# Obliczenie statystyk opisowych dla kolumny z długościami filmów
df['Length'].describe()
