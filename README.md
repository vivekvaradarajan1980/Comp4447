## Comp4447 project work

#### An interactive Flask based Web-App application that can predict using Arima/Sarima or Prophet the closing stock prices for any ticker of your choice


### To get started clone this repository in your personal workspace on your machine using `git clone https://github.com/vivekvaradarajan1980/Comp4447.git`

- Navigate into the directory where you clone this repository on your local machine

- Then install all the dependencies in the python requirements.txt using `pip install -r requirements.txt`

- Then run from your terminal 'flask run' or `python -i App.py`
(`flask run` opens the application in port 5000 which is the default but if you use `python -i App.py` it will run it in whatever port you configure it too in the App.py file. !!!)

- To run in Docker run "docker compose up -d" in your terminal (if you have port 5000 binded to something else you may have to change ports in the .yml)  

- Navigate to your browser to localhost:XXXX where XXXX is whatever port your application is running on.
