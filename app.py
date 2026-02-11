from flask import Flask
from flask import render_template

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app route decorator to map the URL  

@app.route("/")
def index():
        name_data = 'Jackson'
        year_data = 2026
        favorites_list = ['Stardew Valley', 'The Sims', 'BG3', 'Pokemon']
        ratings_dict = {
                        'The Sims':'great',
                        'BG3':'good',
                        'Stardew Valley':'solid',
                        'Pokemon': 'okay',
        }
        return render_template("index.html", name=name_data, year=year_data, favorites=favorites_list, ratings=ratings_dict )    