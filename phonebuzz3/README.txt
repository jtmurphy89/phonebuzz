(0) Open a new tab in your terminal

(1) Download and install RabbitMQ (instructions here: http://www.rabbitmq.com/download.html). Make sure to chown the .erlang_cookie file:

        user$: cd ~
        user$: chown $USER .erlang_cookie

(2) Populate the .env file with the necessary variables (using the ngrok forwarding url for TWILIO_URL, etc.)

(3) Run

        user$: source runscript3.sh

(4) With luck and a fair wind, the server should now be running. Open a new tab and start the celery worker:

        user$: source .env
        user$: celery -A phonebuzz3 worker -l info

(5) Again, with a bit of luck and hopping up and down on one foot while chanting in sanskrit, the celery worker should be running and you can head over to http://localhost:8000 to schedule some phonebuzz calls in the future