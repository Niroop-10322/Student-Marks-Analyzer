import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def analyze_student_marks(students):
    """
    Analyze student marks and provide comprehensive analysis.
    
    Args:
        students (dict): Dictionary with student names as keys and lists of marks as values
                         Format: {'StudentName': [Math, Science, English]}
    
    Returns:
        dict: Analysis results containing all required information
    """
    
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

def main():
    st.set_page_config(
        page_title="Student Marks Analyzer",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📊 Student Marks Analyzer")
    st.markdown("---")
    
    # Sidebar for data input
    st.sidebar.header("📝 Data Input")
    
    # Option to use sample data or custom data
    data_option = st.sidebar.selectbox(
        "Choose data source:",
        ["Sample Data", "Custom Input"]
    )
    
    if data_option == "Sample Data":
        students = {
            'Alice': [85, 90, 78],
            'Bob': [72, 88, 91],
            'Charlie': [95, 85, 89],
            'David': [35, 65, 70]
        }
        st.sidebar.success("Using sample data")
        
    else:
        students = get_custom_data()
    
    # Main analysis
    if students:
        results = analyze_student_marks(students)
        display_streamlit_analysis(results, students)
    
def get_custom_data():
    """Get custom student data from user input"""
    st.sidebar.subheader("Add Students")
    
    students = {}
    
    # Number of students
    num_students = st.sidebar.number_input("Number of students:", min_value=1, max_value=20, value=4)
    
    # Input fields for each student
    for i in range(num_students):
        st.sidebar.markdown(f"### Student {i+1}")
        
        name = st.sidebar.text_input(f"Name {i+1}:", key=f"name_{i}")
        math = st.sidebar.number_input(f"Math {i+1}:", min_value=0, max_value=100, value=85, key=f"math_{i}")
        science = st.sidebar.number_input(f"Science {i+1}:", min_value=0, max_value=100, value=90, key=f"science_{i}")
        english = st.sidebar.number_input(f"English {i+1}:", min_value=0, max_value=100, value=78, key=f"english_{i}")
        
        if name:  # Only add if name is provided
            students[name] = [math, science, english]
    
    return students

def display_streamlit_analysis(results, students):
    """Display analysis results in Streamlit format"""
    
    # Create tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Overview", "📊 Charts", "📈 Analysis", "🎯 Details"])
    
    with tab1:
        display_overview(results, students)
    
    with tab2:
        display_charts(results, students)
    
    with tab3:
        display_analysis_tab(results, students)
    
    with tab4:
        display_details(results)

def display_overview(results, students):
    """Display overview of results"""
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Students", len(students))
    
    with col2:
        st.metric("Failed Students", len(results['failed_students']))
    
    with col3:
        class_avg = sum(results['student_averages'].values()) / len(results['student_averages'])
        st.metric("Class Average", f"{class_avg:.2f}%")
    
    with col4:
        top_avg = results['student_averages'][results['class_topper']]
        st.metric("Top Average", f"{top_avg:.2f}%")
    
    st.markdown("---")
    
    # Student marks table
    st.subheader("📊 Student Marks Table")
    
    # Create DataFrame for display
    data = []
    for name, marks in students.items():
        data.append({
            'Student': name,
            'Math': marks[0],
            'Science': marks[1],
            'English': marks[2],
            'Average': results['student_averages'][name],
            'Status': '❌ Failed' if name in results['failed_students'] else '✅ Passed'
        })
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    
    # Failed students alert
    if results['failed_students']:
        st.error(f"⚠️ Students who failed: {', '.join(results['failed_students'])}")

def display_charts(results, students):
    """Display interactive charts"""
    
    # Prepare data for charts
    data = []
    for name, marks in students.items():
        data.append({
            'Student': name,
            'Math': marks[0],
            'Science': marks[1],
            'English': marks[2],
            'Average': results['student_averages'][name]
        })
    
    df = pd.DataFrame(data)
    
    # Chart 1: Subject-wise comparison
    st.subheader("📈 Subject-wise Performance")
    
    fig_subjects = px.bar(
        df, 
        x='Student', 
        y=['Math', 'Science', 'English'],
        title="Marks by Subject",
        barmode='group'
    )
    fig_subjects.update_layout(height=400)
    st.plotly_chart(fig_subjects, use_container_width=True)
    
    # Chart 2: Average comparison
    st.subheader("🏆 Average Marks Comparison")
    
    fig_avg = px.bar(
        df,
        x='Student',
        y='Average',
        title="Average Marks by Student",
        color='Average',
        color_continuous_scale='RdYlGn'
    )
    fig_avg.update_layout(height=400)
    st.plotly_chart(fig_avg, use_container_width=True)
    
    # Chart 3: Radar chart for top 3 students
    st.subheader("🎯 Performance Radar Chart (Top 3)")
    
    # Get top 3 students by average
    top_3 = sorted(results['student_averages'].items(), key=lambda x: x[1], reverse=True)[:3]
    
    fig_radar = go.Figure()
    
    for name, avg in top_3:
        marks = students[name]
        fig_radar.add_trace(go.Scatterpolar(
            r=marks + [marks[0]],  # Close the shape
            theta=['Math', 'Science', 'English', 'Math'],
            fill='toself',
            name=name
        ))
    
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        height=400
    )
    st.plotly_chart(fig_radar, use_container_width=True)

def display_analysis_tab(results, students):
    """Display detailed analysis"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Class Topper")
        st.info(f"**{results['class_topper']}** with {results['student_averages'][results['class_topper']]}% average")
        
        st.subheader("🥇 Subject Toppers")
        for subject, topper in results['subject_toppers'].items():
            st.success(f"**{subject}**: {topper}")
    
    with col2:
        st.subheader("📊 Performance Summary")
        
        # Create summary DataFrame
        summary_data = []
        for subject in ['Math', 'Science', 'English']:
            marks = [students[name][['Math', 'Science', 'English'].index(subject)] for name in students.keys()]
            summary_data.append({
                'Subject': subject,
                'Average': sum(marks) / len(marks),
                'Highest': max(marks),
                'Lowest': min(marks)
            })
        
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)
        
        # Class statistics
        st.subheader("📈 Class Statistics")
        averages = list(results['student_averages'].values())
        st.metric("Class Average", f"{sum(averages)/len(averages):.2f}%")
        st.metric("Highest Average", f"{max(averages):.2f}%")
        st.metric("Lowest Average", f"{min(averages):.2f}%")

def display_details(results):
    """Display detailed breakdown"""
    
    st.subheader("📋 Detailed Breakdown")
    
    # Failed students details
    if results['failed_students']:
        st.error("### ❌ Failed Students")
        for student in results['failed_students']:
            st.write(f"**{student}** - Needs attention")
    
    # All student averages
    st.subheader("📊 All Student Averages")
    
    avg_data = []
    for name, avg in results['student_averages'].items():
        avg_data.append({
            'Student': name,
            'Average': avg,
            'Grade': get_grade(avg)
        })
    
    avg_df = pd.DataFrame(avg_data)
    avg_df = avg_df.sort_values('Average', ascending=False)
    st.dataframe(avg_df, use_container_width=True)
    
    # Subject analysis
    st.subheader("📚 Subject Analysis")
    
    subjects = ['Math', 'Science', 'English']
    for subject in subjects:
        topper = results['subject_toppers'][subject]
        st.write(f"**{subject} Topper**: {topper}")

def get_grade(average):
    """Convert average to grade"""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    main()
