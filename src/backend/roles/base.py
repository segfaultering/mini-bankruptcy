"""
Attributes, behaviors, and tools that all of the roles should have.
"""
import base.config as cfg

from pathlib import Path

from langchain.tools import tool


@tool
def write_file(filename: str, content: str) -> Path:
    """
    Creates a file with the specified filename (the filename should include the file extension) and writes the content to the file and return the path to the file as a pathlib `Path` object.
    """
    file_path = cfg.USER_DIRS.user_data_path / filename
    file_path.touch()
    with open(file_path, "w") as file:
        file.write(content)

    return file_path






