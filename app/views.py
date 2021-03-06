from app import app
from flask import render_template, request, redirect, url_for, session
from app.modal import User, Bucket
from app.application import Application


@app.route('/')
def home():
    """This page is to return the home page"""

    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    checks if all inputs have been filled, if so it creates checks if the passwords match each other and
    if so creates a user otherwise returns an error
    :return:
    """
    if request.method == "POST":
        if request.form["first_name"] and request.form["second_name"] and request.form["email"] and request.form[
            "password"] and request.form["confirm_password"]:
            if request.form["password"] == request.form["confirm_password"]:
                user = User(request.form["first_name"], request.form["second_name"],
                            request.form["email"], request.form["password"], request.form["confirm_password"])
                application = Application()
                if application.register(user):
                    return redirect(url_for('home'))
            return render_template('signup.html', error='passwords dont match')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
       get email and password, log in the user and store the email in the session
    :return:
    """
    if request.method == "GET":
        return render_template('index.html')
    else:
        if request.form["email"] and request.form["password"]:
            application = Application()
            if application.log_in(request.form["email"], request.form["password"]):
                session['email'] = request.form["email"]
                return redirect(url_for('buckets'))
            return render_template('index.html', error='invalid username or password')
        return render_template('index.html', error='Please enter email and password')


@app.route('/buckets', methods=['GET', 'POST'])
def buckets():
    """

    :return:
    """
    application = Application()
    current_user = application.current_user(session['email'])
    if not current_user:
        return redirect(url_for('login'))
    error = None
    if request.method == 'POST':
        title = request.form['title']
        if title:
            if current_user.add_bucket(Bucket(application.random_id(), title)):
                return redirect(url_for('buckets'))
    return render_template('mybucket.html', error=error, buckets=current_user.buckets, user=current_user)


@app.route('/bucket/edit/<identify>', methods=['GET', 'POST'])
def edit_bucket(identify):
    """

    :param identify:
    :return:
    """
    application = Application()
    current_user = application.current_user(session['email'])
    if not current_user:
        return redirect(url_for('login'))
    bucket = current_user.get_user_bucket(identify)
    if not bucket:
        return redirect(url_for('buckets'))
    if request.method == 'POST':
        if current_user.edit_bucket(identify, request.form['name']):
            return redirect(url_for('buckets'))
    return render_template('edit_bucket.html', user=current_user, bucket=bucket)


@app.route('/bucket/delete/<identify>', methods=['GET', 'POST'])
def delete_bucket(identify):
    """

    :param identify:
    :return:
    """
    application = Application()
    current_user = application.current_user(session['email'])
    if not current_user:
        return redirect(url_for('login'))
    bucket = current_user.get_user_bucket(identify)
    if not bucket:
        return redirect(url_for('buckets'))
    if request.method == 'POST':
        if current_user.delete(identify):
            return redirect(url_for('buckets'))
    return render_template('delete_bucket.html', user=current_user, bucket=bucket)


@app.route('/bucket/items/<identifier>')
def items(identifier):
    """

    :param identifier:
    :return:
    """
    application = Application()
    current_user = application.current_user(session['email'])
    if not current_user:
        return redirect(url_for('login'))
    bucket = current_user.get_user_bucket(identifier)
    if not bucket:
        return redirect(url_for('buckets'))
    return render_template('items.html', bucket=bucket)

@app.errorhandler(404)
def page_not_found(e):
    """
    The page to return in case a route is not defined.
    :param e:
    :return:
    """
    return render_template('404.html'), 404