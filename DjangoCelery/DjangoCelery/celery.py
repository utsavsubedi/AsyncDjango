from __future__ import absolute_import, unicode_literals
import os 

from celery import Celery 
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoCelery.settings')

app = Celery('DjangoCelery')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kathmandu')

app.config_from_object(settings, namespace ='CELERY')

#Celery Beat Setting
app.conf.beat_scchedule = {
    
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
