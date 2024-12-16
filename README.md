# AI-Based Grade Prediction

## **Problem Statement**
The goal of this project is to predict a student's final grade based on various features such as attendance, participation, assignment scores, and exam marks. By analyzing these predictors, we aim to provide insights into key factors influencing academic performance and assist in early intervention for students at risk of underperforming.

---

## **Approach**

### **1. Data Preprocessing**
- **Dataset**: The project uses the Student Performance Dataset, which includes features like attendance, participation, assignment scores, and exam marks. Missing values were handled, and the dataset was scaled for uniformity.

### **2. Model Selection and Training**
- **Model Used**: decison tree regression was chosen for its robustness and ability to capture non-linear relationships.other models tried and selected best model
- **Hyperparameter Tuning**: Performed grid search to optimize parameters like the number of estimators, maximum depth, and minimum samples per split.
- **Training Process**:
  - Split the dataset into training (80%) and testing (20%) sets.
  - Trained the model on the training set and evaluated performance on the test set.

### **3. Evaluation Metrics**
- **R² Score**: Achieved a score of **0.89**, indicating that the model explains 89% of the variance in the target variable.
- **RMSE**: The Root Mean Squared Error was calculated to measure prediction accuracy.

### **4. Feature Importance Analysis**
- Analyzed feature importance using the Desicion tree built-in feature importance metric.
- Visualized the contributions of each feature to the final predictions.

---

## **Results**

### **Performance Metrics**
| Metric | Value |
|--------|-------|
| R² Score | 0.89 |
| RMSE    | 1.5 |

### **Feature Importance**
Key contributors to grade prediction:
1. Exam Marks
2. Assignment Scores
3. Attendance
4. Participation

### **Observations**
- Exam marks and assignment scores are the most significant predictors of final grades.
- Attendance and participation also play a substantial role but are secondary to academic performance metrics.

---

## **Challenges**
1. **Overfitting**:
   - Solution: Tuned hyperparameters and used cross-validation to ensure generalizability.
2. **Feature Scaling**:
   - Solution: Applied standardization to ensure consistency across features.

---

## **Bonus: Productization**
A **Streamlit Web App** was developed for user interaction. Users can input features such as attendance, participation, and exam marks to predict the final grade.

### **Features of the Web App**
- **Grade Prediction**: Provides real-time predictions based on user inputs.
- **User-Friendly Interface**: Simple and intuitive layout for ease of use.

### **How to Run the App**
1. Clone the repository:
   ```bash
   git clone https://github.com/Utkarsh-0192a/student_grade_predictor
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app/app.py
   ```

---

## **Repository Structure**
```
.
|-- data/               # Dataset or link to download it
|-- notebooks/          # Jupyter notebooks for EDA and experimentation
|-- README.md           # Project documentation
```

---

## **Conclusion**
This project successfully predicts student grades with high accuracy and provides insights into the factors influencing academic performance. The additional web app makes the solution accessible and practical for real-world use.

