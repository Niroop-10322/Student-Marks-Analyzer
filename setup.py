#!/usr/bin/env python3
"""
Setup script for Student Marks Analyzer
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="student-marks-analyzer",
    version="2.0.0",
    author="Durgashree Shetty",
    author_email="",
    description="A comprehensive Python program to analyze student performance across different subjects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Niroop-10322/Student-Marks-Analyzer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "web": ["streamlit>=1.28.0", "pandas>=1.5.0"],
        "advanced": ["streamlit>=1.28.0", "pandas>=1.5.0", "plotly>=5.15.0"],
    },
    entry_points={
        "console_scripts": [
            "student-analyzer=student_marks_analyzer:main",
        ],
    },
    keywords="education, analysis, student, marks, performance, streamlit, web-app",
    project_urls={
        "Bug Reports": "https://github.com/Niroop-10322/Student-Marks-Analyzer/issues",
        "Source": "https://github.com/Niroop-10322/Student-Marks-Analyzer",
        "Documentation": "https://github.com/Niroop-10322/Student-Marks-Analyzer#readme",
    },
)
