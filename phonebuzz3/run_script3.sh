rabbitmq-server -detached
rabbitmqctl add_user myuser mypassword
rabbitmqctl add_vhost myvhost
rabbitmqctl set_user_tags myuser mytag
rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
source .env
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8000