from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('network.html')

if __name__ == '__main__':
    # Ensure templates directory exists
    os.makedirs('templates', exist_ok=True)
    
    # Run the Flask app
    app.run(debug=True)
