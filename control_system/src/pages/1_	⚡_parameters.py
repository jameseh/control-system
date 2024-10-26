from typing import Any, Dict, List

import streamlit as st
import streamlit_antd_components as sac

from chat_interface import ChatInterface


class ParametersPage(ChatInterface):

    def __init__(
            self
            ):
        """
        Initialize the parameters page.
        """

        super().__init__()
        self.page_title = "Parameters"
        self.page_icon = "	⚡"
        st.set_page_config(
                page_title=self.page_title,
                page_icon=self.page_icon,
                layout=self.layout,
                initial_sidebar_state=self.initial_sidebar_state,
                menu_items=self.menu_items
        )
        self.screen_width = self.get_screen_width()
        self.container_width = self.get_container_width()

        self._load_parameters()
        self.generate_parameters_components()
        self._load_css_overrides()

    def generate_parameters_components(
            self
            ):
        """
        Generate the parameters components.
        """

        model_parameters = \
            self.parameter_handler.get_parameter_fields(
                    self.parameter_handler.model_parameters,
                    "key", "default_value", "value", "description"
            )
        model_parameters = [
                {key: f"Model_{value}" if key == "key" else value for
                 key, value in
                 param.items()} for param in model_parameters
        ]
        generation_parameters = \
            self.parameter_handler.get_parameter_fields(
                    self.parameter_handler.generation_parameters,
                    "key", "default_value", "value", "description"
            )
        generation_parameters = [
                {key: f"Generation_{value}" if key == "key" else value for
                 key, value in param.items()} for param in
                generation_parameters
        ]

        model_tab, generation_tab = st.tabs(["Model", "Generation"])
        self.display_parameters(model_parameters, "🧬", model_tab)
        self.display_parameters(
                generation_parameters, "🧬", generation_tab
        )

    def display_parameters(
            self,
            parameters: List[Dict[str, Any]],
            title_emoji: str,
            parameter_tab: str
    ):
        """
        Displays a set of parameters with widgets in a multi-column
        layout, ensuring each column is under 200px wide.
        Args:
            parameters (dict): The parameters to display.
            title_emoji (str): The emoji to display before the title.
        """

        with parameter_tab:
            max_column_width = 296  # Set desired maximum width
            available_width = min(
                    self.container_width,
                    self.screen_width
            )
            num_columns = max(
                    1, available_width // max_column_width
            )

            columns = st.columns(num_columns, gap="large")

            for index, param in enumerate(parameters):
                column_index = index % num_columns  # Distribute widgets
                # evenly across columns
                with columns[column_index]:
                    self._widget_model(
                            param["key"],
                            param["default_value"],
                            param["value"],
                            param["description"]
                    )

    def _widget_model(
            self,
            key: str,
            default_value: Any,
            value: Any,
            description: str
    ):
        """
        Generate a widget for a model parameter.

        Args:
            key (str): The parameter key.
            default_value (any): The parameter default value.
            description (str): The parameter description.
        """

        title = f'{key.replace("_", " ").title()}'
        if isinstance(default_value, float):
            # Determine min/max values based on parameter requirements
            if key in ("yarn_beta_fast", "yarn_beta_slow"):
                min_value = 0.0
                max_value = 100.0
            else:
                min_value = 0.0
                max_value = 1.0

            with st.container():
                title = f"##{title}##" + "\n"
                description = f"{description}"

                st.markdown(f"{title}{description}", unsafe_allow_html=True)

                st.slider(
                        label=title,
                        label_visibility="collapsed",
                        value=value if value is not None else default_value,
                        min_value=min_value,
                        max_value=max_value,
                        key=key,
                        on_change=self.update_parameter,
                        args=(key,)
                )

        elif isinstance(default_value, bool):
            sac.switch(
                    label=title,
                    description=description,
                    value=value if value is not None else default_value,
                    on_label='True',
                    off_label='False',
                    align='end',
                    size='md',
                    on_color='green',
                    off_color='red',
                    key=key,
                    on_change=self.update_parameter,
                    args=(key,)
            )

        elif isinstance(default_value, int):
            st.number_input(
                    label=title,
                    help=description,
                    value=value if value is not None else default_value,
                    key=key,
                    on_change=self.update_parameter,
                    args=(key,)
            )

        elif isinstance(default_value, str):
            if key == "model_path_model":
                pass
            else:
                st.text_input(
                        label=title,
                        help=description,
                        value=value if value is not None else default_value,
                        key=key,
                        on_change=self.update_parameter,
                        args=(key,)
                )

        elif default_value is None:
            st.text_input(
                    label=title,
                    help=description,
                    value=value if value is not None else default_value,
                    key=key,
                    on_change=self.update_parameter,
                    args=(key,)
            )

    def _load_parameters(
            self
            ):
        """
        Load the parameters from the parameters file.
        """

        if self.parameter_handler.model_parameters.group_type == "Model":
            self.parameter_handler.load_parameter_group(
                    self.parameter_handler.model_parameters
            )
        else:
            self.parameter_handler.load_parameter_group(
                    self.parameter_handler.generation_parameters
            )


if __name__ == "__main__":
    parameters_page = ParametersPage()
