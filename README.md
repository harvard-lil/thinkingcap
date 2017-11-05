## Getting up and running
You will need postgres for this project so if you don't have it,[Download and install Postgres](https://www.postgresql.org/download/)

```
$ git clone git@github.com:harvard-lil/thinkingcap.git
$ cd thinkingcap
$ createdb thinkingcap
$ fab install_reqs
$ fab init_db
```
create settings.py
```
$ cp config/settings.example.py config/settings.py
```

if you would like to make a new app:
```
$ django-admin startapp your-app-name
$ cd your-app-name
```


## Application specific settings
#### Colors
```
$ ./manage.py shell
```
In your shell
```python
# colors live in config/settings.py if you want to edit them 
from colors import resources
from django.conf import settings
resources.create_colors(settings.COLOR_LIST)
resources.create_API_settings()
```
