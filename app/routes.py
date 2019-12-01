from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def search_result():
    zip_code = request.form.get('zip')
    food_type = request.form.get('food_type')
    return render_template(
        'results.html',
        name='Chef Cao',
        address='1800 Holleman Dr, College Station, TX',
        rating=3.5
    )
