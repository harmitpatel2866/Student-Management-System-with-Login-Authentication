Student Management System with Login & Authentication

A Python-based Student Management System developed as a PBL Mini Project for Python for Data Science.

The application provides a graphical interface for managing student admission records, viewing student information, performing basic data analysis, and generating reports.

Features
Login & Authentication
Student Admission
Student Records
Data Analysis
Report Generation
Data Validation
Logout
Technologies Used
Python
Tkinter
Pandas
CSV
OS Module
ttk
Student Admission

The system allows the user to enter:

Student ID
Student Name
Email
Phone Number
Branch
Semester
Percentage

Student information is stored in a CSV file named:

student_admission.csv
Student Records

The Student Records module displays all registered students in a table.

The table includes:

Student ID
Name
Email
Phone
Branch
Semester
Percentage
Data Analysis

The system performs basic analysis using Pandas:

Total Students
Average Percentage
Highest Percentage
Lowest Percentage
Login & Authentication

Login & Authentication is the selected Beyond-Syllabus Topic of this project.

The system verifies the username and password before providing access to the Student Management dashboard.

Login Credentials
Username: admin
Password: 1234
Data Validation

The system validates student information before saving it.

All fields are required.
Student ID must be unique.
Phone number must contain only digits.
Phone number must contain exactly 10 digits.
Percentage must be between 0 and 100.
Reports

The Reports module generates a summary containing:

Total Registered Students
Average Percentage
Highest Percentage
Lowest Percentage

The report can be saved as:

student_report.txt
Project Structure
Student-Management-System/
│
├── student_management.py
├── student_admission.csv
├── student_report.txt
└── README.md
How to Run
1. Install Python

Check whether Python is installed:

python --version
2. Install Pandas
pip install pandas
3. Open the Project

Open the project folder in VS Code.

4. Run the Application
python student_management.py
Project Objective

The main objective of this project is to develop a simple Python-based application for managing student information while demonstrating GUI development, data storage, data processing, basic statistical analysis, and Login & Authentication.

Future Scope

The project can be extended by adding:

MySQL or SQLite database
Secure password hashing
Multiple user accounts
Admin and Student roles
Search Student
Update Student
Delete Student
Graphical data visualization
PDF report generation
Excel export
Forgot Password functionality
Project Information

Project: Student Management System with Login & Authentication
Subject: Python for Data Science
Project Type: PBL Micro Project
Programming Language: Python
