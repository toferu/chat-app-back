web: daphne chat_api.asgi:application --bind=0.0.0.0:$PORT -v2
chatworker: python manage.py runworker --settings=chat_api.settings -v2