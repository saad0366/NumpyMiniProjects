'''import numpy as np
record={}
stds=5
subs=5
students=[]
subjects=[]
marks=[]
for i in range(stds):
    student=input(f"enter the name of{i+1} student")
    students.append(student)
for i in range(subs):
    subject=input(f"enter the name of {i+1} subject")
    subjects.append(subject)

for i in range(len(subjects)):
    mark=np.random.randint(0,100)
    marks.append(mark)

for i in range(5):
    key=students[i]
    value=


    record[key]=value
print(record)'''
'''import numpy as np

# Step 1: Initialize data structures
record = {}
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

students = []
subjects = []

# Step 2: Input student names
print("\nEnter student names:")
for i in range(num_students):
    name = input(f"  Student {i+1}: ")
    students.append(name)

# Step 3: Input subject names
print("\nEnter subject names:")
for i in range(num_subjects):
    subject = input(f"  Subject {i+1}: ")
    subjects.append(subject)

# Step 4: Generate marks using NumPy and store them
for i in range(num_students):
    # Create an empty dictionary for each student
    student_marks = {}
    
    # Generate random marks for all subjects (0 to 100)
    random_marks = np.random.randint(0, 101, size=num_subjects)
    
    # Assign each subject its corresponding mark
    for j in range(num_subjects):
        student_marks[subjects[j]] = random_marks[j]
    
    # Store in main record
    record[students[i]] = student_marks

# Step 5: Display the record
print("\n📘 STUDENT MARKS RECORD 📘")
for student, marks in record.items():
    print(f"\n{student}:")
    for subject, mark in marks.items():
        print(f"  {subject}: {mark}")'''
import numpy as np

print("🎓 Welcome to Student Grades Analyzer 🎓")

# Step 1: Take dynamic inputs
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

students = []
subjects = []

print("\nEnter student names:")
for i in range(num_students):
    name = input(f"  Student {i+1} name: ")
    students.append(name)

print("\nEnter subject names:")
for i in range(num_subjects):
    subject = input(f"  Subject {i+1} name: ")
    subjects.append(subject)

# Step 2: Generate random marks using NumPy
marks = np.random.randint(0, 101, size=(num_students, num_subjects))

# Step 3: Calculate totals and averages
totals = np.sum(marks, axis=1)
averages = np.mean(marks, axis=1)

# Step 4: Find topper
topper_index = np.argmax(totals)
topper_name = students[topper_index]
topper_score = totals[topper_index]

# Step 5: Subject-wise averages and toppers
subject_avg = np.mean(marks, axis=0)
subject_topper_indices = np.argmax(marks, axis=0)
subject_toppers = [students[i] for i in subject_topper_indices]

# Step 6: Display results neatly
print("\n" + "="*60)
print("📊 STUDENT PERFORMANCE REPORT 📊")
print("="*60)
print(f"{'Student':<15}{'Total Marks':<15}{'Average Marks':<15}")
print("-"*60)
for i in range(num_students):
    print(f"{students[i]:<15}{totals[i]:<15}{averages[i]:<15.2f}")

print("="*60)
print(f"🏆 Topper: {topper_name} with {topper_score} marks")
print("="*60)

# Step 7: Display subject-wise analysis
print("\n📘 SUBJECT-WISE ANALYSIS 📘")
print("-"*60)
print(f"{'Subject':<15}{'Avg Marks':<15}{'Top Scorer':<15}")
print("-"*60)
for i in range(num_subjects):
    print(f"{subjects[i]:<15}{subject_avg[i]:<15.2f}{subject_toppers[i]:<15}")






