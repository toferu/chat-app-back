web: daphne chat_api.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=chat_api.settings -v2