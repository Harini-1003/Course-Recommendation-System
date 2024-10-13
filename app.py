from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load and preprocess the Coursera dataset
data_path = "C:/Users/harin/OneDrive/Desktop/recommendation/data/data.csv/data.csv"
data = pd.read_csv(data_path)

# Data preprocessing
data = data[['course_name', 'level', 'course description', 'course_flag']]  # Use correct columns

# Clean the level column to include only valid levels
valid_levels = ['beginner', 'intermediate', 'expert']
data['level'] = data['level'].str.lower().str.strip()
data = data[data['level'].isin(valid_levels)]

# Debugging: Print unique values for verification
print("Unique levels after cleaning:", data['level'].unique())

# Creating a function to recommend courses based on difficulty
def recommend_courses(difficulty):
    # Normalize the difficulty for comparison
    difficulty = difficulty.lower()

    # Filter data based on difficulty level
    filtered_data = data[data['level'] == difficulty]

    if not filtered_data.empty:
        print("Filtered Data based on difficulty:", filtered_data)  # Debugging print

    return filtered_data['course_name'].tolist()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route for getting recommendations (handle POST requests)
@app.route('/recommend', methods=['POST'])
def get_recommendation():
    difficulty = request.form['difficulty']
    print(f"Received Difficulty: {difficulty}")  # Debugging statement

    recommended_courses = recommend_courses(difficulty)

    if not recommended_courses:
        return jsonify(['No recommendation available'])

    return jsonify(recommended_courses)

if __name__ == '__main__':
    app.run(debug=True)
