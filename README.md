Pre-requisites
  - Local installation of Docker

Go to the command prompt and go to the path 
where you have the file in your local machine

To run the project type the following commands:
    
    docker-compose up -d --build

    docker-compose up -d 

    docker-compose exec web python manage.py migrate 

    docker-compose exec web python manage.py makemigrations

Go to  http://127.0.0.1:8000/  to see if the project has started

To stop the program from running enter the following command:

     docker-compose down

