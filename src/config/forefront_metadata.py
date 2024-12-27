import os
import tomllib
from typing import Optional

class InfoFusionMetadata:
    def __init__(self, filepath: Optional[str] = None):
        '''
        :param filepath: path to the pyproject.toml file
        It can be None, in this case the path will be automatically detected
        by the get_pyproject_toml_path method
        '''
        self.filepath = filepath

    def get_version(self) -> str | None:
        '''
        return the version of the poetry project
        or None if the version is not found
        '''
        try:
            if not self.filepath:
                self.filepath = self.get_pyproject_toml_path()
            with open(self.filepath, "rb") as f:
                data = tomllib.load(f)
            return data.get("project", {}).get("version")
        except FileNotFoundError:
            raise FileNotFoundError(f"Unable to find {self.filepath}")
        except Exception as e:
            raise RuntimeError(f"Error reading {self.filepath}: {e}")

    def get_pyproject_toml_path(self)-> Optional[str]:
        '''
        return the path to the pyproject.toml file
        '''
        current_file_path = os.path.abspath(__file__)

        project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))
        try:
            pyproject_toml_path = os.path.join(project_root, "pyproject.toml")
        except FileNotFoundError:
            raise FileNotFoundError("Unable to find pyproject.toml")
        return pyproject_toml_path