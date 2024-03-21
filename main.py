
# Import the necessary modules.
from flask import Flask, render_template, request

# Create a Flask application.
app = Flask(__name__)

# Define the routes for the application.
@app.route('/')
def home():
    """Display the homepage of the website."""
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    """Display the list of German lessons."""
    return render_template('lessons.html')

@app.route('/lesson/<lesson_id>')
def lesson(lesson_id):
    """Display the corresponding lesson page."""
    return render_template(f'lesson{lesson_id}.html')

@app.route('/resources')
def resources():
    """Display the resources page."""
    return render_template('resources.html')

# Run the application.
if __name__ == '__main__':
    app.run(debug=True)
