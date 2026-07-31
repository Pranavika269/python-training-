from pathlib import Path
import textwrap

root = Path(r"c:\Users\pranavika\OneDrive\Desktop\inventorymanagements\.venv\Lib\site-packages\pranavika")
root.mkdir(parents=True, exist_ok=True)

student_name = "Pranavika S"
college = "Dhaanish Chennai college of engineering"
department = "B.TECH AI&DS"
start_date = "06.07.2026"
status = "Ongoing"
github_profile = "Pranavika269"
linkedin = "Pranavika Srikanth"
leetcode_profile = "Pranavika_Ai&DS"
project_name = "Placement Training Intelligence Dashboard"
project_description = "A Python-based dashboard that helps track placement training progress, daily tasks, LeetCode practice, and interview preparation."


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def add_readme(path, title, content):
    write(path, f"# {title}\n\n{content}")


day_details = [
    ("Day-01_Python_Introduction", "Python Introduction", "Introduction to Python, syntax, comments, and first programs"),
    ("Day-02_Variables_DataTypes", "Variables and Data Types", "Variables, integers, floats, strings, booleans, and type conversion"),
    ("Day-03_Conditional_Statements", "Conditional Statements", "if, elif, else, nested conditions, and logical operators"),
    ("Day-04_Loops", "Loops", "for loop, while loop, range, break, continue, and pass"),
    ("Day-05_List_Tuple", "Lists and Tuples", "List operations, tuple usage, slicing, and iteration"),
    ("Day-06_Sets_Dictionaries", "Sets and Dictionaries", "Set operations, dictionary keys, values, and comprehensions"),
    ("Day-07_Functions", "Functions", "Function definition, parameters, return values, and scope"),
    ("Day-08_Lambda_Modules", "Lambda and Modules", "Lambda expressions, import statements, and reusable modules"),
    ("Day-09_File_Handling", "File Handling", "Read, write, append, and manage files in Python"),
    ("Day-10_Exception_Handling", "Exception Handling", "Try, except, finally, raising exceptions, and debugging"),
    ("Day-11_OOP_Classes", "OOP Classes", "Classes, objects, constructors, and instance attributes"),
    ("Day-12_OOP_Advanced", "OOP Advanced", "Inheritance, polymorphism, encapsulation, and abstraction"),
    ("Day-13_Standard_Libraries", "Standard Libraries", "Math, random, datetime, os, sys, and collections"),
    ("Day-14_SQLite", "SQLite", "Creating databases, tables, and running SQL in Python"),
    ("Day-15_CRUD", "CRUD Operations", "Create, read, update, and delete operations with SQLite"),
    ("Day-16_Current_Progress", "Current Progress", "Review of progress, projects, and interview preparation"),
]

# Root files
write(root / ".gitignore", "__pycache__/\n*.pyc\n*.log\n.venv/\n")
write(root / "LICENSE", "MIT License\n\nCopyright (c) 2026 Pranavika S\n")

