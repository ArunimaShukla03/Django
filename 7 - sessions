In order to take advantage of sessions, instead of having a global variable called "tasks", thus we'll go ahead and delete it and instead we are going to store tasks inside the user's session.

In order to do this, we are going to check to see if tasks is not in "request.session" (where session is kind of a big dictionary representing all the data we have on file inside it about the user) and if not then we add "tasks" as an empty list in a session.

This means if there isn't a list of tasks inside a session then we are creating it and setting it equal to an empty list initially.

And instead of rendering tasks which no longer exists we are rendering "request.session["tasks"]" to pass in the list of tasks to this particular template.

But while running it we get an error saying "no such table: django_session". It turns out that django tends to store data inside of tables, i.e., django stores data about sessions inside of a table. Right now as the table doesn't exist, then we need to create it.

And in order to give django the access to the table it wants to create is to run "python manage.py migrate" in the terminal. This will allow us to create all of the default tables inside of Django's database.

We use {% empty %} when there are no tasks displayed.

Now what needs to change while adding a new task?

Instead of "tasks.append(task)", we need to add to request.session["tasks"] that just contains this one new task.