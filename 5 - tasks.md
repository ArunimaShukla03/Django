First we create a new app called "tasks" and follow all the steps initially followed after we create an app.

Now we want to render a page that displays a list of all of the tasks.

First we create a global variable called "tasks" containing random tasks.

Now inside the function we have the key "tasks" that contains the variable "task" so we can use it when django is rendering it.

Instead of just being static value now it is dynamic.

Now we actively want to add in a new task by essentially creating a form.

Thus now in the "tasks" app "views.py" we add in a new function called "add". We create a new HTML file which allows the user to put in new "task" and add the route in the "urls.py" section in the "tasks" app.

Now django provides us "template inheritance" that is better than copying and pasting similar HTML files.

For this we have a file called "layout" that the other files are going to inherit from (here index.html and add.html) where the structure of the page is the same for both of the pages and all we need to write is what differs in both of the pages.

Here, in index.html and add.html only has difference in their body.

For this, we create a new file called layout.html in templates/tasks which contains the layout which is same for both of the pages.

In this, we add in {% block body %}
{% endblock %} where the basic difference is.

For add.html and index.html we remove everything except where the different content is.

Also, while defining the link it is not necessary to write a link that is rigid instead we may write something like {% url 'add' %} that makes it more flexible (link to url called "add"). This shows the importance of giving names during writing paths in "urls.py".

But this could also cause namespace collision as "index" is a common name in different apps so the href link might not work.

An easy way to fix this is inside "urls.py" for my "tasks" app, let me give each of these urls an app name (here "tasks"). Then while linking, we write "{% url 'tasks:index' %}", this makes sure that the index used is the one under "tasks" app. And likewise change the url in "index.html" too.

Now in order to add action to a form, i.e., for it take that form information and submit it somewhere. And the url with it represents where the page would land after we submit in all the information (here it would land back to the 'add' page again).

We use a method called "post".

In opposition of the "get" request method which is used when we want to get a particular page, if we want to change the state inside the application then we use a different request method called "post" (here we are changing the state of the list of tasks that is stored inside the application).

"Post" is generally used for submitting form data.

This will allow the data to send to the "add" route.