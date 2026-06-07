import backend.config as cfg

from pathlib import Path

from langchain.tools import tool


# Manager Agent
@tool(response_format="content_and_artifact")
def create_tasks(filename: str, file_content: str) -> Path:
    """Creates a checklist file that the manager agent stores tasks for the team to work towards."""
    file = cfg.USER_DIRS.user_data_path / "filename"
    file_path.touch()
    with open(file_path, "w") as file:
        file.write(file_content)
    
    return (f"File written to: {file_path}", 

















