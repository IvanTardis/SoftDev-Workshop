"""
View functions for the application.
"""
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.models import User, Blog, Entry
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    blogs = Blog.query.all()
    return render_template('index.html', blogs=blogs)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/create_blog', methods=['GET', 'POST'])
@login_required
def create_blog():
    if request.method == 'POST':
        title = request.form['title']
        new_blog = Blog(title=title, user_id=current_user.id)

        db.session.add(new_blog)
        db.session.commit()

        flash('Blog created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('create_blog.html')

@app.route('/edit_blog/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def edit_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)

    if blog.user_id != current_user.id:
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        blog.title = request.form['title']
        db.session.commit()
        flash('Blog updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('edit_blog.html', blog=blog)

@app.route('/view_blog/<int:blog_id>')
def view_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    entries = Entry.query.filter_by(blog_id=blog.id).all()
    return render_template('view_blog.html', blog=blog, entries=entries)
