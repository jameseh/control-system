from typing import Any, Dict, List

from dataclasses import dataclass
from .parameter import Parameter


@dataclass
class ParameterGroup:
    """
    This class represents a parameter group.

    Methods:
        update_parameter: Updates the value of a parameter.
        get_parameters: Returns a dictionary of parameters.
    """

    group_name = str
    group_type: str
    description: str

    def update_parameter(
            self,
            parameter_name: str,
            parameter_value: Any
            ):
        """
        Updates the value of a parameter.

        Args:
            parameter_name: The name of the parameter to update.
            parameter_value: The new value of the parameter.
        """

        if hasattr(self, parameter_name):
            parameter = getattr(self, parameter_name)
            if isinstance(parameter, Parameter):
                parameter.update_value(parameter_value)
            else:
                raise ValueError(
                        f'{parameter_name} is not a Parameter object.'
                )
        else:
            raise ValueError(f'Parameter {parameter_name} does not exist.')

    def get_parameter_fields(
            self,
            *properties: str
            ) -> List[Dict[str, Any]]:
        """
        Returns a dictionary of parameter properties.

        Args:
            properties: A list of properties to return.

        Returns:
            A dictionary of parameters.
        """

        result_list = []
        for param_name, field in self.__dataclass_fields__.items():
            if param_name not in ["group_name", "group_type", "description"]:
                parameter = getattr(self, param_name)

                if not properties:  # If properties is empty, return only field
                    result_list.append({param_name: parameter})
                else:
                    parameter_properties = parameter.get_properties(
                            *properties
                    )
                    result_list.append(
                            {
                                    **parameter_properties
                                    # Unpack nested properties
                            }
                    )

        return result_list
