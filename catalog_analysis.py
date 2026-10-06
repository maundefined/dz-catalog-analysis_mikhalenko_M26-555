import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    if not movies:
        return 0.0

    total_rating = math.fsum(movie.get('rating') for movie in movies)
    return round(total_rating / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    if not movies:
        return (0, 0, 0)

    ages = [current_year - movie.get('year') for movie in movies]

    max_age = max(ages)
    min_age = min(ages)
    avg_age = math.ceil(sum(ages) / len(ages))

    return (max_age, min_age, avg_age)

def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f'{hours}ч {mins}м'

def rating_tier(rating):
    if rating >= 9:
        return 'шедевр'
    elif rating >= 7:
        return 'хорошо'
    else:
        return 'средне' if rating >= 5 else 'слабо'

def decade_label(year):
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if 2015 <= year <= 2020:
            return 'недавние'
        case _:
            return 'старые'

for movie in movies:
    if 'comedy' in movie.get('genres'):
        continue
    print(movie.get('title'))

i = 0
while i < len(movies):
    if movies[i].get('rating') > 9.0:
        print(f'Первый фильм с рейтингом выше 9.0: {movies[i].get('title')}')
        break
    i += 1
else:
    print('Шедевров не найдено')

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie.get('duration_min') > threshold:
            count += 1
    return count

def normalize_title(title):
    words = title.split()
    normalized_words = [word[0].upper() + word[1:] for word in words]
    return ' '.join(normalized_words)

def make_slug(title):
    normalized = normalize_title(title)
    return normalized.lower().replace(' ', '-')

def format_report_line(movie):
    title = normalize_title(movie.get('title'))
    genres = ', '.join(sorted(movie.get('genres')))
    duration = duration_in_hours(movie.get('duration_min'))
    return (f"'{title}' ({movie.get('year')}) — {movie.get('rating')}/10, "
            f"{duration}, жанры: {genres}")

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie.get('rating'), reverse=True)
    return [movie.get('title') for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie.get('rating'), reverse=True)
    return [(movie.get('title'), movie.get('rating')) for movie in sorted_movies[:n]]

def count_by_genre(movies):
    genres_count = {}
    for movie in movies:
        for genre in movie['genres']:
            genres_count[genre] = genres_count.get(genre, 0) + 1
    return genres_count

def actor_filmography(movies):
    films = {}
    for movie in movies:
        title = movie.get('title')
        for actor in movie.get('actors'):
            films.setdefault(actor, []).append(title)
    return films

avg = average_rating(movies)
above_avg = {movie['title']: movie['rating']
    for movie in movies if movie['rating'] > avg}

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres |= set(movie.get('genres', set()))
    return genres

def common_actors(movie1, movie2):
    actors1 = set(movie1.get('actors', []))
    actors2 = set(movie2.get('actors', []))
    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie.get('rating', 0) >= min_rating:
            yield movie

for movie in iter_high_rated(movies):
    print(format_report_line(movie))

total_duration = sum(movie.get('duration_min') 
		for movie in movies if movie.get('rating') > 7)
print(total_duration)

def main():
    print("Hello from dz-catalog-analysis-mikhalenko-m26-555!")

if __name__ == "__main__":
    main()
