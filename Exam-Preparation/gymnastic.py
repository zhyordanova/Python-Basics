state = input()
device = input()

difficulty_assessment = 0
evaluation_performance = 0

if state == 'Russia':
    if device == "ribbon":
        difficulty_assessment = 9.1
        evaluation_performance = 9.4
    elif device == 'hoop':
        difficulty_assessment = 9.3
        evaluation_performance = 9.8
    else:
        difficulty_assessment = 9.6
        evaluation_performance = 9
elif state == 'Bulgaria':
    if device == "ribbon":
        difficulty_assessment = 9.6
        evaluation_performance = 9.4
    elif device == 'hoop':
        difficulty_assessment = 9.55
        evaluation_performance = 9.75
    else:
        difficulty_assessment = 9.5
        evaluation_performance = 9.4
elif state == 'Italy':
    if device == "ribbon":
        difficulty_assessment = 9.2
        evaluation_performance = 9.5
    elif device == 'hoop':
        difficulty_assessment = 9.45
        evaluation_performance = 9.35
    else:
        difficulty_assessment = 9.7
        evaluation_performance = 9.15

total_grade = difficulty_assessment + evaluation_performance

diff = 20 - total_grade
percent_diff = (diff / 20) * 100

print(f'The team of {state} get {total_grade:.3f} on {device}.')
print(f'{percent_diff:.2f}%')