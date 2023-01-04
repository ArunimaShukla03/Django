Now, when we fill in the information in "http://127.0.0.1:8000/tasks/add" then it generally gives us an error page, FORBIDDEN (403). Here the 403 is the response code that came back, that is, we don't have permission to do this due to "CSRF verification failed".

CSRF stands for Cross-Site Request Forgery. Someone could forge a request to a particular website using some form on their own separate website. That is someone on a different website might trick the user into submitting a form that submits its data to our add task function that adds the added tasks into their task list instead of ours.

In order to avoid these forgeries, we may add a hidden CSRF token to our form which is a unique token that generates with every session, i.e., for every different user they see a different CSRF token which is submitted with the form every time the form is submitted. And our application checks if the token is valid or not.

If it is valid, it'll allow the form submissions to go through. Any other forger wouldn't be able to fake a request to our website as they don't know specifically what the generated token is.

Django has CSRF validation turned on by default which is done via "Django Middleware". It is the ability of Django to intervene in the request response processing of a Django request.

In the "settings.py" of this project we have default features hooked into request-response processing (CSRF view middleware is also present amongst it),

We may directly add the csrf token in "add.html" by "{% csrf_token %}

We may look into it's value by going to the page source. Django checks if the token is valid and then submits. And if someone else goes to this website then they would see a different token.

We created a form here by scratch but they are so often used that django has added a number of ways to make it easier to create forms.

In order to do this, we are going to go to "views.py" and import "forms" from django and then we are going to create a class to represent this form called "NewTaskForm" which will inherit from forms.Form

Inside this form we are going to define all the fields we would like this form to have. So we have the name of the task that will contain a character field with a label called "New Task".

While rendering "add.html", give this template access to a variable called "form" that represents "NewTaskForm" and plug it in "add.html" which will do exactly the same thing for us.

We may also add additional labels to this form (here "priority" where it only takes integer values while also adding constraints in it such as min or max value).

If only one of the fields is filled then django asks the user to fill out the other field. This is called "client-side validation". The server is not getting any of those data but we are using the defined contraints to check if the filled value matches that data.

When we want to validate form, we not only want the client-side validation but also server-side validation, i.e., we also want to check from the server if the inputs are valid.

HOW DO WE DO THIS?

When we are simply trying to GET the add page by typing in the URL, then we just want to render the form. But if we want to POST data by using the POST request method that means we are submitting the form, and now we want to add in a new task in our list of tasks.

So, we want to add in a check for this by adding a condition that says if the method of request is "POST" then we would like to process the result of the request. In a Django form, this is done by creating a new variable called "form", which will be a NewTaskForm.

Here, NewTaskForm(request.POST) contains all of the data that the user submitted when they submitted the form. Now we are creating a "form" variable by taking all of that data and filling it into a "NewTaskForm" which will contain now all of that data that the user submitted.

Now we check if the form data is valid or not (here by the use of "if" statement). Now by using "cleaned_data" which will give us the access to all of the data that the user submitted (here we specifically want task that the user submitted, thus we access "task" variable as the user submits their tasks in this variable). We save all this inside a variable called "task".

Then, as I would like to add this task in list of tasks thus we use "tasks.append(task)".

But if the form is not valid then we return the "tasks/add.html" page again but instead of providing a new form back to them, we send back the existing form data back to them. This is done so we can display information about any errors as well.

Now lets, consider that client and server are validating different things. That is if we change the max_value in the "NewTaskForm" right now and carry on with the older version of the page then it passes the client-side validation but the server-side validatuion then shows an error.

Thus both client and server side validation is important.

Now, if we fill in the tasks in the form and go back to "View Task" then we can also see the newly added tasks. But if after filling in the form we want to be redirected to "index" page we can also do easily by Django.

In order to carry this out, we create a HttpResponse that redirects the user to a particular route. We could have written "/tasks" but we don't wanna hardcore URLs into our application. Therefore, we just ues the name of the route and let django figure out what the route actually is (here by the name "reverse").

We need to import these by "from django.http import HttpResponseRedirect" and "from django.shortcuts import render".

Also remove the ["foo", "baz", "lol"] and make it an empty list.

BUT there is a huge problem with our application right now as the "tasks" added are a global variable right now so anyone visiting the site can see my list of tasks. We can simulate someone else opening the same website by going to the incognito window and opening the same URL.

But this is not what I want as we want personalized tasks for every different user that visits this website.

So in order to do this, we'll introduce the concept of "sessions" in Django for django to remember who you are on subsequent visits but more importantly for it to store your particular information (here to store all your tasks)
