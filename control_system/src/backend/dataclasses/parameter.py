from typing import Any, Dict

from dataclasses import dataclass, field


@dataclass
class Parameter:
    """
    A class to encapsulate a Parameter with a mutable value and immutable
    default value.

    Attributes:
        key (str): The key of the Parameter.
        default_value (Any): The default value of the Parameter.
        description (str): A description of the Parameter.
        value (Any): The value of the Parameter.

    Methods:
        __hash__ : int
            Return a hash of the Parameter.
        update_value : Any
            Set the value of the parameter.
        get_dict : dict[str, Any]
            Get a dictionary containing the specified properties of the
            parameter.
    """

    key: str
    default_value: Any
    description: str
    value: Any = field(default_factory=lambda: None)  # Mutable attribute

    def update_value(
            self,
            new_value: Any
            ):
        if not isinstance(new_value, type(self.default_value)):
            raise TypeError(
                f"Value must be of type {type(self.default_value)}"
                )
        self.value = new_value

    def get_properties(
            self,
            *properties: str
            ) -> Dict[str, Any]:
        """Returns a dictionary of specified properties of the parameters."""

        if properties:
            return {
                    prop: getattr(self, prop) for prop in properties
            }
        else:
            return {
                    field.name: getattr(self, field.name)
                    for field in self.__dataclass_fields__.values()
            }
