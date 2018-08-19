#Installation

##NOTE: Requires Python and Node.js.

Fork this repository.
* `$ pip install -r requirements.txt`
* `$ npm install`
* `$ python manage.py migrate`
* `$ python manage.py runserver`


rm -f db.sqlite3
rm -r snippets/migrations
python manage.py makemigrations snippets
python manage.py migrate