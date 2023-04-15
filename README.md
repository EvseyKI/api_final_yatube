# python telegram bot-assistant
API для сервиса yatube. Позволяет запрашивать данные о постах, группах и комментариях в социальной сети Yatube, а также управлять ими. Через этот интерфейс смогут работать мобильное приложение или чат-бот; через него же можно передавать данные в любое приложение или на фронтенд.
### Технологии
- Python 3.9
- Django 3.2
- DRF
- JWT + Djoser
### Для запуска
1. Клонируем репозиторий и переходим в api_final_yatube
```
git clone git@github.com:EvseyKI/api_final_yatube.git
```
2. Создаем и активируем виртуальное окружение
```
python -m venv env
source venv/bin/activate
```
3. Устанавливаем необходимые зависимости из requirements
```
pip install -r requirements.txt
```
4. Делаем миграции данных
```
python manage.py migrate
```
5. Запускаем проект
```
python manage.py runserver
```
### Авторы
Евсей
