# petadoptionfile
This project was developed as part of APT 3095: Cloud Computing and Virtualization

The project imitates the idea of a pet adoption file which
you can view pets and  fill some information in the file and the system 
will notify the user if the adoption is successful 

The application aims to streamline the pet adoption process  by automating
part of the processes involved in pet adoption

## Installation

Pre-requisites
   * Local installation of Docker

```
   https://github.com/mwangidennis1/petadoptionfile.git
   cd petadoptionfile
```
## Quickstart

To run the project type the following commands:
```  
    docker-compose up -d --build

    docker-compose exec web python manage.py migrate 

    docker-compose exec web python manage.py makemigrations
```

Go to  http://127.0.0.1:8000/  to see if the project has started

To stop the program from running enter the following command:
```
     docker-compose down
```