root_readme = f"""# Python Placement Training 2026

![Python Banner](Assets/Images/banner.png)

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)  [![GitHub](https://img.shields.io/badge/GitHub-Portfolio-green)](https://github.com/{github_profile})  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/{linkedin.replace(' ', '')})

## Student Profile
- Student Name: {student_name}
- College: {college}
- Department: {department}
- Training Start Date: {start_date}
- Training Status: {status}
- GitHub: {github_profile}
- LinkedIn: {linkedin}
- LeetCode: {leetcode_profile}

## Professional Summary
This repository documents a structured placement training journey in Python, covering fundamentals, problem solving, SQLite, interview preparation, and mini-projects. It is designed to be recruiter-friendly and suitable for GitHub portfolio presentation.

## Table of Contents
- [Training Timeline](#training-timeline)
- [Daily Progress Table](#daily-progress-table)
- [Skills Learned](#skills-learned)
- [Technology Stack](#technology-stack)
- [Folder Structure](#folder-structure)
- [LeetCode Section](#leetcode-section)
- [Database Section](#database-section)
- [Mini Projects](#mini-projects)
- [Final Project](#final-project)
- [Future Goals](#future-goals)
- [Repository Statistics](#repository-statistics)
- [Acknowledgements](#acknowledgements)

## Training Timeline
- Start Date: {start_date}
- Current Status: {status}
- Focus Areas: Python Basics, Data Structures, OOP, SQLite, CRUD, Projects, and Interview Preparation

## Daily Progress Table
| Day | Topic | Status |
|---|---|---|
| 01 | Python Introduction | Completed |
| 02 | Variables and Data Types | Completed |
| 03 | Conditional Statements | Completed |
| 04 | Loops | Completed |
| 05 | Lists and Tuples | Completed |
| 06 | Sets and Dictionaries | Completed |
| 07 | Functions | Completed |
| 08 | Lambda and Modules | Completed |
| 09 | File Handling | Completed |
| 10 | Exception Handling | Completed |
| 11 | OOP Classes | Completed |
| 12 | OOP Advanced | Completed |
| 13 | Standard Libraries | Completed |
| 14 | SQLite | Completed |
| 15 | CRUD | Completed |
| 16 | Current Progress | Ongoing |

## Skills Learned
- Python Syntax and Basics
- Control Flow and Loops
- Functions and Modules
- File Handling and Exceptions
- Object-Oriented Programming
- SQLite and Database Operations
- Problem Solving and Interview Preparation

## Technology Stack
- Python 3.x
- SQLite
- Markdown
- Git and GitHub
- VS Code

## Folder Structure
- [Day-01_Python_Introduction](Day-01_Python_Introduction/README.md)
- [Day-02_Variables_DataTypes](Day-02_Variables_DataTypes/README.md)
- [Day-03_Conditional_Statements](Day-03_Conditional_Statements/README.md)
- [Day-04_Loops](Day-04_Loops/README.md)
- [Day-05_List_Tuple](Day-05_List_Tuple/README.md)
- [Day-06_Sets_Dictionaries](Day-06_Sets_Dictionaries/README.md)
- [Day-07_Functions](Day-07_Functions/README.md)
- [Day-08_Lambda_Modules](Day-08_Lambda_Modules/README.md)
- [Day-09_File_Handling](Day-09_File_Handling/README.md)
- [Day-10_Exception_Handling](Day-10_Exception_Handling/README.md)
- [Day-11_OOP_Classes](Day-11_OOP_Classes/README.md)
- [Day-12_OOP_Advanced](Day-12_OOP_Advanced/README.md)
- [Day-13_Standard_Libraries](Day-13_Standard_Libraries/README.md)
- [Day-14_SQLite](Day-14_SQLite/README.md)
- [Day-15_CRUD](Day-15_CRUD/README.md)
- [Day-16_Current_Progress](Day-16_Current_Progress/README.md)
- [MCQ-Tests](MCQ-Tests/Test-01.md)
- [Mini-Projects](Mini-Projects/README.md)
- [Final-Project](Final-Project/README.md)
- [LeetCode](LeetCode/README.md)
- [Documentation](Documentation/README.md)

## LeetCode Section
- Profile: {leetcode_profile}
- Public Submission Link: __________________
- Practice Tracker: [LeetCode Index](LeetCode/README.md)

## Database Section
- [Student Management System](Student%20Management%20System/README.md)
- [Employee Management System](Employee%20Management%20System/README.md)
- [Library Management System](Library%20Management%20System/README.md)
- [Hospital Management System](Hospital%20Management%20System/README.md)
- [SQLite CRUD](SQLite%20CRUD/README.md)
- [SQL Queries](SQL%20Queries/README.md)
- [Database Schema](Database%20Schema/README.md)

## Mini Projects
- Number Guessing Game
- Calculator App
- Student Record Manager
- File Organizer Utility

## Final Project
- Project Name: {project_name}
- Description: {project_description}
- See [Final Project README](Final-Project/README.md)

## Future Goals
- Strengthen DSA and problem-solving
- Build full-stack projects
- Improve coding interview readiness
- Contribute to open source and internships

## Repository Statistics
- Total Daily Notes: 16
- Topics Covered: Python, OOP, SQLite, CRUD, Projects
- Interview Preparation: Included in each day

## Acknowledgements
Special thanks to mentors, instructors, and the Python learning community for continuous guidance.

## Footer
Built with passion for placement preparation and professional growth.
"""
write(root / "README.md", root_readme)

