#!/usr/bin/env python3
"""
Streamlit Student Marks Analyzer Runner
This script helps you run the Streamlit web application.
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import streamlit
        import pandas
        import plotly
        print("✅ All dependencies are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_streamlit.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def run_streamlit():
    """Run the Streamlit application"""
    print("🚀 Starting Streamlit app...")
    print("📱 The app will open in your web browser")
    print("🔗 If it doesn't open automatically, go to: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the app")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])
    except KeyboardInterrupt:
        print("\n👋 Streamlit app stopped")

def main():
    print("📊 Student Marks Analyzer - Streamlit Version")
    print("=" * 50)
    
    # Check if dependencies are installed
    if not check_dependencies():
        print("\n🔧 Installing missing dependencies...")
        if not install_dependencies():
            print("❌ Failed to install dependencies. Please install manually:")
            print("   pip install -r requirements_streamlit.txt")
            return
    
    # Run the app
    run_streamlit()

if __name__ == "__main__":
    main()
