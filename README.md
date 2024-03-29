# api_final_yatube
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
5. Создаем пользователя
```
python manage.py createsuperuser
```
6. Запускаем проект
```
python manage.py runserver
```
### Примеры запросов
Пример POST-запроса с токеном Антона Чехова: добавление нового поста.
POST .../api/v1/posts/
```
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
}
```
Пример ответа:
```
{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
```
Пример GET-запроса с токеном Антона Чехова: получаем информацию о группе.
GET .../api/v1/groups/2/
```
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
}
```
### Где посмотреть документацию
Документацию можно посмотреть по адресу http://127.0.0.1:8000/redoc/
### Автор
Evsey, learner and beginner python programmer