# IF YOU'RE IN A BIND ...

# DON'T ASK ME WHY THIS WORKS ...
# If (particularly after modifying the models) you get an error saying 
# that it could not find column name "foo_bar",
# 1. change the app/module folder name (e.g., "wedding" to "theWedding")
# 2. modify references in relevant files:  settings.py, urls.py, admin.py, serializers.py
# 3. delete all files in the app/module's "migrations" folder
# 4. in the TERMINAL run 
#    python manage.py makemigrations NEW_APP_NAME
#    python manage.py migrate --run-syncdb
#    python manage.py runserver


### VIRTUAL ENVIRONMENT STUFF LOCATION(S)
# /Users/ehlerorngard/.local/share/virtualenvs/wedding-hE_WFSQZ/lib/python3.7/importlib/__init__.py