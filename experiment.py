from pathlib import Path

path = Path.home() / "Downloads"

for item in path.rglob("*"):
    print(item)
