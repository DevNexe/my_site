from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
db = SQLAlchemy(app)
passcode = str(input("Введите спец. пароль который вы хотите установить для создания админ аккаунтов: "))

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.String(255), nullable=False)

# Добавляем специальный пароль
def initialize_admin_password():
    with app.app_context():  # Устанавливаем контекст приложения
        if not Settings.query.filter_by(key="admin_password").first():
            new_setting = Settings(key="admin_password", value=passcode)
            db.session.add(new_setting)
            db.session.commit()

# Выполняем инициализацию
initialize_admin_password()
