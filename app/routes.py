from flask import render_template, request, redirect, url_for
from app import app

posts = []
@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        user_data = {
            'name': request.form.get('name'),
            'city': request.form.get('City'),
            'hobby': request.form.get('Hobby'),
            'age': request.form.get('age')
        }
        return render_template('contact.html', user_data=user_data)
    return render_template('index.html')

@app.route('/g', methods=['GET', 'POST'])
def i():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            posts.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('City')
        hobby = request.form.get('Hobby')
        age = request.form.get('age')
        user_data = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        }



    return render_template('index.html', user_data=user_data)