In the newly created "hello" app, we have "views.py" which lets us describe what is it that the user sees when they visit a particular route or where we can decide what gets rendered to the user.

Now we have this newly created "hello" app which we would like to install in our DJANGO project and in order to install it, we would go to settings for this particular django project.

Going to the settings, we have "installed apps" variable which is where Django configures what apps are installed on this project and we may add our newly created app "hello" on this django project.

Now we want this app to display or do something when we visit a particular route.

In order to do this, go to the "views.py" section. Think of each view as something that the user might want to see. And in order to create a view in Django, we're going to define a function.

Here, in "views.py" we have created a function called "index" that by convention takes a request argument. And this is going to be an argument that is going to represent the HTTP request that the user made in order to access our web server.

Now in this index function, we have "HttpResponse" which is a special class created by Django and if we want to use it, we generally need to import it. So in order to access a lot of features provided by Django, we need to import them first.

Here we used "from django.http import HttpResponse" to import our class "HttpResponse" which gives the ability to generate an HttpResponse.

NOW, WHEN SHOULD YOU RETURN THIS RESPONSE?

Now, we need to tell Django, that when one particular URL is visited then this function should run that particular HTTP response.

For this, we need to create "urls.py" file for this particular app. Django has "urls.py" file for the entire project but for the sake of independence or some kind of separation each app contains its own "urls.py" file to control what URLs are available for that particular app.

So, now we have created a "urls.py"  in "hello" app which has a variable "urlpatterns" containing the list of all the allowable URLs that can be accessed for this particular app.

Import "from django.urls import path" and start creating URLs. Here empty string in path means no additional arguments or nothing at the end of the route. And second part contains what view should be rendered when this URL is visited.

We may also give this URL pattern a name which will make it easier to access it later when we might want to link it to things so giving a name to a path can be a useful tool.

The last step in "urls.py" is to import views from the current directory by "from . import views".

The final step is go to the "urls.py" in DJANGO directory which is the "urls.py" file for the entire project and for all the apps which might be contained in this project.

To add our own route or for a particular path to lead to not the admin app but the hello app that we have just now created, we include all the urls in hello application in this "urls.py" file (basically linking these two URL configuration files together).

To do this, use the command "include("hello.urls")".

Now, on typing the "http://127.0.0.1:8000/hello/" as URL we get Hello World!

(as when we access the hello app, the path taken triggers the function "index" from views and thus returns the HttpResponse "Hello World!")

Now we may edit the view function as we please to change the HttpResponse (here "Hello World").

We may add as many views we want. The second view here "arunima" needs to be associated with a particular URL. Thus, again we go to the "urls.py" in the hello directory where we already have a default route represented by the empty string. Now, we may add to this.

Thus when we type in "http://127.0.0.1:8000/hello/arunima" we get "Hello Arunima!" as the HttpResponse.

But this might get tedious after some time, so we just create URL patterns that has placeholder effects by taking an additional parameter such as "name" which returns the HttpResponse by plugging in the name.

Now in the "urls.py" file, in the path we simply write <str:name> followed by the function used and its name. It means that it can be any string now.

Now if we type in any url which is followed by a string, we get the HttpResponse "Hello <String>!" as any string that is typed in the URL will act as the parameter to the function created.

We may also capitalize it by writing name.capitalize in the HttpResponse in the views section.

These Http reponses can be any HTML content but it gets laborious in long HTML codes thus we use a way in which we separate the HTML part of the code from the django code. 