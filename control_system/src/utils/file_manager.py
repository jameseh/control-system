import json
from pathlib import Path
from typing import Any, List

from .logger import Logger


logger = Logger(__name__)


class FileManager:
    """
    A class for file system operations.

    Methods:
      create_directory(self, directory_path):
          Creates a directory at the specified path.

      load_json(self, file_path):
          Loads data from a JSON file at the specified path.

      save_json(self, data, file_path):
          Saves data to a JSON file at the specified path.

      delete_file(self, file_path):
          Deletes the file at the specified path.

      file_exists(self, file_path):
          Checks if the file exists at the specified path.

      list_files(self):
          Lists all files in the base directory.
    """

    def __enter__(
            self
            ) -> 'FileManager':
        """
        Enter the runtime context for the FileManager object.

        Returns:
            FileManager: The FileManager instance.
        """
        return self

    def __exit__(
            self,
            exc_type,
            exc_value,
            traceback
            ) -> None:
        """
        Exit the runtime context for the FileManager object.

        """
        pass

    @staticmethod
    def create_directory(
            base_dir: str
            ):
        """
        Create a directory.

        Args:
            base_dir (str): The base directory for file operations.
            directory already exists. Defaults to
            False.

        """

        try:
            Path(base_dir).mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            logger.log("INFO", f"Directory already exists: {base_dir}")
        except OSError as e:
            logger.log("INFO", f"Error creating directory: {e}")

    @staticmethod
    def load_json(
            base_dir: str,
            filename: str
            ) -> Any:
        """
        Load a JSON file.

        Args:
            base_dir (str): The base directory for file operations.
            filename (str): The name of the file to load.

        Returns:
            Any: The data from the JSON file, or an empty list if the file
            does not exist.
        """
        path = Path(base_dir) / filename
        if path.exists():
            with open(path, 'r') as file:
                return json.load(file)
        else:
            return []

    @staticmethod
    def save_json(
            base_dir: str,
            filename: str,
            data: Any
            ) -> None:
        """
        Save data to a JSON file.

        Args:
            base_dir (str): The base directory for file operations.
            filename (str): The name of the file to save to.
            data (Any): The data to save.
        """
        path = Path(base_dir) / filename
        with open(path, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def delete_file(
            base_dir: str,
            filename: str
            ) -> None:
        """
        Delete a file.

        Args:
            base_dir (str): The base directory for file operations.
            filename (str): The name of the file to delete.
        """
        path = Path(base_dir) / filename
        if path.exists():
            path.unlink()

    @staticmethod
    def file_exists(
            base_dir: str,
            filename: str
            ) -> bool:
        """
        Check if a file exists.

        Args:
            base_dir (str): The base directory for file operations.
            filename (str): The name of the file to check.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return (Path(base_dir) / filename).exists()

    @staticmethod
    def list_files(
            base_dir: str
            ) -> List[str]:
        """
        List all files in the base directory.

        Args:
            base_dir (str): The base directory for file operations.

        Returns:
            List[str]: A list of all files in the base directory.
        """
        return [str(file) for file in Path(base_dir).glob('*')]
