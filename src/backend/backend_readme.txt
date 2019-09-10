

Pre-Req:

Docker Hub and Docker desktop Approach:

For windows or Mac:
download and install Docker desktop from the following link:

https://www.docker.com/products/docker-desktop

Complete the install steps as documented in above link.

Creation and Deploying docker images:

1.Launch Kitematic (docker repo login will be required to upload docker images to docker repo).
2.Start the command line prompt from Kitematic launch tool option
3.Change directory to "backend" code location - directory where Dockerfile is located
4.Execute the following commands:
	a. docker build -t kasibackend:latest .
	b. To list current running docker containers - docker ps
	c. docker stop <containerid>
	d. docker rm <containerid>
	e. docker run -p 4200:4200 -e PYTHONUNBUFFERED=0 kasibackend:latest
	f. docker-machine ls
	g. Use the ip address and port displayed after executing step f - using any browser

5.To upload the image generated to docker image repository:
	a. docker images
	b. docker tag <ImageId> <yourhubusername>/kasibackend:firsttry
	c. docker push <yourhubusername>/kasibackend

6.With above the docker image is available to be downloaded from any other machine using docker command
7.To download docker image from docker hub:
	a. docker pull <yourhubusername>/kasibackend
	b. To save pulled image: docker save kasibackend > kasibackend.tar
	c. To load from tar file: docker load --input kasibackend.tar



AWS Steps:
1. Create AWS ECR - to store docker images in AWS Registry - either using Web Console or CLI as follows: 
https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-repository.html#how-to-create-repository-console

https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-repository.html#how-to-create-repository-cli

2. Create ECS Instance
	a. https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html
	b. Use the ssh keypair generated from above to remote ssh into the ec2 instance using tool like putty
	c. Use winzip to move the complete backend folder if you want to run the Dockerfile to deploy or
	d. Use the Docker image from ECR to deploy in the ec2 instace

3. Note the ip adress of the backend application EC2 instance to use in the frontend proxy file.

4. The backend application can be secured further with EC2 security policies as required


