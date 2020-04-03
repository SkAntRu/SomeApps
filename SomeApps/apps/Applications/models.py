from django.db import models

import secrets


class Application(models.Model):
    """Приложение с Название приложения, Ключ API

    Ключ API генерируется изначально с помощью secrets.token_hex(16)
    Для изменения ключа необходимо вызывать метод change_api_key(str), len(str)<=16


    """

    def __str__(self):
        return f'ID: {self.id}, Title: {self.title}'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,
                             verbose_name='Title',
                             null=False,
                             blank=False)
    api_key = models.CharField(max_length=32,
                               verbose_name='date published',
                               default=secrets.token_hex(16),
                               null=False,
                               blank=False)

    def change_api_key(self, new_key):
        """Change api_key of instance

        input:
            new_key: str

        return:
            error_text or """
        if new_key and len(new_key) <= 32:
            if len(Application.objects.filter(api_key=new_key)) == 0:
                self.api_key = new_key
                self.save()
            else:
                return f'Another application exists with key={new_key}'
        else:
            return 'New API key have to be not empty and in range 0 < lenght <= 16'