# Create assets and docs placeholders
for folder in ["Assets", "Images", "Resources", "Documentation"]:
    (root / folder).mkdir(parents=True, exist_ok=True)
    write(root / folder / "README.md", f"# {folder}\n\nThis folder contains supporting assets and documentation for the training repository.\n")

# Create banner placeholder image file
write(root / "Assets" / "Images" / "banner.png", "placeholder image")

# Create daily folder structure
for folder_name, title, topic in day_details:
    folder = root / folder_name
    folder.mkdir(parents=True, exist_ok=True)
    day_readme = f"""# {title}

## Date
{start_date}

## Topics Covered
- {topic}
- Python basics and syntax
- Practical coding exercises

## Theory
This day focuses on understanding the core concept of {title.lower()} in Python. The student learns definitions, syntax, examples, and real-time applications.

## Definitions
- Variable: A container for storing data.
- Expression: A combination of values and operators.
- Statement: A line of code that performs an action.

## Syntax
```python
# Example syntax
value = 10
print(value)
```

## Flow Diagram
```text
Start -> Learn concept -> Practice code -> Write exercises -> Review interview questions
```

## Advantages
- Easy to understand
- Useful for placement interviews
- Builds problem-solving ability

## Disadvantages
- Needs consistent practice
- Requires debugging patience

## Real-Time Applications
- Automation scripts
- Data processing tasks
- Web and AI application logic

## Examples
```python
# Example program
name = 'Pranavika'
print(f'Hello, {{name}}')
```

## Python Programs
- Practice beginner-level programs with comments and docstrings.

## Interview Questions
- What is the purpose of this concept?
- How is it different from similar concepts?
- Where is it used in real-world code?

## LeetCode Problems
- Solve one beginner-friendly problem daily.

## Summary
This topic is a core building block for your Python journey and helps with interview readiness.

## Learning Outcome
- Understand the concept clearly
- Write simple programs confidently
- Explain the topic in interviews

## References
- Python official documentation
- Beginner Python practice resources
"""
    write(folder / "README.md", day_readme)
    write(folder / "Notes.md", f"# Notes for {title}\n\n- Study the concept thoroughly.\n- Review examples and notes after coding.\n")
    write(folder / "leetcode.md", f"# LeetCode Practice for {title}\n\n- Solve one problem daily.\n- Record your approach and complexity.\n")
    write(folder / "interview_questions.md", f"# Interview Questions for {title}\n\n1. Explain the concept in simple words.\n2. Give a real-world example.\n3. Compare it with a related concept.\n")
    write(folder / "practice_questions.md", f"# Practice Questions for {title}\n\n- Write a small program using this concept.\n- Modify the example to handle input from the user.\n")

    # section directories with README files
    section_dirs = ["Python Programs", "Exercises", "Summary", "Learning Outcome", "Real-Time Examples", "Interview Tips", "Important Points", "Common Mistakes", "Folder Documentation"]
    for section in section_dirs:
        section_path = folder / section
        section_path.mkdir(parents=True, exist_ok=True)
        write(section_path / "README.md", f"# {section}\n\nThis section contains study material and practice notes for {title}.\n")

    # One beginner program in each day
    py_file = folder / "Python Programs" / f"{folder_name.lower()}_program.py"
    write(py_file, textwrap.dedent(f'''\
    """Beginner Python program for {title}."""

    def main():
        """Demonstrate a simple Python example."""
        # Store user input in a variable
        name = "{student_name.split()[0]}"
        # Print a greeting using string formatting
        print(f"Hello, {{name}}! Welcome to {title}.")

    if __name__ == "__main__":
        main()
    '''))

    # One exercise file
    exercise_file = folder / "Exercises" / "exercise.py"
    write(exercise_file, textwrap.dedent(f'''\
    """Coding exercise for {title}."""
    # Write a small program based on the day's topic.
    print("Complete the exercise for {title}.")
    '''))

