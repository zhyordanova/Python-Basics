import sys
count_movie = int(input())

max_ratings = -sys.maxsize
min_ratings = sys.maxsize
min_name = ''
max_name = ''
sum_ratings = 0
average_ratings = 0

for i in range(0, count_movie):
    movie_name = input()
    ratings = float(input())

    if ratings > max_ratings:
        max_ratings = ratings
        max_name = movie_name

    if ratings < min_ratings:
        min_ratings = ratings
        min_name = movie_name

    sum_ratings += ratings

    average_ratings = sum_ratings / count_movie

print(f'{max_name} is with highest rating: {max_ratings:.1f}')
print(f'{min_name} is with lowest rating: {min_ratings:.1f}')
print(f'Average rating: {average_ratings:.1f}')
