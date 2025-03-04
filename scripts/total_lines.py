import typing
import pathlib

def count_lines(project_root: str | pathlib.Path) -> int:
    if isinstance(project_root, str):
        project_root = pathlib.Path(project_root)
    lines = 0
    for entry in project_root.iterdir():
        if entry.is_dir() and (
            entry.name == ".git" or
            entry.name == ".idea" or
            entry.name == ".vscode" or
            entry.name == "__pycache__" or
            entry.name == "venv" or
            entry.name == "logs"):
            pass
        if entry.is_dir():
            lines += count_lines(entry)
        try:
            with open(entry, "r") as f:
                lines += len(f.readlines())
        except Exception as e:
            print(e)
    return lines


if __name__ == "__main__":
    print(count_lines(pathlib.Path("./")))
