# В файле secret_keys указываются параметры для SMTP
# import secret_keys

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_site_velik',
        'USER': 'root',
        'PASSWORD': 'qwerty1234',
        'HOST': 'db',
        'PORT': '3306',
    }
}

SECRET_KEY = "django-insecure-5rq1i%566u3ljb*y^pa$d#34kjzmi-lstj-0@lskwhm+n_#5s("

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 465

# Указать свои параметры для корректной работы восстановления пароля по электронной почте
# ---------------------------------------------------------------------------------------
# EMAIL_HOST_USER = secret_keys.EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD = secret_keys.EMAIL_HOST_PASSWORD 
EMAIL_HOST_USER = 'YOUR EMAIL'
EMAIL_HOST_PASSWORD = 'YOUR EMAIL HOST PASSWORD'
# ---------------------------------------------------------------------------------------

EMAIL_USE_SSL = True