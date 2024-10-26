import functools

import llama_cpp


class LlamaCPPBackend():

    def __init__(
            self
            ):
        """
           Initializes the backend.
        """
        self.model = None

    @staticmethod
    def replace_enums(
            func
            ):
        """
        Decorator to replace enum names with values in function arguments.

        Args:
            func: The function to decorate.

        Returns:
            The decorated function.
        """

        @functools.wraps(func)
        def wrapper(
                *args,
                **kwargs
                ):
            """
            A decorator that replaces enum names with values in function
            arguments.

            Args:
                func: The function to decorate.

            Returns:
                The decorated function.
            """

            # Replace enums in kwargs
            LlamaCPPBackend._replace_enums_in_dict(kwargs)

            # Replace enums in args if they are dict
            args = list(args)
            for i, arg in enumerate(args):
                if isinstance(arg, dict):
                    LlamaCPPBackend._replace_enums_in_dict(arg)
                    args[i] = arg

            return func(*tuple(args), **kwargs)

        return wrapper

    @classmethod
    def _replace_enums_in_dict(
            cls,
            dictionary
            ):
        """
        Replaces enum names with values in a dictionary.

        Args:
            dictionary: The dictionary to replace enums in.

        Returns:
            The dictionary with replaced enums.
        """

        for key, value in dictionary.items():
            if isinstance(value, str) and value.startswith("LLAMA_"):
                try:
                    dictionary[key] = getattr(llama_cpp, value)
                except AttributeError:
                    print(f"Invalid enum name: {value}")

    def load_model(
            self,
            model_parameters
            ):
        """
           Loads the model.

           Args:
               model_parameters: The parameters for the model.
        """
        self.model = llama_cpp.Llama(**model_parameters)

    @replace_enums
    def generate_completion(
            self,
            messages: list[str],
            generation_parameters: dict
    ):
        """
           Generates a response from the model.

           Args:
               list[str]: The list of messages
               generation_parameters: The parameters for the generation.

           Returns:
               str: The response from the model.
        """

        data = self.model.create_completion(messages, **generation_parameters)
        return data["choices"][0]["text"]
