

1. cd to folder backend
2. In command prompt - cd path/to/backend
3. set FLASK_APP = app.py
4. flask run
or
4. in command prompt - execute - python app.py
5. With above service starts
6. Browse to: http://localhost:5000/api/simulator-model/ (POST request expected is int array of size 12, application/json)
7. Browse to: http://localhost:5000/api/evaluator-model/ (POST request expected is int array of size 10, application/json)
8. Response for example  can be - "category:3"


Docker Steps:
Follow the steps mentioned below to create docker image and run the same in local:
1. Pre-requisite : Docker is installed and can be run successfully in local environment - windows or linux server
2. Start command prompt/powershell
3. >>> cd to /path/to/backend
3. >>> docker build -t kasibackend:latest .
	a. -t is to tag the docker image
	b. kasibackend is the name of the docker image - can be any string value
	c. latest - indicates the most recently updated version
	d. The . refers to everything under current directory
4. >>> docker images
	a. this will list all the docker images within the current system
5. >>> docker ps
	a. This will list the all running processes
6. >>> docker-machine ls
	a. This is list the running instances - with the ip address
	b. Note down the IP address
7. >>> docker run -p 5000:5000 kasibackend:latest
	a. This will run the docker image - will be available for external browser access - port 5000
8. Launch browser
9. In address bar - enter either:
	a. http://localhost:5000 or
	b. http://<ip-address-from-step-6b>:5000
	c. This will display the swagger ui - will mean everything is running successfully
10.The api endpoints utilize POST methods for the following uris (content type as application/json):
	a. .../api/simulator-model/ - expects input int array of size 10
	b. .../api/evaluator-model/ - expects input int array of size 12
	c. The response for both endpoints will provide the category 