# Root-level MCQ tests
mcq_dir = root / "MCQ-Tests"
mcq_dir.mkdir(parents=True, exist_ok=True)
for idx in range(1, 4):
    write(mcq_dir / f"Test-0{idx}.md", f"""# MCQ Test {idx}

- Date: __________________
- Score: __________________
- Remarks: __________________
- Topics Covered: __________________
- Performance Analysis: __________________
""")

# Mini Projects placeholder
mini_dir = root / "Mini-Projects"
mini_dir.mkdir(parents=True, exist_ok=True)
write(mini_dir / "README.md", """# Mini Projects

This section contains small beginner-friendly Python projects created during the training period.

## Suggested Projects
- Number Guessing Game
- Calculator App
- Student Record Manager
- File Organizer Utility
""")

# Final project structure
final_dir = root / "Final-Project"
final_dir.mkdir(parents=True, exist_ok=True)
for subdir in ["Architecture", "Workflow", "Objectives", "Features", "Technology Stack", "Installation", "Folder Structure", "Screenshots", "Future Scope", "License", "Contributors", "Timeline", "Progress"]:
    subpath = final_dir / subdir
    subpath.mkdir(parents=True, exist_ok=True)
    write(subpath / "README.md", f"# {subdir}\n\nPlaceholder content for the final project section.\n")
write(final_dir / "README.md", f"""# Final Project

## Project Name
{project_name}

## Project Description
{project_description}

## Architecture
See [Architecture](Architecture/README.md)

## Workflow
See [Workflow](Workflow/README.md)

## Objectives
See [Objectives](Objectives/README.md)

## Features
See [Features](Features/README.md)

## Technology Stack
See [Technology Stack](Technology%20Stack/README.md)

## Installation
See [Installation](Installation/README.md)

## Folder Structure
See [Folder Structure](Folder%20Structure/README.md)

## Screenshots
See [Screenshots](Screenshots/README.md)

## Future Scope
See [Future Scope](Future%20Scope/README.md)

## License
See [License](License/README.md)

## Contributors
See [Contributors](Contributors/README.md)

## Timeline
See [Timeline](Timeline/README.md)

## Progress
See [Progress](Progress/README.md)
""")
write(final_dir / "main.py", textwrap.dedent('''\
"""Starter file for the final project."""
print("Final project is ready to be built.")
'''))

# Database section
for db_name in ["Student Management System", "Employee Management System", "Library Management System", "Hospital Management System", "SQLite CRUD", "SQL Queries", "Database Schema"]:
    db_path = root / db_name
    db_path.mkdir(parents=True, exist_ok=True)
    write(db_path / "README.md", f"# {db_name}\n\nThis folder contains database practice materials and documentation for the placement training repository.\n")
    write(db_path / "Python Programs" / "sample.py", textwrap.dedent('''\
    """Sample Python database script."""
    print("Database practice script")
    '''))
    write(db_path / "Documentation" / "notes.md", f"# Documentation for {db_name}\n\n- Create schema.\n- Write queries.\n- Validate outputs.\n")

# LeetCode structure
leetcode_root = root / "LeetCode"
leetcode_root.mkdir(parents=True, exist_ok=True)
write(leetcode_root / "README.md", f"""# LeetCode Practice

- LeetCode Profile: {leetcode_profile}
- My Public Submission Link: __________________

## Daily Practice Index
- [Day 01](Day-01/README.md)
- [Day 02](Day-02/README.md)
- [Day 03](Day-03/README.md)
- [Day 04](Day-04/README.md)
- [Day 05](Day-05/README.md)
- [Day 06](Day-06/README.md)
- [Day 07](Day-07/README.md)
- [Day 08](Day-08/README.md)
- [Day 09](Day-09/README.md)
- [Day 10](Day-10/README.md)
- [Day 11](Day-11/README.md)
- [Day 12](Day-12/README.md)
- [Day 13](Day-13/README.md)
- [Day 14](Day-14/README.md)
- [Day 15](Day-15/README.md)
- [Day 16](Day-16/README.md)
""")

