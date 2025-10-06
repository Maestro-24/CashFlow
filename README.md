# 💰 CashFlow - Система учета финансовых операций

## 📋 О проекте

Приложение позволяет:
- 📊 Вести учет финансовых операций
- 🏷️ Классифицировать операции по статусам, типам, категориям и подкатегориям
- 🔍 Фильтровать и анализировать данные
- 📈 Управлять справочниками категорий
- ✏️ Редактировать и удалять записи

## 🛠 Технологии

**Backend:** Django 4.2+  
**Database:** SQLite  
**Frontend:** Bootstrap 5, jQuery

## 📁 Структура проекта

<img width="617" height="670" alt="image" src="https://github.com/user-attachments/assets/2421b111-a163-440d-a9b8-cb431400dfa6" />


🚀 Быстрый старт
Предварительные требования
Python 3.8 или выше
pip (менеджер пакетов Python)

<b> Установка и запуск </b>

1.  **Скачайте проект и перейдите в его директорию** 
    
2.  **Создайте виртуальное окружение**
    
    **Windows:**

    python -m venv venv

    venv\Scripts\activate

    **macOS/Linux:**

    python3 -m venv venv

    source venv/bin/activate

3.  **Установите зависимости**

    cd cashFlow
   
    pip install -r requirements.txt

4.  **Настройте базу данных**

    python manage.py makemigrations
 
    python manage.py migrate

5.  **Создайте суперпользователя (опционально)**

    python manage.py createsuperuser

    Следуйте инструкциям для создания учетной записи администратора.

6.  **Запустите сервер разработки**

    python manage.py runserver

7.  **Откройте приложение в браузере**

    http://127.0.0.1:8000/


🔧 Администрирование
Для доступа к стандартной панели администратора Django:

    1.Перейдите по адресу http://127.0.0.1:8000/admin/
    2.Введите данные суперпользователя
    3.Управляйте всеми моделями через интерфейс администратора


# 📸 Скриншоты работы программы
## Главная страница со списком операций
<img width="1312" height="701" alt="image" src="https://github.com/user-attachments/assets/cb8d0933-b0db-4591-9940-29ff86295622" />

## Форма добавления/редактирования записи
<img width="865" height="527" alt="image" src="https://github.com/user-attachments/assets/3587a31e-cf26-4c31-81f8-0cef28e6eb42" />

## Управление справочниками
<img width="1311" height="721" alt="image" src="https://github.com/user-attachments/assets/b52e19a0-6f44-4376-9062-f553b38a086a" />


