from mongoengine import connect
from decouple import config

connect(
    db=config('MONGO_DB_NAME', default='coffee_shop'),
    host=config('MONGO_HOST', default='localhost'),
    port=config('MONGO_PORT', default=27017, cast=int)
)