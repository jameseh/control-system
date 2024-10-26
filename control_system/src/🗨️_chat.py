import asyncio

import streamlit as st

from chat_interface import ChatInterface


class Chat(ChatInterface):
    """
    Encapsulates the chat page within the application, managing chat
    functionality, UI components, and underlying logic.

    Attributes:
        messages (list[Message]): A list of chat messages, where each
            message is represented as a `Message` object.

    Properties:
        page_title (str): The title of the page.
        page_icon (str): The icon of the page.
        layout (str): The layout of the page.
        initial_sidebar_state (str): The initial state of the sidebar.
        menu_items (dict): The menu items of the page.

    Methods:
        chat_component(self) -> None:
            Constructs and renders the main chat interface component.

        chat_history_component(self) -> None:
            Constructs and renders the component for managing and displaying
            chat history.
    """

    def __init__(
            self
            ):
        """
        Initialize the chat page
        """

        super().__init__()
        st.set_page_config(
                page_title=self.page_title,
                page_icon=self.page_icon,
                layout=self.layout,
                initial_sidebar_state=self.initial_sidebar_state,
                menu_items=self.menu_items
        )

        self.chat_component()
        self.chat_history_component()

    def chat_component(
            self
            ):
        """
        Chat component
        """

        st.header(f"{self.page_icon} Chat", divider=True)
        st.container(height=48, border=False)

        # Initialize session state
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Initialize chat history based on session state
        if st.session_state.get("new_chat", False):
            self.messages = []  # Clear messages only for new chats
        else:
            # Initialize chat history from PromptHandler
            self.messages = self.prompt_handler.conversation_history

        # Display chat messages from history from PromptHandler
        for message in self.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input(placeholder="Prompt..."):
            # Display user message in chat message container
            with st.chat_message("user", avatar="🥷"):
                st.markdown(prompt)

            # Format the prompt
            formatted_prompt = self.prompt_handler.format_prompt(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant", avatar="🤖"):
                response_placeholder = st.empty()
                response = asyncio.run(
                        self.model_handler.backend.generate_response(
                                formatted_prompt
                        )
                )

                if response:
                    response_placeholder.markdown(response)
                    self.update_chat_history(prompt, response)

    def chat_history_component(
            self
            ):
        """
        chats history component
        """

        # Initialize session state
        if "sidebar_chats_to_display" not in st.session_state:
            st.session_state["sidebar_chats_to_display"] = 25

        chat_dir = self.chat_handler.list_chats()

        with st.sidebar:
            with st.expander("chats", expanded=True):
                key = "new_chat_button"
                st.button(
                        label="✨ new",
                        use_container_width=False,
                        key=key,
                        on_click=self.update_current_chat_id
                )

                col1, col2, col3 = st.columns([10, 1, 1])
                for file in chat_dir[
                            :st.session_state["sidebar_chats_to_display"]]:
                    snippet = \
                        self.chat_handler.get_chat_snippet(file)
                    with col1:
                        key = f"load_{file}"
                        st.button(
                                snippet,
                                on_click=(
                                        self.load_and_display_chat),
                                args=(file,),
                                use_container_width=True,
                                key=key
                        )

                    with col2:
                        key = f"edit_{file}"
                        st.button(
                                "✏️",
                                on_click=self.chat_handler.delete_chat,
                                args=(file,),
                                use_container_width=False,
                                key=key
                        )

                    with col3:
                        key = f"delete_{file}"
                        st.button(
                                "💣",
                                on_click=self.chat_handler.delete_chat,
                                args=(file,),
                                use_container_width=False,
                                key=key
                        )


if __name__ == "__main__":
    chat = Chat()
