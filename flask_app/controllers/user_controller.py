
from flask_app import app
from flask import redirect ,render_template, request
from flask_app.models.user_model import User 

# ============================ FORM ROUTES =========================================
@app.route('/')
@app.route('/user_form')
def show_user_form():


    return render_template('create_user.html')



@app.route('/user_form/submit', methods=['POST'])
def submit_user_form():
    data = {
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }

    User.create_one_user(data)
    return redirect ('/all_users')

# ============================ FORM ROUTES =========================================
# ============================ DISPLAY ROUTES =========================================

@app.route('/all_users')
def display_all_user():

    all_users = User.get_all_users()

    return render_template('all_users.html', all_users=all_users)


@app.route('/user/<int:id>')
def display_one_user(id):
    data = {
        'id' : id
    }

    one_user = User.get_one_user(data)
    return render_template('show_user.html',one_user=one_user)

# ============================ DISPLAY ROUTES =========================================
# ============================ EDIT ROUTES =========================================

@app.route('/user/edit_form/<int:id>')
def edit_user_form(id):

    data = {
    'id' : id
    }

    one_user = User.get_one_user(data)

    return render_template('edit_user.html',one_user=one_user)


@app.route('/user_form/edit/<int:id>',methods=['POST'])
def edit_one_user(id):
    data = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id' : id
    }

    User.edit_one_user(data)

    return redirect('/all_users')



@app.route('/delete/user/<int:id>')
def delete_one_user(id):
    data = {
        'id': id
    }
    User.delete_one_user(data)
    return redirect('/all_users')
