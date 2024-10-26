# practice_5 Использование Docker в приложении Flask с БД
## Развертывание
1. Для создания кластера необходимо выполнить команду
```
docker-compose up -d --build
```
2. Перейти по адресу http://localhost:5000/ После каждого посещения данной страницы будет изменяться значение счетчика.
3. Для подключения к БД PostgreSQL необходимо использовать следующие данные: Host=localhost;Port=5001;Username=user;Password=password;Database=counter_db
