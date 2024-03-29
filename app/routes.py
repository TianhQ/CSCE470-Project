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
        address='1800 Holleman Dr',
        city='College Station',
        state='TX',
        zip_code=77840,
        count_reviews=200,
        rating=3.5,
        documents=[{'name':'lal', 'address':'56565 college'}, {'name':'lal', 'address':'56565 college'}, {'name':'lal', 'address':'56565 college'}]
    )
