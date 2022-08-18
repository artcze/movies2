from django.db.models import CharField, DateField, Model, FloatField, ForeignKey, IntegerField, TextField, \
    DateTimeField, DO_NOTHING


class Genre(Model):  # w django musi dziedziczyć po klasie Model
    name = CharField(max_length=128)


# description = CharField(max_length=128, default=None) # defaukt=None to ze pole nie jest wymagane

# migracaj -> specjaly kod, wylapuje zmiany
# python manage.py makemigrations - dodanie migracji
# python manage.py migrate - wykonanie migracji
#
class Actor(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    #    birth = DateField(default=None,null=True)
    phone = CharField(max_length=20)
    email = CharField(max_length=20)
    salary = FloatField(default=10000.0)


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)


