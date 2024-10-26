import pickle
from typing import Any

from .dataclasses.parameter_group import ParameterGroup


class ParameterHandler:

    def __init__(
            self,
            save_directory: str
            ):
        self.model_parameters = None
        self.generation_parameters = None

        self.save_directory = save_directory

    @staticmethod
    def format_filename(
            group: ParameterGroup
            ):
        """
        Formats the filename of the parameter group
        """
        filename = (f'{group.group_name.replace(".", "_")}-'
                    f'{group.group_type}.pickle')
        return filename

    def save_parameter_group(
            self,
            group: ParameterGroup
            ) -> None:
        filename = self.format_filename(group)

        with open(f"{self.save_directory}/{filename}", "wb") as f:
            pickle.dump(group, f)

    def load_parameter_group(
            self,
            group: ParameterGroup
            ) -> None:
        try:
            filename = self.format_filename(group)

            with open(f"{self.save_directory}/{filename}", "rb") as f:
                data = pickle.load(f)

            if data.group_type == "Model":
                self.model_parameters = data
            else:
                self.generation_parameters = data

        except FileNotFoundError:
            pass

    def update_parameter(
            self,
            group: ParameterGroup,
            key: str,
            value: Any
            ):
        if group.group_type == "Model":
            self.model_parameters.update_parameter(key, value)
        else:
            self.generation_parameters.update_parameter(key, value)

        self.save_parameter_group(group)

    def get_parameter_fields(
            self,
            group: ParameterGroup,
            *properties
    ) -> list[dict[str, Any]]:
        if group.group_type == "Model":
            return self.model_parameters.get_parameter_fields(*properties)
        else:
            return self.generation_parameters.get_parameter_fields(*properties)

    def get_parameters(
            self,
            group: ParameterGroup
            ):
        """
        Updates the group.parameters dictionary with Parameter keys and values.
        """

        parameter_dict = {}
        parameters = self.get_parameter_fields(
                group, "key", "value", "default_value"
        )

        for parameter in parameters:
            parameter_dict[parameter["key"]] = \
                parameter["value"] if parameter["value"] is not None else \
                    parameter["default_value"]

        return parameter_dict