problem_names = [
    ("Day-01", "Two Sum", "two-sum"),
    ("Day-02", "Palindrome Number", "palindrome-number"),
    ("Day-03", "Maximum Subarray", "maximum-subarray"),
    ("Day-04", "Contains Duplicate", "contains-duplicate"),
    ("Day-05", "Valid Anagram", "valid-anagram"),
    ("Day-06", "Best Time to Buy and Sell Stock", "best-time-to-buy-and-sell-stock"),
    ("Day-07", "Binary Search", "binary-search"),
    ("Day-08", "First Bad Version", "first-bad-version"),
    ("Day-09", "Merge Two Sorted Lists", "merge-two-sorted-lists"),
    ("Day-10", "Climbing Stairs", "climbing-stairs"),
    ("Day-11", "Reverse Linked List", "reverse-linked-list"),
    ("Day-12", "Valid Parentheses", "valid-parentheses"),
    ("Day-13", "Symmetric Tree", "symmetric-tree"),
    ("Day-14", "Invert Binary Tree", "invert-binary-tree"),
    ("Day-15", "Linked List Cycle", "linked-list-cycle"),
    ("Day-16", "Fibonacci Number", "fibonacci-number"),
]

for day_folder, problem_title, slug in problem_names:
    problem_dir = leetcode_root / day_folder
    problem_dir.mkdir(parents=True, exist_ok=True)
    write(problem_dir / "README.md", f"""# {problem_title}

## Official LeetCode Problem Link
https://leetcode.com/problems/{slug}/

## Explanation
This problem is solved using a straightforward approach that is easy to understand and explain in interviews.

## Algorithm
1. Read input values.
2. Apply the core logic.
3. Return the result.

## Brute Force
A simple nested loop or direct method can solve the problem but may be less efficient.

## Optimized Approach
Use a more efficient strategy such as hashing or a single pass.

## Time Complexity
O(n)

## Space Complexity
O(1) or O(n)

## Sample Input
```text
Example input
```

## Sample Output
```text
Example output
```

## Interview Tips
- Mention the intuition clearly.
- Explain why the optimized approach is better.
- Discuss edge cases.
""")
    write(problem_dir / "solution.py", textwrap.dedent(f'''\
    """Python solution for {problem_title}."""

    def solve(data):
        """Return a simple result for the example problem."""
        return data

    if __name__ == "__main__":
        print(solve([1, 2, 3]))
    '''))
    write(problem_dir / "explanation.md", f"# Explanation\n\nThe solution focuses on clarity and interview-ready reasoning.\n")
    write(problem_dir / "algorithm.md", f"# Algorithm\n\n1. Understand the problem.\n2. Choose the suitable approach.\n3. Write the code and test with examples.\n")
    write(problem_dir / "brute_force.md", f"# Brute Force\n\nA direct approach can be used for small inputs.\n")
    write(problem_dir / "optimized_approach.md", f"# Optimized Approach\n\nAn optimized approach reduces time complexity and improves efficiency.\n")
    write(problem_dir / "time_complexity.md", f"# Time Complexity\n\nO(n)\n")
    write(problem_dir / "space_complexity.md", f"# Space Complexity\n\nO(1)\n")
    write(problem_dir / "sample_input.md", f"# Sample Input\n\nExample input for {problem_title}.\n")
    write(problem_dir / "sample_output.md", f"# Sample Output\n\nExample output for {problem_title}.\n")
    write(problem_dir / "interview_tips.md", f"# Interview Tips\n\n- Explain the approach clearly.\n- Mention complexity.\n- Include edge cases.\n")

# Documentation placeholder
write(root / "Documentation" / "README.md", """# Documentation

This folder contains supporting notes and references for the placement training repository.
""")

# Create a simple banner file as text
write(root / "Images" / "README.md", """# Images

This folder stores visual assets such as banners and screenshots for the repository.
""")

print("Repository structure created successfully.")
