import os
from rich import print

print(os.environgetenv("HELLO", "value does not exist"))