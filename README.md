## Inventory Management System
*(building REST APIs using Django and Django REST Framework)*
by **Animesh Kumar**

### Table of contents
* [How to Execute](#how-to-execute)
* [Features for Employees](#features-for-employees)
* [Features for Managers](#features-for-managers)
* [Contact developer](#contact-developer)

### How to Execute
To be able to run this REST API server locally, open a terminal and execute

* >mkdir mydir
* >cd mydir
* make sure that virtualenv is created in a python3 version 3.8.x or more.
     >virtualenv myenv
* >source myenv/bin/activate
* >git clone https://github.com/Animesh241100/inventory-management-api.git
* >cd inventory-management-api/src
* >pip3 install -r requirements.txt
* >python manage.py runserver

and you should see the server is up at the IP `http://127.0.0.1:8000/`

You can start making API requests to this server using some tool like `Postman`.

### Features for Employees
* View available list of equipments (GET)
```http
http://127.0.0.1:8000/api/employee/equipments
```
Here `pk` can be any number starting from 1 to 5 to uniquely identify the equipments.(there are only 5 equipments as of now, add more from django-admin).

* Issue a particular piece of equipment to the manager (GET) 
```http
http://127.0.0.1:8000/api/employee/issue/{pk}
```
* Return a particular piece of equipment to the manager (GET). 
```http
http://127.0.0.1:8000/api/employee/return/{pk}
```
* Request access for an unissued equipment (GET). 
```http
http://127.0.0.1:8000/api/employee/request-access/{pk}
```
### Features for Managers
* View available pieces of equipments (GET)
```http
http://127.0.0.1:8000/api/manager/available
```
* View issued pieces of equipments (GET)
```http
http://127.0.0.1:8000/api/manager/issued
```

* View access requests by employees (GET). It will return all the equipment objects along with the number of requests submitted to access the resepctive equipment.
```http
http://127.0.0.1:8000/api/manager/requests
```

### Contact Developer
##### Animesh Kumar
* +91 7985851496
* 24animesh11@gmail.com

