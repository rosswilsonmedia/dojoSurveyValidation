from flask_app import app

from flask import render_template, request, redirect, session, flash
from ..models.dojo import Dojo

@app.route('/')
def index():
    if 'form_response' in session:
        session.pop('form_response')
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    if Dojo.validate_form(request.form):
        Dojo.save(request.form)
        session['form_response']=request.form
        return redirect('/result')
    else:
        return redirect('/')

@app.route('/result')
def result_page():
    return render_template('result.html', form_response=session['form_response'])