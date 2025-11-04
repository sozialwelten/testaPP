from django.db import models

from testapp.settings import BASE_URL
from testapp.utils.helpers import HttpUrl 

class TestappModel:
    def get_remote_name(self) -> str:
        model_name = type(self).__name__.upper()

        if model_name == "USER":
            name = self.name




        return result

