import random
import string
from pathlib import Path
directory = Path("D:\python5")
directory.mkdir(parents=True, exist_ok=True)
for i in range(10):
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    filename = name + ".txt"
    file_path = directory / filename
    file_path.touch()
    print(file_path.absolute())
