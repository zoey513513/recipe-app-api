"""
django command to wait for the database to be available
"""

from lib2to3.pytree import Base
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
      