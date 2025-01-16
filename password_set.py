from app import db, Settings, app  # Импортируйте объект `app` из вашего приложения

# Добавляем специальный пароль
def initialize_admin_password():
    with app.app_context():  # Устанавливаем контекст приложения
        if not Settings.query.filter_by(key="admin_password").first():
            new_setting = Settings(key="admin_password", value="your_password")
            db.session.add(new_setting)
            db.session.commit()

# Выполняем инициализацию
initialize_admin_password()
