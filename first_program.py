print("Hello World")
print()
def personalized_greeting(name, course_code):
    print(f"Hello {name}, welcome to {course_code} !!!")
personalized_greeting("Lula","COMP 170")

students = ["Omar","Lula","Enrique","Arhub","Ben","Richard","Heather"]
your_course = "COMP 170"

for name in students:
    personalized_greeting(name,your_course)

# An array is a contiguous space in memory indexed sequentially from 0 on.
# "len" is a reserved string that gives the "length" of a specified array.