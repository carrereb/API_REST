# API_REST

## advanced of the project

The main difficulty is to understand how Django works because I never used this framework.  
To help me understand this framework better, I found :

- Django documentation : https://docs.djangoproject.com/en/4.1/
- Tutorials on Openclassrooms :
    + to understand how Django works : https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django
    + to set up the API : https://openclassrooms.com/fr/courses/7192416-mettez-en-place-une-api-avec-django-rest-framework
- To understand the json display : https://www.delftstack.com/howto/django/django-create-json-response/

Now, the difficulty is to understang how can I import a json file for the POST request.  
  
I found a way to do that using Django REST Framework and I change the structure of my code to adapt it to the framework.  
  
Now, I have two difficulties :
- create the client for the chargepoint giving in the URL
- make that each URL use an only one method (GET, POST or DELETE)

I decided to use netcat and telnet to test my POST and DELETE requests.  
I modified my code with the help of the website https://www.django-rest-framework.org/tutorial/3-class-based-views/  
This allowed me to better understand how I can manage the different requests.  
