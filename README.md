# Crunchyroll
## Notes
After updating or adding new models, you need to run ```makemigrations``` and the ```migrate```.

After that, make sure new models are added to the ```models/__init__.py```, and models are registered with ```admin.py```.
## API Fetch
Specify the model and the url. e.g.
```
python manage.py fetch Todo https://jsonplaceholder.typicode.com/todos/1
```
