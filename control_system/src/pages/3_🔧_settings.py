import streamlit as st

from ..chat_interface import ChatInterface


class SettingsPage(ChatInterface):
    """
    Encapsulates the settings page within the chat interface, providing
    functionalities for customizing
    application behavior and preferences.

    Attributes:
        page_title (str): The title displayed for the page.

    Methods:
        settings_component(self) -> None:
            Constructs and renders the UI components for managing
            application settings.

        file_explorer_trigger(self) -> None:
            Triggers the opening of a file explorer for user interaction (
            e.g., file selection).

        update_parameter(self, parameter_name: str, parameter_value: Any) ->
        None:
            Updates a specified model or generation parameter with a new value.
    """

    def __init__(
            self
            ):
        super().__init__()
        self.page_title = "Settings"
        self.page_icon = "🔧"
        st.set_page_config(
                page_title=self.page_title,
                page_icon=self.page_icon,
                layout=self.layout,
                initial_sidebar_state=self.initial_sidebar_state,
                menu_items=self.menu_items
        )

        self.settings_component()

    def settings_component(
            self
            ):
        """Settings component."""

        st.header(f"🔧  {self.page_title}", divider=True)
        st.container(height=64, border=False)

        col1, col2 = st.columns([9, 1])

        with st.container(height=24, border=False):
            with col1:
                key = "model_path_model"

                st.text_input(
                        label="Model Path or URL",
                        help="Path to model file or URL to OpenAI API compliant "
                             "endpoint, ea: \
                              \n https://platform.openai.com/docs/api-reference"
                             "/making-requests",
                        value="",
                        key=key,
                        on_change=self.update_parameter,
                        args=(key,)
                )

            with col2:
                key = "open_model_path"
                st.button(
                        label="📂  Open",
                        use_container_width=False,
                        key=key,
                        on_click=self.file_explorer_trigger,
                        args=(key,)
                )

        col1, col2 = st.columns([9, 1])
        with col1:
            key = "conversations_directory"
            st.text_input(
                    label="Conversations Directory",
                    value="conversations",
                    key=key,
                    label_visibility="collapsed",
                    on_change=self.update_parameter
            )

        with col2:
            key = "open_directory"
            st.button(
                    label="📂  Open",
                    use_container_width=False,
                    key=key,
                    on_click=self.file_explorer_trigger,
                    args=(key,)
            )


if __name__ == "__main__":
    settings_page = SettingsPage()
