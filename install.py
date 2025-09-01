#!/usr/bin/env python3
"""
Installation script for Student Marks Analyzer
"""

import subprocess
import sys
import os

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    
    try:
        # Install basic dependencies
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit", "pandas"])
        print("✅ Basic dependencies installed successfully!")
        
        # Ask if user wants advanced features
        response = input("🤔 Do you want to install advanced features (charts)? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "plotly"])
            print("✅ Advanced dependencies installed successfully!")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def create_desktop_shortcut():
    """Create desktop shortcuts for easy access"""
    print("🔗 Creating desktop shortcuts...")
    
    # Create batch file for Windows
    if os.name == 'nt':  # Windows
        with open("run_console.bat", "w") as f:
            f.write("@echo off\n")
            f.write("python student_marks_analyzer.py\n")
            f.write("pause\n")
        
        with open("run_web.bat", "w") as f:
            f.write("@echo off\n")
            f.write("python -m streamlit run simple_streamlit.py\n")
            f.write("pause\n")
        
        print("✅ Created run_console.bat and run_web.bat files")
    
    # Create shell scripts for Unix-like systems
    else:
        with open("run_console.sh", "w") as f:
            f.write("#!/bin/bash\n")
            f.write("python3 student_marks_analyzer.py\n")
        
        with open("run_web.sh", "w") as f:
            f.write("#!/bin/bash\n")
            f.write("python3 -m streamlit run simple_streamlit.py\n")
        
        # Make scripts executable
        os.chmod("run_console.sh", 0o755)
        os.chmod("run_web.sh", 0o755)
        
        print("✅ Created run_console.sh and run_web.sh files")

def main():
    """Main installation function"""
    print("🚀 Student Marks Analyzer - Installation")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Create shortcuts
    create_desktop_shortcut()
    
    print("\n🎉 Installation completed successfully!")
    print("\n📋 Next steps:")
    print("1. Console version: python student_marks_analyzer.py")
    print("2. Web version: python -m streamlit run simple_streamlit.py")
    print("3. Or use the created shortcut files")
    
    print("\n📚 For more information, see README.md")
    print("🌐 GitHub: https://github.com/Niroop-10322/Student-Marks-Analyzer")

if __name__ == "__main__":
    main()
