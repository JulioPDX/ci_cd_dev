import os
from rich import print

print(os.getenv("HELLO", "value does not exist"))