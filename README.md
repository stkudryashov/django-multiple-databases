## _How to use multiple databases in Django_

****

### Dependency installation
From `requirements.txt` install all requirements
- _Django 3.2_
- _mysqlclient 2.0.3_


### Database configuration
In the `settings.py` set the databases
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_core',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    },
    'movie': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_movie',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    },
    'song': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_song',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```


### Router creation
In folder `routers` create file `db_routers.py`
```python
class DatabaseRouter:
    route_app_labels = {'movie', 'song'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return model._meta.app_label
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return model._meta.app_label
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == app_label
        return db == 'default'
```
`route_app_labels` - applications that have their own database


### Router connection
In the `settings.py` set your router
```python
DATABASE_ROUTERS = [
    'routers.db_routers.DatabaseRouter',
]
```


### Specify the base for the model
If you want to specify a database for the model from another application, do it in the meta class
```python
class Song(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    album = models.CharField(max_length=255, verbose_name='album')
    duration = models.PositiveIntegerField(verbose_name='duration')


class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    duration = models.PositiveIntegerField(verbose_name='duration')

    class Meta:
        app_label = 'movie'
```

### Performing migrations
`python manage.py migrate` to migrate a default database\
`python manage.py migrate --database=movie` to migrate a movie database

_Migrations are performed separately for each database_
