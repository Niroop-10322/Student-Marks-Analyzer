# Student Marks Analyzer

A comprehensive Python program to analyze student performance across different subjects in a school setting.

## Features

The Student Marks Analyzer provides the following functionalities:

1. **Store Marks**: Stores marks for multiple students across three subjects (Math, Science, English)
2. **Display and Flag**: Displays each student's marks and flags students who failed any subject (marks below 40)
3. **Calculate Average**: Calculates the average marks for each student
4. **Identify Class Topper**: Identifies the class topper based on the highest average score
5. **Determine Subject-wise Toppers**: Determines the student with the highest mark in each individual subject

## Implementation Requirements

The program uses the following programming constructs as required:
- **Dictionaries**: Student data is stored in a dictionary with student names as keys and lists of marks as values
- **Lists**: Used for storing marks and various result collections
- **For Loops**: Used extensively for iterating through students and analyzing data
- **If Statements**: Used for conditional logic (checking failing students, finding toppers)

## Sample Input

The program uses the following sample data structure:

```python
students = {
    'Alice': [85, 90, 78],
    'Bob': [72, 88, 91],
    'Charlie': [95, 85, 89],
    'David': [35, 65, 70]  # David is failing in Math
}
```

## How to Run

1. Make sure you have Python installed on your system
2. Open a terminal/command prompt in the project directory
3. Run the program:

```bash
python student_marks_analyzer.py
```

## Expected Output

The program will display:

- **All Students and Their Marks**: Complete list of students with their individual subject marks
- **Failed Students**: List of students who scored below 40 in any subject
- **Average Marks**: Average score for each student
- **Class Topper**: Student with the highest average score
- **Subject-wise Toppers**: Top performer in each individual subject

## Sample Output

```
============================================================
                    STUDENT MARKS ANALYZER
============================================================

📊 ALL STUDENTS AND THEIR MARKS:
----------------------------------------
Alice: Math=85, Science=90, English=78
Bob: Math=72, Science=88, English=91
Charlie: Math=95, Science=85, English=89
David: Math=35, Science=65, English=70

⚠️  STUDENTS WHO FAILED ANY SUBJECT (Marks < 40):
--------------------------------------------------
• David

📈 AVERAGE MARKS FOR EACH STUDENT:
----------------------------------------
Alice: 84.33%
Bob: 83.67%
Charlie: 89.67%
David: 56.67%

🏆 CLASS TOPPER (Highest Average):
-----------------------------------
• Charlie with 89.67% average

🥇 SUBJECT-WISE TOPPERS:
-------------------------
• Math: Charlie
• Science: Alice
• English: Bob

============================================================
```

## Customization

To analyze different student data, modify the `students` dictionary in the `main()` function:

```python
students = {
    'StudentName1': [Math_Marks, Science_Marks, English_Marks],
    'StudentName2': [Math_Marks, Science_Marks, English_Marks],
    # Add more students as needed
}
```

## Program Structure

- `analyze_student_marks(students)`: Main analysis function that processes student data
- `display_analysis(results)`: Function to format and display the analysis results
- `main()`: Entry point that sets up sample data and runs the analysis

## Requirements

- Python 3.x
- No external dependencies required

## Author

Durgashree Shetty
