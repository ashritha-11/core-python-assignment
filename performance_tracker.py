def calculate_average(students):
    averages = {}
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        averages[name] = round(avg, 2)  
    return averages
def find_top_performer(averages):
    return max(averages, key=averages.get)
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
averages = calculate_average(students)
top_student = find_top_performer(averages)
print("Average Marks:", averages)
print("Top Performer:", top_student)
