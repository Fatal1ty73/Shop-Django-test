#Installation

##NOTE: Requires Python and Node.js.

Fork this repository.
* `$ pip install -r requirements.txt`
* `$ npm install`
* `$ python manage.py migrate`
* `$ python manage.py runserver`


rm -f db.sqlite3
rm -r snippets/migrations
python3 manage.py makemigrations shop_api
python3 manage.py migrate