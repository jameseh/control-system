from pathlib import PurePath

import streamlit as st

from backend.llamacpp.llamacpp_backend import LlamaCPPBackend
from backend.llamacpp.llamacpp_parameters import (
    LlamaCPPModelParameters,
    LlamaCPPCompletionParameters
)
from backend.transformers.transformers_backend import TransformerBackend
from backend.transformers.mamba_parameters import (
    MambaModelParameters,
    MambaGenerationParameters
)
from backend.model_handler import ModelHandler
from backend.network.network_backend import NetworkBackend
from backend.network.network_parameters import (
    NetworkModelParameters,
    NetworkCompletionParameters
)
from backend.parameter_handler import ParameterHandler
from chat_handler import ChatHandler
from prompt_handler import PromptHandler
from utils.file_explorer_dialog import FileExplorer as fe
from utils.file_manager import FileManager


class ChatInterface:
    """
    Encapsulates the chat interface, providing a structured framework for
    interacting with large language models (LLMs).

    Attributes:
        page_icon (str): Icon to display in the browser tab.
        page_title (str): Title of the page.
        layout (str): Layout of the page.
        initial_sidebar_state (str): Initial state of the sidebar.
        menu_items (dict): Menu items to display in the sidebar.
        chat_handler (ChatHandler): chat manager to manage chats.
        current_chat_id (str): ID of the current chat.
        messages (list): List of messages in the chat.
        prompt_handler (PromptHandler): Prompt handler to handle prompts.
        model_handler (ModelHandler): Model handler to handle models.

    Methods:
        __init__(self):
            Initialize the chat interface.
    """

    def __init__(
            self
    ):
        """
        Initialize the chat interface.
        """

        self.page_icon = "🗨️"
        self.page_title = "LangChat"
        self.layout = "wide"
        self.initial_sidebar_state = "expanded"
        self.menu_items = {
                "Get Help"    : "https://github.com/jameseh/langchat/",
                "Report a bug": "https://github.com/jameseh/langchat/issues",
                "About"       : """Simple chat interface to run local LLMs 
                using various backends or connect to remote LLMs using \
                    the OpenAI API compliant remote LLMs"""
        }

        self.appdata_directory = PurePath("appdata")
        self.chats_directory = self.appdata_directory.joinpath("chats")
        self.parameter_states_directory = self.appdata_directory.joinpath(
                "parameter_states"
        )

        self.file_manager = FileManager
        self.file_manager.create_directory(self.appdata_directory)

        self.chat_handler = ChatHandler(f"{self.appdata_directory}/chats")

        self.current_chat_id = self.chat_handler.create_chat_id()
        self.messages = None

        self.parameter_handler = ParameterHandler(
                f"{self.appdata_directory}/parameter_states"
        )

        self.model_handler = ModelHandler()
        self.prompt_handler = PromptHandler()

        self.backends = {
                "network"     : {
                        "backend"          : NetworkBackend,
                        "model_parameters" : NetworkModelParameters,
                        "generation_method": {
                                "generate_completion":
                                    NetworkCompletionParameters,
                        },
                },
                "llamacpp"    : {
                        "backend"          : LlamaCPPBackend,
                        "model_parameters" : LlamaCPPModelParameters,
                        "generation_method": {
                                "generate_completion":
                                    LlamaCPPCompletionParameters,
                        },
                },
                "transformers": {
                        "backend"          : TransformerBackend,
                        "model_parameters" : MambaModelParameters,
                        "generation_method": {
                                "generate": MambaGenerationParameters,
                        }
                },
        }
        self.set_backend(
                "llamacpp", "generate_completion"
        )

    @staticmethod
    def send_message(
            message
    ):
        """
        Trigger callback to handle message processing and response.
        ## TODO: Implement - Agent callback placeholder
        Args:
            message (str): Message to send to the LLM.
        """

        st.session_state.callback_trigger = True

    def set_appdata_directory(
            self,
            new_directory
    ):
        with self.file_manager() as fm:
            fm.create_directory(new_directory)
        self.appdata_directory = new_directory
        return self.appdata_directory

    def set_handler_directory(
            self,
            handler_var,
            handler,
            new_directory
    ):
        """
        Set the handler directory.
        """

        with self.file_manager() as fm:
            fm.create_directory(f"{self.appdata_directory}/{new_directory}")
        handler_var = handler(new_directory)
        return handler_var

    def update_chat_history(
            self,
            prompt,
            response
    ):
        """"
        Update the chat history with the prompt and response.

        Args:
            prompt (str): Prompt sent to the LLM.
            response (str): Response from the LLM.
        """

        self.messages.extend(
                [
                        {
                                "role"   : "user",
                                "content": prompt
                        },
                        {
                                "role"   : "assistant",
                                "content": response
                        }]
        )
        st.session_state.messages = self.messages

        self.chat_handler.append_and_save_message(
                self.current_chat_id,
                {
                        "role"   : "user",
                        "content": prompt
                }
        )

        self.chat_handler.append_and_save_message(
                self.current_chat_id,
                {
                        "role"   : "assistant",
                        "content": response
                }
        )

    def update_current_chat_id(
            self
    ):
        """
        Update the current chat id.
        """
        self.current_chat_id = \
            self.chat_handler.create_chat_id()
        self.messages = []
        st.session_state.messages = self.messages

    def load_and_display_chat(
            self,
            chat_id
    ):
        messages = self.chat_handler.load_chat(chat_id)
        self.messages = messages
        st.session_state.messages = messages

        for message in messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def delete_selected_chats(
            self
    ):
        """
        Delete selected chats from the chat manager
        """

        checked_items = ac.get_checked_keys()  # Get checked items from tree
        for item in checked_items:
            if item.is_file():
                self.chat_handler.delete_chat(item)
            else:
                pass

    def file_explorer_trigger(
            self,
            *args
    ):
        """
        Trigger file explorer dialog

        Args:
            *args: Arguments to pass to the file explorer dialog.
        """

        with fe() as f:
            if args[0] == "open_directory":
                path = f.directory_explorer()
                st.session_state["chat_directory"] = str(path)

            elif args[0] == "open_model_path":
                path = f.file_explorer()
                st.session_state["model_path"] = str(path)

            self.update_parameter(*args)

    def update_parameter(
            self,
            *args
    ):
        """
        Updates the instance variable dictionaries with the new value
        from session_state for the given key.

        Args:
            *args: Arguments to pass to the file explorer dialog.
        """

        key = args[0]
        new_value = st.session_state[key]

        if key.startswith("Model_"):
            self.parameter_handler.update_parameter(
                    self.parameter_handler.model_parameters,
                    key.replace("Model_", ""),
                    new_value
            )

        if key.startswith("Generation_"):
            self.parameter_handler.update_parameter(
                    self.parameter_handler.generation_parameters,
                    key.replace("Generation_", ""),
                    new_value
            )
        st.session_state["widget_changed"] = True

    @staticmethod
    def if_widget_changed():
        """
        Checks if the widget has changed.

        Returns:
            bool: True if the widget has changed, False otherwise.
        """

        if "widget_changed" in st.session_state:
            st.session_state["widget_changed"] = False
            st.rerun()
            return
        else:
            return False

    def set_backend(
            self,
            selected_type: str,
            generation_method: str
    ):
        """
        Sets up the handlers for the selected backend.

        Args:
            selected_type (str): Selected backend type (from self.backends).
            generation_method (str): Selected generation method.
        """

        # Extract model parameters, backend class, and generation method
        # name from the map
        model_params_class = self.backends[selected_type]["model_parameters"]
        backend_class = self.backends[selected_type]["backend"]
        generation_params_class = \
            self.backends[
                selected_type]["generation_method"][generation_method
            ]

        self.parameter_handler.generation_parameters = \
            generation_params_class()

        # Instantiate backend and model parameters
        self.model_handler.backend = backend_class()
        self.parameter_handler.model_parameters = model_params_class()
        self.model_handler.model_parameters = \
            self.parameter_handler.model_parameters

        # Store generation_method for future reference (if needed)
        self.model_handler.generation_method = generation_method

    @staticmethod
    def _load_css_overrides():
        return st.markdown(
                "<link href='static/styles/custom_overrides.css' "
                "rel='stylesheet'>",
                unsafe_allow_html=True
        )
