def analyze_student_marks(students):

    # Initialize results dictionary
    results = {
        'all_students': [],
        'failed_students': [],
        'student_averages': {},
        'class_topper': '',
        'subject_toppers': {
            'Math': '',
            'Science': '',
            'English': ''
        }
    }
    
    # Track highest marks for each subject
    subject_highest = {'Math': 0, 'Science': 0, 'English': 0}
    highest_average = 0
    
    # Analyze each student
    for student_name, marks in students.items():
        math, science, english = marks
        
        # Store student information
        student_info = {
            'name': student_name,
            'marks': {
                'Math': math,
                'Science': science,
                'English': english
            }
        }
        results['all_students'].append(student_info)
        
        # Check for failing students (marks below 40)
        if math < 40 or science < 40 or english < 40:
            results['failed_students'].append(student_name)
        
        # Calculate average marks
        average = (math + science + english) / 3
        results['student_averages'][student_name] = round(average, 2)
        
        # Track class topper (highest average)
        if average > highest_average:
            highest_average = average
            results['class_topper'] = student_name
        
        # Track subject-wise toppers
        if math > subject_highest['Math']:
            subject_highest['Math'] = math
            results['subject_toppers']['Math'] = student_name
        
        if science > subject_highest['Science']:
            subject_highest['Science'] = science
            results['subject_toppers']['Science'] = student_name
        
        if english > subject_highest['English']:
            subject_highest['English'] = english
            results['subject_toppers']['English'] = student_name
    
    return results

def display_analysis(results):
 
    print("=" * 60)
    print("STUDENT MARKS ANALYZER")
    print("=" * 60)
    
    # Display all students and their marks
    print("\n ALL STUDENTS AND THEIR MARKS:")
    print("-" * 40)
    for student in results['all_students']:
        print(f"{student['name']}: Math={student['marks']['Math']}, "
              f"Science={student['marks']['Science']}, English={student['marks']['English']}")
    
    # Display failed students
    print(f"\n  STUDENTS WHO FAILED ANY SUBJECT (Marks < 40):")
    print("-" * 50)
    if results['failed_students']:
        for student in results['failed_students']:
            print(f"• {student}")
    else:
        print("• No students failed any subject!")
    
    # Display average marks for each student
    print(f"\n AVERAGE MARKS FOR EACH STUDENT:")
    print("-" * 40)
    for student_name, average in results['student_averages'].items():
        print(f"{student_name}: {average}%")
    
    # Display class topper
    print(f"\n CLASS TOPPER (Highest Average):")
    print("-" * 35)
    print(f"• {results['class_topper']} with {results['student_averages'][results['class_topper']]}% average")
    
    # Display subject-wise toppers
    print(f"\n SUBJECT-WISE TOPPERS:")
    print("-" * 25)
    for subject, topper in results['subject_toppers'].items():
        print(f"• {subject}: {topper}")
    
    print("\n" + "=" * 60)

def main():
    # Sample input data
    students = {
        'Alice': [85, 90, 78],
        'Bob': [72, 88, 91],
        'Charlie': [95, 85, 89],
        'David': [35, 65, 70] 
    }
    
    print("Student Marks Analyzer - Analysis Results")
    print("Sample Data Used:")
    for name, marks in students.items():
        print(f"  {name}: {marks}")
    
    # Analysis
    results = analyze_student_marks(students)
    
    # Display results
    display_analysis(results)

if __name__ == "__main__":
    main()
cd "d:\Cogniquest py\Student marks analyzer"
git init
