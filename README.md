# Wedding Website backend

This app is an API which serves database data to orngard.com.

More specifically at present it takes and stores users' RSVPs and data from the wedding website hosted at orngard.com.

It is built with Python using the Django framework and a Postgres database.
<br />

#### *Check out the the frontend repo:* **[frontend](https://github.com/ehlerorngard/orngard.com)**

#### *View and try out the website:* **[orngard.com/ehlerandemily](https://www.orngard.com/ehlerandemily)**
<br />*Feel free to try out the RSVP (select RSVP from the menu sidebar)*
<br /><br />

## code excerpts 

### urls.py
<img width="870" alt="urls2" src="https://user-images.githubusercontent.com/34467850/58847511-13345c80-8638-11e9-8b4a-2d8ee257819f.png">

### views.py
<img width="835" alt="InviteeView" src="https://user-images.githubusercontent.com/34467850/58847293-4de9c500-8637-11e9-8590-a214196285cd.png">

<img width="605" alt="csrf view" src="https://user-images.githubusercontent.com/34467850/58847290-4de9c500-8637-11e9-9f51-73cdb59dd2d3.png">

### models.py
<img width="827" alt="Models" src="https://user-images.githubusercontent.com/34467850/58847294-4e825b80-8637-11e9-98dd-34871685bd75.png">

### settings.py
After delineating universal settings, import further customizations according to environment:
<img width="526" alt="settings" src="https://user-images.githubusercontent.com/34467850/58847578-542c7100-8638-11e9-917a-9e245fb8ef9e.png">

### development_settings.py
<img width="752" alt="development_settings" src="https://user-images.githubusercontent.com/34467850/58847292-4de9c500-8637-11e9-899b-a8fd8803d6cf.png">


## technologies utilized 
* Python
* Django
* PostgreSQL
* Psycopg
* Django REST framework
* django-cors-headers
* gunicorn

