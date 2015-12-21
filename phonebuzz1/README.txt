(0) Make sure that Django and pip are both installed and up to date

(1) Download ngrok so we can forward a real internet link to localhost:8000

    user$: brew install ngrok
    user$: ngrok 8000

(2) Point your Twilio voice url to the 'Forwarding' HTTP link in the ngrok terminal tab

(3) Open a new tab in terminal and run

    user$: source run_script1.sh

(4) Call your Twilio number as many times as this app will let you. Or until you get really bored.