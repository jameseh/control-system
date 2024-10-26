import uuid
from typing import Any, List

from utils.file_manager import FileManager


class ChatHandler:
    """
    A class to manage chats.
    """

    def __init__(
            self,
            save_directory: str
            ) -> None:
        """
        Initialize the chatManager with a directory for chats.

        Methods:
            load_chat: Load a chat.
            save_chat: Save a chat.
            delete_chat: Delete a chat.
            append_and_save_message: Append a message to a chat and save it.
            create_chat_id: Create a new chat ID.
            list_chats: List all chats.
            get_chat_snippet: Get a snippet of a chat.
        """

        self.save_directory = save_directory
        self._create_save_directory()

    def _create_save_directory(
            self
            ):
        with FileManager() as fm:
            fm.create_directory(self.save_directory)

    def load_chat(
            self,
            chat_id: str
            ) -> Any:
        """
        Load a chat.

        Args:
            chat_id (str): The ID of the chat to load.

        Returns:
            Any: The data from the chat.
        """
        with FileManager() as file_manager:
            return file_manager.load_json(
                    self.save_directory,
                    f"{chat_id}.json"
            )

    def save_chat(
            self,
            chat_id: str,
            messages: Any
            ) -> None:
        """
        Save a chat.

        Args:
            chat_id (str): The ID of the chat to save.
            messages (Any): The messages to save.
        """
        with FileManager() as file_manager:
            file_manager.save_json(
                    self.save_directory,
                    f"{chat_id}.json",
                    messages
            )

    def delete_chat(
            self,
            chat_id: str
            ) -> None:
        """
        Delete a chat.

        Args:
            chat_id (str): The ID of the chat to delete.
        """
        with FileManager() as file_manager:
            file_manager.delete_file(self.save_directory, f"{chat_id}.json")

    def append_and_save_message(
            self,
            chat_id: str,
            message: Any
            ) -> None:
        """
        Append a message to a chat and save it.

        Args:
            chat_id (str): The ID of the chat to append to.
            message (Any): The message to append.
        """
        messages = self.load_chat(chat_id)
        messages.append(message)
        self.save_chat(chat_id, messages)

    @staticmethod
    def create_chat_id() -> str:
        """
        Create a new chat ID.

        Returns:
            str: The new chat ID.
        """
        return str(uuid.uuid4())

    def list_chats(
            self
            ) -> List[str]:
        """
        List all chats.

        Returns:
            List[str]: A list of all chat IDs.
        """

        with FileManager() as file_manager:
            files = file_manager.list_files(self.save_directory)
        return [file.stem for file in files if file.suffix == ".json"]

    def get_chat_snippet(
            self,
            chat_id: str,
            character_length: int = 32
    ) -> str:
        """
        Get a snippet of a chat.

        Args:
            chat_id (str): The ID of the chat.
            character_length (int, optional): The maximum number of
            characters to include. Defaults to 32.

        Returns:
            str: A snippet of the chat.
        """
        messages = self.load_chat(chat_id)

        if messages:
            first_assistant_message = next(
                    (msg for msg in messages if msg['role'] == 'assistant'),
                    None
            )

            if first_assistant_message:
                return first_assistant_message['content'][:character_length]

        return ""
