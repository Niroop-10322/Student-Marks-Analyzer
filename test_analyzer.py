"""
Test file for Student Marks Analyzer
Demonstrates how to use the analyzer functions with different data sets.
"""

from student_marks_analyzer import analyze_student_marks, display_analysis

def test_different_data_sets():
    """Test the analyzer with different student data sets."""
    
    # Test Case 1: Original sample data
    print("TEST CASE 1: Original Sample Data")
    print("=" * 50)
    students1 = {
        'Alice': [85, 90, 78],
        'Bob': [72, 88, 91],
        'Charlie': [95, 85, 89],
        'David': [35, 65, 70]
    }
    
    results1 = analyze_student_marks(students1)
    display_analysis(results1)
    
    # Test Case 2: More students with different scenarios
    print("\nTEST CASE 2: Extended Data Set")
    print("=" * 50)
    students2 = {
        'Emma': [92, 88, 95],
        'Frank': [45, 78, 82],
        'Grace': [38, 42, 35],  # Failing in multiple subjects
        'Henry': [88, 92, 90],
        'Ivy': [75, 68, 72]
    }
    
    results2 = analyze_student_marks(students2)
    display_analysis(results2)
    
    # Test Case 3: Edge cases
    print("\nTEST CASE 3: Edge Cases")
    print("=" * 50)
    students3 = {
        'Perfect': [100, 100, 100],
        'Barely_Pass': [40, 40, 40],
        'Just_Fail': [39, 39, 39],
        'Mixed': [100, 30, 50]
    }
    
    results3 = analyze_student_marks(students3)
    display_analysis(results3)

def demonstrate_function_usage():
    """Demonstrate how to use the functions programmatically."""
    
    print("\n" + "=" * 60)
    print("PROGRAMMATIC USAGE DEMONSTRATION")
    print("=" * 60)
    
    # Example: Get just the analysis results without display
    students = {
        'John': [85, 90, 88],
        'Sarah': [92, 87, 91],
        'Mike': [35, 75, 80]
    }
    
    results = analyze_student_marks(students)
    
    # Access specific results programmatically
    print(f"Number of students analyzed: {len(results['all_students'])}")
    print(f"Failed students: {results['failed_students']}")
    print(f"Class topper: {results['class_topper']}")
    print(f"Math topper: {results['subject_toppers']['Math']}")
    print(f"Science topper: {results['subject_toppers']['Science']}")
    print(f"English topper: {results['subject_toppers']['English']}")
    
    # Calculate class average
    total_average = sum(results['student_averages'].values()) / len(results['student_averages'])
    print(f"Class average: {total_average:.2f}%")

if __name__ == "__main__":
    test_different_data_sets()
    demonstrate_function_usage()
