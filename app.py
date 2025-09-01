import streamlit as st
from student_marks_analyzer import analyze_student_marks

st.title("Student Marks Analyzer")

# Input form for student marks
st.header("Enter Student Marks")
students = {}
num_students = st.number_input("Number of students", min_value=1, max_value=20, value=4)

for i in range(num_students):
    name = st.text_input(f"Student {i+1} Name", key=f"name_{i}")
    math = st.number_input(f"{name} - Math Marks", min_value=0, max_value=100, key=f"math_{i}")
    science = st.number_input(f"{name} - Science Marks", min_value=0, max_value=100, key=f"science_{i}")
    english = st.number_input(f"{name} - English Marks", min_value=0, max_value=100, key=f"english_{i}")
    if name:
        students[name] = [math, science, english]

if st.button("Analyze"):
    results = analyze_student_marks(students)
    st.subheader("All Students and Their Marks")
    for student in results['all_students']:
        st.write(f"{student['name']}: Math={student['marks']['Math']}, Science={student['marks']['Science']}, English={student['marks']['English']}")
    
    st.subheader("Failed Students")
    if results['failed_students']:
        for student in results['failed_students']:
            st.write(f"{student}")
    else:
        st.write("No students failed any subject!")
    
    st.subheader("Average Marks for Each Student")
    for student_name, average in results['student_averages'].items():
        st.write(f"{student_name}: {average}%")
    
    st.subheader("Class Topper")
    st.write(f"{results['class_topper']} with {results['student_averages'][results['class_topper']]}% average")
    
    st.subheader("Subject-wise Toppers")
    for subject, topper in results['subject_toppers'].items():
        st.write(f"{subject}: {topper}")