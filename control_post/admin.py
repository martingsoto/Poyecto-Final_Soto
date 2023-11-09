from django.contrib import admin

# Register your models here.

from control_post.models import usuario, blogpost, genero

admin.site.register(usuario)
admin.site.register(genero)
admin.site.register(blogpost)