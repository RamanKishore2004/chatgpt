import streamlit as st

def calculate_grade(test_scores):
    # Define your grading scale
    grading_scale = {
        'A': (90, 100),
        'B': (80, 89),
        'C': (70, 79),
        'D': (60, 69),
        'F': (0, 59)
    }
    
    # Calculate average score
    average_score = sum(test_scores) / len(test_scores)
    
    # Determine the grade
    for grade, (min_score, max_score) in grading_scale.items():
        if min_score <= average_score <= max_score:
            return grade

def main():
    st.title("Simple Grade Calculator")

    # Allow user to input test scores
    num_tests = st.number_input("Number of tests", min_value=1, step=1, value=1)
    test_scores = []
    for i in range(num_tests):
        score = st.number_input(f"Test {i+1} score", min_value=0.0, max_value=100.0, step=0.1, value=0.0)
        test_scores.append(score)

    # Calculate overall grade
    if st.button("Calculate Grade"):
        final_grade = calculate_grade(test_scores
