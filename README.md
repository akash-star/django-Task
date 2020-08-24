# Django Scheduling API

### making a Scheduling API by Django REST Framework

##### ABSTRACT: 
###### Django API for scheduling. The application is build in python Django REST framework. The django model accepts two parameters url and time.The Specification defines an API to Schedule a task on a Specified time. The task is to return the url if it matches the time specified mentioned. if it matches the

### Working mechanism:
    1. first we have to call the API with a url_for_site containng a url and a timestamp containing a date and time in specific format and It would be a POST call. This will schedule the task for us.

    2. Then if the current date and time matches with the one specified at the time of POST request the api will send a GET request request to the url and it will return a status code.

    3. the call to http://127.0.0.1:8000/main-content/ will make a GET call to the database to retrieve all the existing scheduled tasks and also provides a interface to create a scheduled task by POST request.
    
    4. we can make a GET call by passing 2 parameters (a DATE-TIME format as 1st parameter and a URL as 2nd parameter) to retrieve a perticular scheduled task.
        The url structure of the call should be like: http://127.0.0.1:8000/main-content/Date-Time&URL 
    
    5. the api with endpoint '/ping' e.g: 'http://127.0.0.1:8000/ping' returns a response of 'status': 'OK' to make sure that the server is alive
