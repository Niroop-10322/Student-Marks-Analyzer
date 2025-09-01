# Student Marks Analyzer

A comprehensive Python program to analyze student performance across different subjects in a school setting, available in both **console** and **web application** versions.

## 🌟 Features

The Student Marks Analyzer provides the following functionalities:

1. **Store Marks**: Stores marks for multiple students across three subjects (Math, Science, English)
2. **Display and Flag**: Displays each student's marks and flags students who failed any subject (marks below 40)
3. **Calculate Average**: Calculates the average marks for each student
4. **Identify Class Topper**: Identifies the class topper based on the highest average score
5. **Determine Subject-wise Toppers**: Determines the student with the highest mark in each individual subject

## 📱 Versions Available

### 🖥️ Console Version
- **File**: `student_marks_analyzer.py`
- **Features**: Command-line interface with formatted output
- **Dependencies**: Python 3.x only (no external packages)

### 🌐 Web Application (Streamlit)
- **File**: `simple_streamlit.py`
- **Features**: Interactive web interface with real-time updates
- **Dependencies**: Streamlit, Pandas

## 🚀 Quick Start

### Console Version
```bash
python student_marks_analyzer.py
```

### Web Application
```bash
# Install dependencies
pip install streamlit pandas

# Run the web app
python -m streamlit run simple_streamlit.py
```

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Console Version (No Dependencies)
The console version requires no additional packages - just Python!

### Web Application Dependencies
```bash
pip install streamlit pandas
```

## 🎯 How to Use

### Console Version
1. Run `python student_marks_analyzer.py`
2. View the formatted analysis output
3. Modify the `students` dictionary in the code to analyze different data

### Web Application
1. Run `python -m streamlit run simple_streamlit.py`
2. Open your browser to `http://localhost:8501`
3. Choose between sample data or custom input
4. Explore the interactive interface with real-time updates

## 📊 Sample Input

The program uses the following sample data structure:

```python
students = {
    'Alice': [85, 90, 78],
    'Bob': [72, 88, 91],
    'Charlie': [95, 85, 89],
    'David': [35, 65, 70]  # David is failing in Math
}
```

## 📈 Expected Output

### Console Version Output
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

### Web Application Features
- **Interactive Metrics**: Real-time key performance indicators
- **Data Tables**: Sortable tables with student information
- **Failure Alerts**: Visual indicators for failing students
- **Performance Summary**: Subject-wise statistics
- **Grade Conversion**: Automatic grade assignment (A+, A, B, C, D, F)

## 🔧 Implementation Requirements

The program uses the following programming constructs as required:

- **Dictionaries**: Student data is stored in a dictionary with student names as keys and lists of marks as values
- **Lists**: Used for storing marks and various result collections
- **For Loops**: Used extensively for iterating through students and analyzing data
- **If Statements**: Used for conditional logic (checking failing students, finding toppers)

## 📁 Project Structure

```
Student-Marks-Analyzer/
├── student_marks_analyzer.py      # Console version
├── simple_streamlit.py            # Web application
├── streamlit_standalone.py        # Advanced web version (with charts)
├── streamlit_app.py               # Original web version
├── test_analyzer.py               # Testing and demonstration
├── run_streamlit.py               # Easy setup script
├── requirements_streamlit.txt     # Web app dependencies
├── README.md                      # This file
└── README_Streamlit.md           # Detailed web app documentation
```

## 🎨 Web Application Features

### Interactive Interface
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Real-time Updates**: Instant analysis as you change data
- **Beautiful UI**: Modern interface with emojis and colors

### Data Input Options
- **Sample Data**: Quick start with pre-loaded data
- **Custom Input**: Add your own students and marks
- **Dynamic Forms**: Adjustable number of students (1-20)

### Analysis Views
- **Key Metrics**: Total students, failed students, class average, top average
- **Student Table**: Complete marks table with pass/fail status
- **Performance Summary**: Subject-wise statistics
- **Grade Analysis**: Complete list with letter grades

## 🔧 Customization

### Console Version
To analyze different student data, modify the `students` dictionary in the `main()` function:

```python
students = {
    'StudentName1': [Math_Marks, Science_Marks, English_Marks],
    'StudentName2': [Math_Marks, Science_Marks, English_Marks],
    # Add more students as needed
}
```

### Web Application
- Use the sidebar to input custom data
- Add up to 20 students
- All analysis updates automatically

## 🐛 Troubleshooting

### Console Version
- Ensure Python 3.x is installed
- Run from the project directory

### Web Application
- Install dependencies: `pip install streamlit pandas`
- Use `python -m streamlit run simple_streamlit.py`
- If port is busy, try `python -m streamlit run simple_streamlit.py --server.port 8502`

## 🎓 Educational Use

### Perfect For
- **Teachers**: Analyze class performance
- **Students**: Track individual progress
- **Administrators**: Monitor academic performance
- **Data Science Learning**: Interactive data visualization

### Learning Outcomes
- **Data Analysis**: Real-time data processing
- **Visualization**: Interactive charts and graphs
- **Web Development**: Streamlit framework
- **Python Programming**: Data manipulation and analysis

## 🤝 Contributing

Feel free to enhance the application:
- Add new chart types
- Implement data export features
- Add more analysis metrics
- Improve the UI/UX

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Durgashree Shetty**

---

**🎉 Choose your preferred version and start analyzing student performance!**
