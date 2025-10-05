📋 О проекте
Приложение позволяет:
📊 Вести учет финансовых операций
🏷️ Классифицировать операции по статусам, типам, категориям и подкатегориям
🔍 Фильтровать и анализировать данные
📈 Управлять справочниками категорий
✏️ Редактировать и удалять записи

🛠 Технологии
Backend: Django 4.2+
Database: SQLite
Frontend: Bootstrap 5, jQuery


📁 Структура проекта

cashflow-project/
├── cashFlow/              # Основной проект Django
│   ├── task/              # Приложение финансового учета
│   │   ├── migrations/    # Миграции базы данных
│   │   ├── templates/     # HTML шаблоны 
│   │   │   ├──base.html  
│   │   │   ├── finance/
│   │   │   │   ├── record_list.html
│   │   │   │   ├── record_form.html
│   │   │   │   ├── record_confirm_delete.html
│   │   │   │   ├── reference_management.html
│   │   │   │   └── edit_reference.html
│   │   ├── models.py      # Модели данных
│   │   ├── views.py       # Представления
│   │   ├── urls.py        # Маршруты
│   │   ├── forms.py       # Формы
│   │   ├── admin.py       # Данные
│   │   ├── tests.py       # Проверка функциональности
│   │   └── apps.py        # Конфигурация приложения
│   ├── cashFlow/
│   │   ├── asgi.py        # Развертывание
│   │   ├── settings.py    # Настройка проекта
│   │   ├── urls.py        # Маршрутизация
│   │   └── wsgi.py        # Развертывание
│   ├── manage.py          # Django management script
│   └── db.sqlite3         # База данных
├── requirements.txt       # Зависимости
└── README.md              # Эта документация


🚀 Быстрый старт
Предварительные требования
Python 3.8 или выше
pip (менеджер пакетов Python)

<b> Установка и запуск </b>

1.  Скачайте проект и перейдите в его директорию
    cd cashflow-project
    
2.  Создайте виртуальное окружение
    
    Windows:
    
    python -m venv venv
    venv\Scripts\activate
    
    macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate

3.  Установите зависимости

    cd cashFlow
    pip install -r requirements.txt

4.  Настройте базу данных

    python manage.py makemigrations
    python manage.py migrate

5.  Создайте суперпользователя (опционально)

    python manage.py createsuperuser
    Следуйте инструкциям для создания учетной записи администратора.

6.  Запустите сервер разработки

    python manage.py runserver

7.  Откройте приложение в браузере

    http://127.0.0.1:8000/


🔧 Администрирование
Для доступа к стандартной панели администратора Django:

1.Перейдите по адресу http://127.0.0.1:8000/admin/
2.Введите данные суперпользователя
3.Управляйте всеми моделями через интерфейс администратора