import streamlit as st
import pandas as pd
import joblib


model = joblib.load('decision_tree_model.pkl')

st.title("Grade Prediction App")
st.write("Enter student details to predict their grade.")

col =['participation','failures','attendance', 'assignment_scores', 'exam_marks']
miin = {'participation': 0, 'failures': 0, 'attendance': 25, 'assignment_scores': 0, 'exam_marks': 0}
maxx = {'participation': 4, 'failures': 4, 'attendance': 100, 'assignment_scores': 20, 'exam_marks': 20}

# Create input fields dynamically based on dataset features
input_data = {}
for column in col:
    min_value = float(miin[column])
    max_value = float(maxx[column])
    input_data[column] = st.number_input(f"{column} ({min_value} to {max_value})", value=min_value, min_value=min_value, max_value=max_value)
input_data['attendance'] = 100 - input_data['attendance']
# Convert input data to a DataFrame
input_df = pd.DataFrame([input_data])

# Predict grade
if st.button("Predict Grade"):
    prediction = model.predict(pd.DataFrame(input_df, columns=col))[0]
    st.success(f"The predicted grade is: {prediction:.2f} out of 20")

