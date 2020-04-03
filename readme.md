Hello, it is my conversation task proving that i could work with DRF

To install project:
* Copy Repo
* install requirements
```pip install -r requirements.txt```
* ```python manage.py createsuperuser```
* ```python manage.py migrate```

About project urls

**api/v1/applications/create**
Create new application
Require authentification
GET: return all applications
POST: create new application.
requirements:
body={"title": 'Some Application', -- Required
"api_key": '7e58cde3e22d306ac49677d057000c41' -- Optional
}
api_key have to be string with 0 < len(api_key) <= 32
If not implement "api_key", it will generate automatically

**api/v1/applications/**
GET: Return all applications

**api/test/**
Get Application By Api Key
GET: return all applications
POST: return application with api_key=request.data['api_key']
requirements:
body={"api_key": "7e58cde3e22d306ac49677d057000c41"}

**api/v1/application/change_api_key**
Change Api Key
Require authentification
GET: return all applications
POST: change api_key in application.
Return True of Error Message
requirements:
body={"title": 'Some Application',
"new_api_key": '7e58cde3e22d306ac49677d057000c41'
}
api_key have to be string with 0 < len(api_key) <= 32

**api-auth/**
Default login DRF page

**admin/**
Default Django Admin page