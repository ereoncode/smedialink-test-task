### Задание на позицию Django-разработчика 

Необходимо создать RESTful API для проведения аукционов по словесному описанию:

1) Должен быть реализован механизм регистрации пользователя, получения токена и дальнейшей авторизации запросов по токену.
2) Пользователь может получить список всех аукционов, зарегистрированных в системе. Используя фильтр в запросе, можно получить все, только активные или только завершенные аукционы.
3) Пользователь может создать новый аукцион установив описание товара, начальную цену, шаг цены и время окончания аукциона. В момент когда новый аукцион создан, всем зарегистрированным пользователям системы отправляется сообщение по электронной почте о том, что у них есть возможность присоединится к торгам.
4) Обновлять поля аукциона, указанные при создании, нельзя. Удалять созданные аукционы нельзя.
5) Если пользователь не является хозяином аукциона, то должна иметься возможность сделать ставку, если аукцион активен. При этом её размер должен быть свалидирован, исходя из предыдущей цены и шага. Изменять или удалять ставки нельзя.
6) Если пользователь сделал на конкретном аукционе хотя бы одну ставку, то информация о изменении цены этого аукциона должна доставляться на электронную почту пользователя при каждой новой ставке от других пользователей.
7) При получении детальной информации об аукционе необходимо вернуть поля, указанные при его создании + список сделанных на него ставок с именами пользователей, которые их сделали.
8) В момент, когда время аукциона подошло к концу, система должна прекратить прием новых ставок, автоматически определить победителя и разослать всем, кто участвовал в торгах, уведомления по почте об их прекращении.


#### Установка
    
```shell
$ git clone https://github.com/ereoncode/auction.git
$ cd auction
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ touch .env
```

Пример содержимого ```.env``` файла:

```.env
SECRET_KEY="-v+*#)o%3i)yn8$378230&3%f^g_tt5ow-gkie4x@l9f350m3g"
ALLOWED_HOSTS = localhost, 127.0.0.1, 0.0.0.0
DOMAIN_NAME=auction.com
SITE_ID=1

ADMIN_USERNAME=admin
ADMIN_PASSWORD=Ferwbjy13@
ADMIN_EMAIL=admin@auction.com

DATABASE_NAME=auction
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432

CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379

SMTP_HOST=smtp.auction.com
SMTP_PORT=429
SMTP_USER=noreply@auction.com
SMTP_PASSWORD=Pa$$w0rd
SMTP_USE_TLS=True

```

#### Запуск
* Build Redis docker image
```sh 
sudo docker pull redis
```
* Run Redis
```sh
sudo docker run --rm --name=redis-devel --publish=6379:6379 --hostname=redis redis:latest
```
* Run celery workers
```sh 
celery -A web_auction worker -l info
celery -A web_auction flower -l info
```
* Run Django application
```sh
python manage.py runserver 0.0.0.0:8000
```

#### Docs:
* [Swagger](https://swagger.io) available on http://0.0.0.0:8000/swagger/
* [Redoc](https://rebilly.github.io/ReDoc/) available on http://0.0.0.0:8000/redoc/
