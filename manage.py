Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... import os
... import sys
... 
... if __name__ == "__main__":
...     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
... 
...     try:
...         from django.core.management import execute_from_command_line
...     except ImportError as exc:
...         raise ImportError(
...             "Couldn't import Django. Are you sure it's installed and "
...             "available on your PYTHONPATH environment variable? Did you "
...             "forget to activate a virtual environment?"
...         ) from exc
... 
...     execute_from_command_line(sys.argv)
