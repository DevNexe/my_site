from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from werkzeug.utils import secure_filename

# Инициализация приложения
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

db = SQLAlchemy(app)

# Убедитесь, что папка для загрузки существует
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Модель для пользователей
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

# Модель для публикаций
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(200))

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.String(255), nullable=False)

# Главная страница с публикациями
@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts, logged_in=session.get('logged_in'), is_admin=session.get('is_admin'))

# Страница для создания новой публикации
@app.route('/create', methods=['GET', 'POST'])
def create():
    if not session.get('is_admin'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image = request.files['image']

        image_filename = None
        if image and image.filename != '':
            image_filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))

        new_post = Post(title=title, content=content, image_filename=image_filename)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')


# Страница для редактирования публикации
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if not session.get('is_admin'):
        return redirect(url_for('index'))

    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        image = request.files['image']

        if image and image.filename != '':
            # Удаление старого изображения
            if post.image_filename:
                old_image_path = os.path.join(app.config['UPLOAD_FOLDER'], post.image_filename)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
            
            image_filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
            post.image_filename = image_filename

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', post=post)


# Удаление публикации
@app.route('/delete/<int:id>')
def delete(id):
    if not session.get('is_admin'):
        return redirect(url_for('index'))

    post = Post.query.get_or_404(id)
    if post.image_filename:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], post.image_filename))
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

# Регистрация
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_admin = 'is_admin' in request.form
        
        # Проверка наличия admin_password в базе
        admin_password_entry = Settings.query.filter_by(key="admin_password").first()
        if is_admin:
            if not admin_password_entry:
                return "Admin password is not set in the database.", 400
            
            stored_password = admin_password_entry.value
            provided_password = request.form.get('admin_password')
            if provided_password != stored_password:
                return "Invalid admin password.", 403

        # Создание пользователя
        new_user = User(username=username, password=generate_password_hash(password), is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html')

# Вход
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            session['is_admin'] = user.is_admin
            return redirect(url_for('index'))
        return 'Invalid credentials!'
    return render_template('login.html')

# Выход
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
