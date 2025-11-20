from django.db import models
from typing import Any

import testapp as ta

def get_local_link(arg, default: Any|None = None) -> Any:
    if isinstance(arg, ta.models.bookcaches.BookCaches):

