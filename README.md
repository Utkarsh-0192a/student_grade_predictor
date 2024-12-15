# AI-Based Grade Prediction

## **Problem Statement**
The goal of this project is to predict a student's final grade based on various features such as attendance, participation, assignment scores, and exam marks. By analyzing these predictors, we aim to provide insights into key factors influencing academic performance and assist in early intervention for students at risk of underperforming.

---

## **Approach**

### **1. Data Preprocessing**
- **Dataset**: The project uses the Student Performance Dataset, which includes features like attendance, participation, assignment scores, and exam marks. Missing values were handled, and the dataset was scaled for uniformity.
- **Feature Engineering**:
  - Normalized numerical features to ensure consistent scaling.
  - Encoded categorical variables (if any) using one-hot encoding.

### **2. Model Selection and Training**
- **Model Used**: Random Forest Regressor was chosen for its robustness and ability to capture non-linear relationships.
- **Hyperparameter Tuning**: Performed grid search to optimize parameters like the number of estimators, maximum depth, and minimum samples per split.
- **Training Process**:
  - Split the dataset into training (80%) and testing (20%) sets.
  - Trained the model on the training set and evaluated performance on the test set.

### **3. Evaluation Metrics**
- **R² Score**: Achieved a score of **0.83**, indicating that the model explains 83% of the variance in the target variable.
- **RMSE**: The Root Mean Squared Error was calculated to measure prediction accuracy.

### **4. Feature Importance Analysis**
- Analyzed feature importance using the Random Forest's built-in feature importance metric.
- Visualized the contributions of each feature to the final predictions.

---

## **Results**

### **Performance Metrics**
| Metric | Value |
|--------|-------|
| R² Score | 0.83 |
| RMSE    | 3.21 |

### **Feature Importance**
Key contributors to grade prediction:
1. Exam Marks
2. Assignment Scores
3. Attendance
4. Participation

**Visualization**: Below is a bar chart showing the importance of each feature (provided in the repository).

### **Observations**
- Exam marks and assignment scores are the most significant predictors of final grades.
- Attendance and participation also play a substantial role but are secondary to academic performance metrics.

---

## **Challenges**
1. **Handling Missing Data**:
   - Solution: Imputed missing values using the median for numerical features.
2. **Overfitting**:
   - Solution: Tuned hyperparameters and used cross-validation to ensure generalizability.
3. **Feature Scaling**:
   - Solution: Applied standardization to ensure consistency across features.

---

## **Bonus: Productization**
A **Streamlit Web App** was developed for user interaction. Users can input features such as attendance, participation, and exam marks to predict the final grade.

### **Features of the Web App**
- **Grade Prediction**: Provides real-time predictions based on user inputs.
- **Feature Importance Visualization**: Displays a bar chart of feature contributions.
- **User-Friendly Interface**: Simple and intuitive layout for ease of use.

### **How to Run the App**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app/app.py
   ```

---

## **Repository Structure**
```
.
|-- data/               # Dataset or link to download it
|-- src/                # Source code for preprocessing, training, and evaluation
|-- app/                # Streamlit app code
|-- notebooks/          # Jupyter notebooks for EDA and experimentation
|-- README.md           # Project documentation
|-- requirements.txt    # Dependencies for the project
```

---

## **Conclusion**
This project successfully predicts student grades with high accuracy and provides insights into the factors influencing academic performance. The additional web app makes the solution accessible and practical for real-world use.

---

## **Future Improvements**
- Explore advanced models like Gradient Boosting or Neural Networks for improved performance.
- Incorporate additional features like socio-economic factors or study habits.
- Deploy the app to a cloud platform for wider accessibility.
