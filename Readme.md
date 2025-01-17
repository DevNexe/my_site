Это мой сайт блог созданный на Flask он поддерживает систему аккаунтов пользователей и администраторов. Администраторы могут создавать, редактировать и просматривать посты. А пользователи только имеют право просматривать посты. 

## Возможности
- Регистрация и вход пользователей
- Установка тем (Например: Темная тема)
- Просматривание постов (Доступно всем пользователям)
- Создание и редактирование постов (Доступно только с админ аккаунтов)

## Скриншоты сайта
Темная тема:
![Главная страница от лица админа](/preview_images/dark1.png)
![Главная страница от лица пользователя](/preview_images/dark5.png)
![Главная страница от лица не авторизованого](/preview_images/dark4.png)
![Страница входа в аккаунт](/preview_images/dark7.png)
![Страница регистрации аккаунта](/preview_images/dark8.png)
![Страница редактирования поста](/preview_images/dark6.png)
![Боковая панель](/preview_images/dark2.png)
![Переключатель темы](/preview_images/dark3.png)

Светлая тема:
![Главная страница от лица админа](/preview_images/light1.png)
![Главная страница от лица пользователя](/preview_images/light8.png)
![Главная страница от лица не авторизованого](/preview_images/light4.png)
![Страница входа в аккаунт](/preview_images/light6.png)
![Страница регистрации аккаунта](/preview_images/light7.png)
![Страница редактирования поста](/preview_images/light5.png)
![Боковая панель](/preview_images/light2.png)
![Переключатель темы](/preview_images/light3.png)

## ВАЖНО
Чтобы создать админ аккаунт используйте:
   ```
   your_password
   ```

Чтобы установить свой админ парроль сделайте:
1. Откройте ```password_set.py``` в любом редакторе текста.

2. замените ```your_password``` на свой пароль. (ВАЖНО: Пароль не должен содержать кирилльские буквы или пробелы)

## Установка
Чтобы запустить проект локально, выполните следующие шаги:
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/DevNexe/my_site.git
   ```

2. Установите все зависимости:
   ```bash
   pip install pip install -r requirements.txt
   ```

## Запуск приложения
Чтобы запустить сайт выполните следующие шаги:
1. Запустите код:
   ```bash
   python app.py
   ```

2. Остановите код комбинацией клавиш:
   ```
   Ctrl+C
   ```

3. Запустите код:
   ```bash
   python password_set.py
   ```
   
4. Снова остановите код комбинацией клавиш:
   ```
   Ctrl+C
   ```
   
5. Заново запустите код:
   ```bash
   python app.py
   ```

6. Перейдите на:
   ```
   http://127.0.0.1:5000
   ```

Вот и все надеюсь вам понравился мой сайт.
Спасибо за чтение описания!
Желаю вам удачи и успехов.
