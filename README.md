# Student Placement Predictor

## Overview

The **Student Placement Predictor** is a web-based application developed using **Python** and **Streamlit** to help students evaluate their placement readiness. The application assesses a student's academic performance, technical skills, and technical assessment score to estimate placement chances and provide personalized recommendations for improvement.

---

# Problem Statement

Many students are uncertain about their placement readiness because there is no unified platform that evaluates their academic performance, technical knowledge, and overall preparedness. As a result, students often struggle to identify their strengths, weaknesses, and the areas that require improvement before campus recruitment.

This project addresses this challenge by providing an interactive placement prediction system that evaluates students through academic details, skill assessment, and a technical test, followed by placement probability prediction and career guidance.

---

# Solution Approach

The Student Placement Predictor is designed as a Streamlit-based web application that:

* Collects student academic and personal information.
* Evaluates self-assessed technical skill levels.
* Conducts a branch-specific online technical assessment.
* Calculates the assessment score.
* Predicts placement probability using rule-based logic and assessment scoring.
* Recommends suitable job roles based on student performance.
* Provides learning resources to improve placement readiness.

---

# Key Features

## Student Information Collection

The application collects the following information:

* Full Name
* Email Address
* Mobile Number
* Branch
* Academic Year
* CGPA

## Skill Assessment

Students can select their technical skill level from the following categories:

* Beginner
* Intermediate
* Advanced

## Online Technical Assessment

* Branch-specific technical questions
* 20 Multiple Choice Questions (MCQs)
* Timer-based examination
* Automatic score calculation

### Question Palette

The application provides an interactive question palette with the following indicators:

* Current Question
* Answered Questions
* Unanswered Questions

## Placement Prediction

Based on the student's academic details, selected skill level, and technical assessment score, the system predicts placement readiness as:

* High
* Medium
* Low

## Career Recommendations

The application suggests suitable job roles based on the student's performance and skill level.

## Learning Resources

Students receive learning recommendations to strengthen weak areas and improve placement readiness.

## Answer Review

After completing the assessment, students can review:

* Selected answers
* Correct answers
* Reference materials for further learning

---

# Project Workflow

1. Student enters personal and academic details.
2. Student selects technical skill level.
3. The system generates a branch-specific technical assessment.
4. Student completes the assessment within the allotted time.
5. The system evaluates the responses and calculates the score.
6. Placement probability is predicted using rule-based evaluation.
7. Suitable job roles and learning resources are recommended.
8. Students can review their answers along with correct solutions and references.

---

# Repository Structure

```text
Student-Placement-Predictor/
│
├── datasets/
│   ├── cse_questions.csv
│   ├── ece_questions.csv
│   ├── eee_questions.csv
│   ├── mech_questions.csv
│   └── civil_questions.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

* Python
* Streamlit
* Pandas
* HTML
* CSS
* Git
* GitHub

---

# Installation and Setup

## Prerequisites

* Python 3.8 or above
* Git

## Clone the Repository

```bash
git clone https://github.com/your-username/Student-Placement-Predictor.git
```

```bash
cd Student-Placement-Predictor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

---

# Access the Application

**Local URL**

```text
http://localhost:8501
```

**Network URL**

```text
http://10.236.151.5:8501
```

---

# Future Enhancements

* Machine Learning-based placement prediction
* Resume analysis and scoring
* Interview performance evaluation
* Aptitude assessment module
* Personalized learning dashboard
* Admin panel for question management
* Performance analytics and reports

---

# Author

**Harshitha Yalla**

Capstone Project – Student Placement Predictor

Training Program | January 2026

GitHub: https://github.com/harshithayalla15

LinkedIn: https://www.linkedin.com/in/harshithayalla/
