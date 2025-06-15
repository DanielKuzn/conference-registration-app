import pandas as pd

def get_movies_data():
    # Wczytaj dane z pliku CSV
    df = pd.read_csv('movies.csv', sep=';', encoding='ISO-8859-1', skiprows=[1])
    return df

# Zadanie 1 – Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# a następnie wyświetli wszystkie filmy z roku 2000.
def zadanie_1():
    movies = get_movies_data()
    movies_2000 = movies[movies["Year"] == 2000]
    print("Filmy z roku 2000:")
    print(movies_2000[["Title", "Year"]].to_string())

# Zadanie 2 – Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# obliczy i wyświetli średnią długość filmów wszystkich reżyserów.
def zadanie_2():
    movies = get_movies_data()
    avg_length = movies.groupby('Director')['Length'].mean()
    print("Średnie długości filmów: ")
    print(avg_length)

# Zadanie 2b
def zadanie_2b():
    movies = get_movies_data()
    avg_length = movies.groupby('Director').agg({
        'Length': ['count', 'mean'],
        })
    print("Średnie długości filmów: ")
    print(avg_length)

# Zadanie 3 – Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# utworzy nowy plik CSV zawierający tylko kolumny z tytułem,
# reżyserem i popularnością dla każdego filmu oraz zapisze go pod nową nazwą.
def zadanie_3():
    movies = get_movies_data()
    if all(col in movies.columns for col in ['Title', 'Director', 'Popularity']):
        selected_columns = movies[['Title', 'Director', 'Popularity']]
        selected_columns.to_csv('filmy_tytul_rezyser_popularnosc.csv', index=False)
        print("Plik 'filmy_tytul_rezyser_popularnosc.csv' został zapisany.")
    else:
        print("Brak wymaganych kolumn (Title, Director, Popularity) w danych.")

# Zadanie 4 – Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# obliczy i wyświetli procentowy udział filmów z nagrodami w stosunku do całkowitej liczby filmów.
def zadanie_4():
    movies = get_movies_data()
    if 'Awards' in movies.columns:
        awarded = movies[movies['Awards'].astype(str).str.strip().str.lower() == 'yes']
        total = len(movies)
        percentage = (len(awarded) / total) * 100 if total > 0 else 0
        print(f"Procentowy udział filmów z nagrodami: {percentage:.2f}%")
    else:
        print("Brak kolumny 'Awards' w danych.")

# Zadanie 5 – Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# a następnie wyświetli wszystkie filmy z reżyserem o nazwisku "Kubrick".
def zadanie_5():
    movies = get_movies_data()
    if 'Director' in movies.columns:
        kubrick_movies = movies[movies['Director'].astype(str).str.contains('Kubrick', case=False, na=False)]
        print("Filmy reżyserowane przez Kubricka:")
        print(kubrick_movies[['Title', 'Director']].to_string(index=False))
    else:
        print("Brak kolumny 'Director' w danych.")

# Zadanie 6 – Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# obliczy i wyświetli sumę popularności filmów z gatunkiem "comedy".
def zadanie_6():
    movies = get_movies_data()
    if 'Subject' in movies.columns and 'Popularity' in movies.columns:
        comedy_movies = movies[movies['Subject'].astype(str).str.contains('Comedy', case=False, na=False)]
        comedy_movies['Popularity'] = pd.to_numeric(comedy_movies['Popularity'], errors='coerce')
        total_popularity = comedy_movies['Popularity'].sum()
        print(f"Suma popularności filmów z gatunkiem 'Comedy': {total_popularity}")
    else:
        print("Brak wymaganych kolumn (Subject, Popularity) w danych.")


# Wywołanie wszystkich funkcji

print("\n###### Zadanie 1 ######\n")
zadanie_1()

print("\n###### Zadanie 2 ######\n")
zadanie_2()

print("\n###### Zadanie 2b ######\n")
zadanie_2b()

print("\n###### Zadanie 3 ######\n")
zadanie_3()

print("\n###### Zadanie 4 ######\n")
zadanie_4()

print("\n###### Zadanie 5 ######\n")
zadanie_5()

print("\n###### Zadanie 6 ######\n")
zadanie_6()
