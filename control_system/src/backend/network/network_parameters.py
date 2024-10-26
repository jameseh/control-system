from dataclasses import dataclass, field

from ..dataclasses.parameter import Parameter
from ..dataclasses.parameter_group import ParameterGroup


@dataclass
class NetworkModelParameters(ParameterGroup):

    group_name: str = "Network"
    group_type: str = "Model"
    description: str = "Network model parameters for OpenAI API Compliant endpoints."

    model_ip: Parameter = field(
            default_factory=lambda: Parameter(
                    key="model_ip",
                    default_value='http://url/to/model',
                    description="Host IP address for the model endpoint"
            )
    )

    model: Parameter = field(
            default_factory=lambda: Parameter(
                    key="model",
                    default_value="text-davinci-003",
                    description="The model identifier to use for completion."
            )
    )


@dataclass
class NetworkCompletionParameters(ParameterGroup):

    group_name: str = "Network"
    group_type: str = "Completion"
    description: str = "Network completion parameters for OpenAI API Compliant " \
                       "endpoints."

    prompt: Parameter = field(
            default_factory=lambda: Parameter(
                    key="prompt",
                    default_value="",
                    description="The text prompt to complete."
            )
    )

    temperature: Parameter = field(
            default_factory=lambda: Parameter(
                    key="temperature",
                    default_value=1.0,
                    description="Controls randomness of completions (higher = more "
                                "random)."
            )
    )

    top_k: Parameter = field(
            default_factory=lambda: Parameter(
                    key="top_k",
                    default_value=None,
                    description="Number of highest probability tokens to consider at "
                                "each step."
            )
    )

    top_p: Parameter = field(
            default_factory=lambda: Parameter(
                    key="top_p",
                    default_value=None,
                    description="Nucleus sampling probability (choose one of top_k or "
                                "top_p)."
            )
    )

    max_tokens: Parameter = field(
            default_factory=lambda: Parameter(
                    key="max_tokens",
                    default_value=1024,
                    description="Maximum number of tokens to generate."
            )
    )

    do_sample: Parameter = field(
            default_factory=lambda: Parameter(
                    key="do_sample",
                    default_value=True,
                    description="Whether to use sampling (True) or deterministic "
                                "generation (False)."
            )
    )

    repetition_penalty: Parameter = field(
            default_factory=lambda: Parameter(
                    key="repetition_penalty",
                    default_value=1.0,
                    description="Penalty for repeating tokens."
            )
    )

    stop: Parameter = field(
            default_factory=lambda: Parameter(
                    key="stop",
                    default_value=[],
                    description="Sequences indicating the end of the completion."
            )
    )

    logprobs: Parameter = field(
            default_factory=lambda: Parameter(
                    key="logprobs",
                    default_value=False,
                    description="Whether to include token log probabilities in the "
                                "response."
            )
    )

    echo: Parameter = field(
            default_factory=lambda: Parameter(
                    key="echo",
                    default_value=False,
                    description="Whether to include the prompt in the response."
            )
    )
