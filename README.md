
**ENV**

mamba activate mydjangocelery


**python manage.py migrate**

docker run -p 127.0.0.1:6379:6379 --name redis-celery -d redis

python manage.py qcluster
