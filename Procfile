web: daphne chat_api.asgi:application --port $PORT --bind 0.0.0.0:8000 --ssl-cert /app/.heroku/ssl/cert.pem --ssl-key /app/.heroku/ssl/privkey.pem

chatworker: python manage.py runworker --settings=chat_api.settings -v2

