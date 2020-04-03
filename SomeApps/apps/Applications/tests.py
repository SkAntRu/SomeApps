from django.test import TestCase

from Applications.models import Application


def create_application(title='test application title'):
    """
    Create a new application
    """
    return Application.objects.create(title=title)


class ApplicationModelTests(TestCase):

    def test_change_api_key_empty_key(self):
        """change_api_key return error if new_key is empty"""

        new_app = create_application()
        empty_key = ''
        self.assertEqual(new_app.change_api_key(empty_key),
                         'New API key have to be not empty and in range 0 < lenght <= 16',
                         'change_api_key not return error'
                         )

    def test_change_api_key_big_lenght_key(self):
        """change_api_key return error if lenght of new_key bigger than 32 digits"""

        new_app = create_application()
        big_lenght_key = '1'*33
        self.assertEqual(new_app.change_api_key(big_lenght_key),
                         'New API key have to be not empty and in range 0 < lenght <= 16',
                         'change_api_key not return error'
                         )

    def test_change_api_key_existing_key(self):
        """change_api_key return error if new_key belong to another Apllication instance"""

        new_app = create_application()
        new_app_key = new_app.api_key
        another_app = create_application('another application')

        self.assertEqual(another_app.change_api_key(new_app_key),
                         f'Another application exists with key={new_app_key}',
                         'change_api_key not return error'
                         )

    def test_change_api_key_happyend(self):
        """change_api_key return None and changed api_key"""

        new_app = create_application()
        new_key = '1'*10

        self.assertEqual(new_app.change_api_key(new_key),
                         None,
                         'change_api_key not return None'
                         )
        self.assertEqual(new_app.api_key,
                         new_key,
                         'change_api_key not saved new_key in instance'
                         )
