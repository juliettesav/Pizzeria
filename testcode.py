import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django 
django.setup()

from pizzas.models import *


menu = Pizza.objects.all()

print(menu)

#for p in menu: 
#    print(p)
#    print(p.text)
#    print(p.date_added)

p = Pizza.objects.get(id=1)
print(p)

entries = Entry.objects.filter(item=p)

for e in entries: 
    print(e)
    print(e.date_added)

from django.contrib.auth.models import User 

for user in User.objects.all():
    print(user.username)
    print(user.last_login)
