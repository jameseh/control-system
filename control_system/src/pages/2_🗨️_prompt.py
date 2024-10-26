import streamlit as st

from ..chat_interface import ChatInterface


class PromptPage(ChatInterface):
    """
    Encapsulates the prompt page within the chat interface, providing
    functionalities for managing and
    interacting with prompts.

    Attributes:
        page_title (str): The title displayed for the page.
        prompt_handler (PromptHandler): An object responsible for handling
        prompt-related actions.

    Methods:
        prompts_component(self) -> None:
            Constructs and renders the UI components for managing prompts.

        _widget_model(self, parameter_name: str, parameter_value: Any) ->
        st.container:
            Creates a widget for a model parameter, handling user input and
            updates.
    """

    def __init__(
            self
            ):
        super().__init__()
        self.page_title = "Prompt Configuration"
        self.page_icon = "🕵"
        st.set_page_config(
                page_title=self.page_title,
                page_icon=self.page_icon,
                layout=self.layout,
                initial_sidebar_state=self.initial_sidebar_state,
                menu_items=self.menu_items
        )

        self.prompts_component()

    def prompts_component(
            self
            ):
        """
        Prompts Widget Components
        """

        st.header("🕵️‍♂️ Prompt Configuration", divider=True)
        st.container(height=64, border=False)

        prompts_keys = [
                "system_prompt",
                "tool_prompt",
                "agent_prompt"]

        _, col1, _, col2, _, col3, _ = st.columns(
                [1, 16, 1, 16, 1, 16, 1],
                gap="large"
        )
        columns = [col1, col2, col3]
        column_index = 0

        for key in prompts_keys:
            with columns[column_index]:
                title = key.replace("_", " ").title()
                st.subheader(f"💡 {title}", divider=True)
                st.container(height=24, border=False)
                self._widget_model(key)
                column_index += 1

    def _widget_model(
            self,
            key
            ):
        """
        Widget Model

        Args:
            key (str): Prompt Key
        """

        st.text_area(
                label=key,
                value=getattr(self.prompt_handler, key),
                height=196,
                label_visibility="collapsed",
                key=key,
                on_change=self.update_parameter,
                args=(key,)
        )


if __name__ == "__main__":
    prompt_page = PromptPage()
