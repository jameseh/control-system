class PromptHandler:
    """
    Handles the formatting of the prompt.
    """

    def __init__(
            self,
            system_prompt=None,
            tool_prompt=None,
            agent_prompt=None,
            conversation_history=None,
            available_tools=None
    ):
        self.system_prompt = system_prompt
        self.tool_prompt = tool_prompt
        self.agent_prompt = agent_prompt
        self.conversation_history = conversation_history or []
        self.available_tools = available_tools or []

    @staticmethod
    def _format_context_messages(
            context_messages
            ):
        """
        Formats the context messages.

        Args:
            context_messages (list): The context messages to format.

        Returns:
            str: The formatted context messages.
        """
        formatted_messages = "\n".join(
                f"{role}: {content}" for message in context_messages
                for role, content in message.items()
        )
        return formatted_messages

    def _get_recent_messages(
            self,
            num_messages=5
            ):
        """
        Gets the most recent messages from the conversation history.

        Args:
            num_messages (int): The number of messages to get.

        Returns:
            list: The most recent messages.
        """
        return self.conversation_history[-num_messages:]

    def _format_prompt(
            self,
            prompt
            ):
        """
        Formats the prompt for the agent.

        Args:
            prompt (str): The prompt to format.

        Returns:
            str: The formatted prompt.
        """
        context_string = self._format_context_messages(
                self._get_recent_messages()
        )
        formatted_prompt = (f"{self.system_prompt}\n\n{context_string}\n\n"
                            f"{prompt}\n\n{self.tool_prompt}\n\n"
                            f"{self.agent_prompt}")
        tools_string = "\n".join(self.available_tools)
        if tools_string:
            formatted_prompt += f"\n\nAvailable Tools:\n{tools_string}"
        return formatted_prompt
