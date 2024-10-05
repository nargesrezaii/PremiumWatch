import environ

env = environ.Env()

environ.Env.read_env('.env')

SECRET_KEY = env('SECRET_KEY')

if env.bool('PROD', default=False):
    from .prod import *
else:
    from .dev import *
