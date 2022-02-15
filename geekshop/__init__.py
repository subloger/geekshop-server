import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'geekshop.settings'
django.setup()

# настрока ORM Django для работы в консоли для комъюнити версии, без нее не работает.
# решение нашел в интернете
