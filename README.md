# Breast Cancer Prediction Using Machine Learning
This project is a machine learning based web application that predicts whether breast cancer is **Benign** or **Malignant** using medical input data.  
The application is built using **Python**, **Flask**, and **Scikit-Learn**.

---

# Introduction

Breast cancer is one of the most common cancers worldwide. Early detection can significantly improve treatment outcomes.  
This project uses a trained machine learning model to classify breast cancer and provides predictions through a web interface.

---

## Project Structure

Breast-Cancer-Prediction-Using-Machine-Learning/
│

├── data/

│ └── dataset.csv

│

├── model/

│ └── model.pkl

│

├── static/

│ └── style.css

│

├── templates/

│ └── index.html

│

├── Breastcancer.ipynb

├── app.py

├── requirement.txt

└── README.md



---

## Machine Learning Model

- Dataset: Breast Cancer Dataset
- Problem Type: Classification
- Output:
  - Benign (Non-Cancerous)
  - Malignant (Cancerous)
- The trained model is saved using Pickle and reused in the Flask application.

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS

---

## Installation

### Step 1: Clone the Repository


git clone https://github.com/Sreenidhi646/Breast-Cancer-Prediction-Using-Machine-Learning.git
cd Breast-Cancer-Prediction-Using-Machine-Learning
Step 2: Create Virtual Environment (Optional)

python -m venv venv
Activate:

Windows:


venv\Scripts\activate
Linux / macOS:


source venv/bin/activate

Step 3: Install Required Libraries

pip install -r requirement.txt
Running the Application

python app.py
Open your browser and go to:


http://127.0.0.1:5000/
 How to Use
Open the web application.

Enter the medical input values.

Click on Predict.

The result will display whether the tumor is Benign or Malignant.

 Step-by-Step Workflow
Load dataset using Pandas

Preprocess the data

Split dataset into training and testing sets

Train machine learning model

Evaluate model accuracy

Save trained model using Pickle

Load model in Flask application

Take user input and generate prediction

 Requirements
All required Python packages are listed in requirement.txt.

Main libraries:

Flask

scikit-learn

pandas

numpy



Contributing
Fork the repository

Create a new branch

Commit your changes

Submit a pull request



 Author
Sreeidhi M
GitHub: https://github.com/Sreenidhi646

