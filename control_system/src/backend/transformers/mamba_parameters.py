from dataclasses import dataclass, field

from ..dataclasses.parameter import Parameter
from ..dataclasses.parameter_group import ParameterGroup


@dataclass
class MambaModelParameters(ParameterGroup):
    """
    Parameters for the Mamba model

    Attributes:
        d_model: Dimensionality of the model's hidden states
        n_layer: Number of layers in the model
        vocab_size: Size of the model's vocabulary
        rms_norm: Whether to use root mean square layer normalization
        residual_in_fp32: Whether to perform residual connections in full
            precision
        fused_add_norm: Whether to fuse addition and normalization
        pad_vocab_size_multiple: Pads the vocabulary size to a multiple of
        this value
    """

    group_name: str = "Mamba"
    group_type: str = "Model"
    description: str = "Parameters for loading Mamba models."

    model_path: Parameter = field(
            default_factory=lambda: Parameter(
                    key="model_path",
                    default_value='path/to/model',
                    description="Path to the model file"
            )
    )

    chat_format: Parameter = field(
            default_factory=lambda: Parameter(
                    key="chat_format",
                    default_value='chatml',
                    description="Chat format."
            )
    )

    device: Parameter = field(
            default_factory=lambda: Parameter(
                    key="device",
                    default_value="cuda",
                    description="Device to use for inference"
            )
    )

    d_model: Parameter = field(
            default_factory=lambda: Parameter(
                    key="d_model",
                    default_value=2560,
                    description="Dimensionality of the model's hidden states"
            )
    )

    n_layer: Parameter = field(
            default_factory=lambda: Parameter(
                    key="n_layer",
                    default_value=64,
                    description="Number of layers in the model"
            )
    )

    vocab_size: Parameter = field(
            default_factory=lambda: Parameter(
                    key="vocab_size",
                    default_value=50277,
                    description="Size of the model's vocabulary"
            )
    )

    rms_norm: Parameter = field(
            default_factory=lambda: Parameter(
                    key="rms_norm",
                    default_value=True,
                    description="Whether to use root mean square layer normalization"
            )
    )

    residual_in_fp32: Parameter = field(
            default_factory=lambda: Parameter(
                    key="residual_in_fp32",
                    default_value=True,
                    description="Whether to perform residual connections in full "
                                "precision"
            )
    )

    fused_add_norm: Parameter = field(
            default_factory=lambda: Parameter(
                    key="fused_add_norm",
                    default_value=True,
                    description="Whether to fuse addition and normalization"
            )
    )

    pad_vocab_size_multiple: Parameter = field(
            default_factory=lambda: Parameter(
                    key="pad_vocab_size_multiple",
                    default_value=8,
                    description="Pads the vocabulary size to a multiple of this value"
            )
    )


@dataclass
class MambaGenerationParameters(ParameterGroup):

    group_name: str = "Mamba"
    group_type: str = "Generation"
    description: str = "Parameters for transformers generation."

    max_length: Parameter = field(
            default_factory=lambda: Parameter(
                    key="max_length",
                    default_value=2048,
                    description="Maximum length of the generated text sequence."
            )
    )

    temperature: Parameter = field(
            default_factory=lambda: Parameter(
                    key="temperature",
                    default_value=1.0,
                    description="Controls randomness of generation (higher = more "
                                "random)."
            )
    )

    top_k: Parameter = field(
            default_factory=lambda: Parameter(
                    key="top_k",
                    default_value=None,
                    description="Number of highest probability tokens to consider at "
                                "each step (choose one of top_k or top_p)."
            )
    )

    top_p: Parameter = field(
            default_factory=lambda: Parameter(
                    key="top_p",
                    default_value=None,
                    description="Nucleus sampling probability (choose one of top_k "
                                "or top_p)."
            )
    )

    repetition_penalty: Parameter = field(
            default_factory=lambda: Parameter(
                    key="repetition_penalty",
                    default_value=1.0,
                    description="Penalty for repeating tokens."
            )
    )

    bos_token_id: Parameter = field(
            default_factory=lambda: Parameter(
                    key="bos_token_id",
                    default_value=None,
                    description="Token ID for the beginning-of-sequence marker."
            )
    )

    pad_token_id: Parameter = field(
            default_factory=lambda: Parameter(
                    key="pad_token_id",
                    default_value=None,
                    description="Token ID for padding."
            )
    )

    eos_token_id: Parameter = field(
            default_factory=lambda: Parameter(
                    key="eos_token_id",
                    default_value=None,
                    description="Token ID for the end-of-sequence marker."
            )
    )

    length_penalty: Parameter = field(
            default_factory=lambda: Parameter(
                    key="length_penalty",
                    default_value=None,
                    description="Penalty for longer sequences."
            )
    )

    no_repeat_ngram_size: Parameter = field(
            default_factory=lambda: Parameter(
                    key="no_repeat_ngram_size",
                    default_value=None,
                    description="Size of n-gram used for preventing repetition."
            )
    )

    bad_words_ids: Parameter = field(
            default_factory=lambda: Parameter(
                    key="bad_words_ids",
                    default_value=None,
                    description="List of token IDs to avoid during generation."
            )
    )

    num_return_sequences: Parameter = field(
            default_factory=lambda: Parameter(
                    key="num_return_sequences",
                    default_value=1,
                    description="Number of different sequences to generate."
            )
    )

    attention_mask: Parameter = field(
            default_factory=lambda: Parameter(
                    key="attention_mask",
                    default_value=None,
                    description="Attention mask for the input tokens."
            )
    )

    model_kwargs: Parameter = field(
            default_factory=lambda: Parameter(
                    key="model_kwargs",
                    default_value=None,
                    description="Additional keyword arguments passed to the model."
            )
    )
