from dataclasses import dataclass, field

from ..dataclasses.parameter import Parameter
from ..dataclasses.parameter_group import ParameterGroup


@dataclass
class LlamaCPPModelParameters(ParameterGroup):
    """
    A class to encapsulate all the parameters for Llama.CPP model loading.

    Attributes:
        model_path (Parameter):  Path to the model file
        n_gpu_layers (Parameter):  Number of layers to offload to GPU (-1 for all layers)
        split_mode (Parameter):  How to split the model across GPUs. See llama_cpp.LLAMA_SPLIT_* for options.
        main_gpu (Parameter):  Main GPU for model or small tensors (depends on split_mode)
        tensor_split (Parameter): Optional How split tensors should be distributed across GPUs. If None, the model is not split.
        vocab_only (Parameter):  Load only vocabulary, not weights
        use_mmap (Parameter):  Use memory-mapped files if possible
        use_mlock (Parameter):  Force system to keep model in RAM
        kv_overrides (Parameter): Optional Key-value overrides for model settings
        seed (Parameter):  RNG seed, -1 for random
        n_ctx (Parameter):  Text context length (0 = from model)
        n_batch (Parameter):  Maximum batch size for prompt processing
        n_threads (Parameter): Optional Number of threads for generation
        n_threads_batch (Parameter): Optional Number of threads for batch processing
        rope_scaling_type (Parameter):  RoPE scaling type, from enum llama_rope_scaling_type`. See https://github.com/ggerganov/llama.cpp/pull/2054 for details
        rope_freq_base (Parameter):  RoPE base frequency (0 = from model)
        rope_freq_scale (Parameter):  RoPE frequency scaling factor (0 = from model)
        yarn_ext_factor (Parameter):  YaRN extrapolation mix factor (negative = from model)
        yarn_attn_factor (Parameter):  YaRN magnitude scaling factor
        yarn_beta_fast (Parameter):  YaRN low correction dim
        yarn_beta_slow (Parameter):  YaRN high correction dim
        yarn_orig_ctx (Parameter):  YaRN original context size
        logits_all (Parameter):  Return logits for all tokens (not just last)
        embedding (Parameter):  Embedding mode only
        offload_kqv (Parameter):  Offload K, Q, V to GPU
        last_n_tokens_size (Parameter):  Maximum tokens in last_n_tokens deque
        lora_base (Parameter): Optional path to base model for LoRA
        lora_path (Parameter): Optional Path to LoRA file to apply to model
        numa (Parameter):  Enable NUMA support. (NOTE: Initial value is used for the remainder of the program)
        chat_format (Parameter):  Chat format for create_chat_completion
        chat_handler (Parameter): Optional chat handler for create_chat_completion
        verbose (Parameter):  Print verbose output to stderr
    """

    group_name: str = 'Llama.CPP'
    group_type: str = 'Model'
    description: str = "Llama.CPP model loading parameters"

    model_path: Parameter = field(
            default_factory=lambda: Parameter(
                    key="model_path",
                    default_value='path/to/model',
                    description="Path to the model file"
            )
    )

    n_gpu_layers: Parameter = field(
            default_factory=lambda: Parameter(
                    key="n_gpu_layers",
                    default_value=0,
                    description="Number of layers to offload to GPU "
                                + "(-1 for all layers)"
            )
    )

    split_mode: Parameter = field(
            default_factory=lambda: Parameter(
                    key="split_mode",
                    default_value='LLAMA_SPLIT_LAYER',
                    description="How to split the model across GPUs. "
                                + "See llama_cpp.LLAMA_SPLIT_* for options."
            )
    )

    main_gpu: Parameter = field(
            default_factory=lambda: Parameter(
                    key="main_gpu",
                    default_value=0,
                    description="Main GPU for model or small tensors "
                                + "(depends on split_mode)"
            )
    )

    tensor_split: Parameter = field(
            default_factory=lambda: Parameter(
                    key="tensor_split",
                    default_value=None,
                    description="How split tensors should be distributed across GPUs. "
                                + "If None, the model is not split."
            )
    )

    vocab_only: Parameter = field(
            default_factory=lambda: Parameter(
                    key="vocab_only",
                    default_value=False,
                    description="Load only vocabulary, not weights"
            )
    )

    use_mmap: Parameter = field(
            default_factory=lambda: Parameter(
                    key="use_mmap",
                    default_value=True,
                    description="Use memory-mapped files if possible"
            )
    )

    use_mlock: Parameter = field(
            default_factory=lambda: Parameter(
                    key="use_mlock",
                    default_value=False,
                    description="Force system to keep model in RAM"
            )
    )

    kv_overrides: Parameter = field(
            default_factory=lambda: Parameter(
                    key="kv_overrides",
                    default_value=None,
                    description="Key-value overrides for model settings"
            )
    )

    seed: Parameter = field(
            default_factory=lambda: Parameter(
                    key="seed",
                    default_value='LLAMA_DEFAULT_SEED',
                    description="RNG seed, -1 for random"
            )
    )

    n_ctx: Parameter = field(
            default_factory=lambda: Parameter(
                    key="n_ctx",
                    default_value=512,
                    description="Text context length (0 = from model)"
            )
    )

    n_batch: Parameter = field(
            default_factory=lambda: Parameter(
                    key="n_batch",
                    default_value=512,
                    description="Maximum batch size for prompt processing"
            )
    )

    n_threads: Parameter = field(
            default_factory=lambda: Parameter(
                    key="n_threads",
                    default_value=None,
                    description="Number of threads for generation"
            )
    )

    n_threads_batch: Parameter = field(
            default_factory=lambda: Parameter(
                    key="n_threads_batch",
                    default_value=None,
                    description="Number of threads for batch processing"
            )
    )

    rope_scaling_type: Parameter = field(
            default_factory=lambda: Parameter(
                    key="rope_scaling_type",
                    default_value='LLAMA_ROPE_SCALING_UNSPECIFIED',
                    description="RoPE scaling type, from `enum "
                                "llama_rope_scaling_type`. See "
                                "https://github.com/ggerganov/llama.cpp/pull/2054 "
                                "for details"
            )
    )

    rope_freq_base: Parameter = field(
            default_factory=lambda: Parameter(
                    key="rope_freq_base",
                    default_value=0.0,
                    description="RoPE base frequency (0 = from model)"
            )
    )

    rope_freq_scale: Parameter = field(
            default_factory=lambda: Parameter(
                    key="rope_freq_scale",
                    default_value=0.0,
                    description="RoPE frequency scaling factor (0 = from model)"
            )
    )

    yarn_ext_factor: Parameter = field(
            default_factory=lambda: Parameter(
                    key="yarn_ext_factor",
                    default_value=-1.0,
                    description="YaRN extrapolation mix factor 0 (negative = from "
                                "model)"
            )
    )

    yarn_attn_factor: Parameter = field(
            default_factory=lambda: Parameter(
                    key="yarn_attn_factor",
                    default_value=1.0,
                    description="YaRN magnitude scaling factor"
            )
    )

    yarn_beta_fast: Parameter = field(
            default_factory=lambda: Parameter(
                    key="yarn_beta_fast",
                    default_value=32.0,
                    description="YaRN low correction dim"
            )
    )

    yarn_beta_slow: Parameter = field(
            default_factory=lambda: Parameter(
                    key="yarn_beta_slow",
                    default_value=1.0,
                    description="YaRN high correction dim"
            )
    )

    yarn_orig_ctx: Parameter = field(
            default_factory=lambda: Parameter(
                    key="yarn_orig_ctx",
                    default_value=0,
                    description="YaRN original context size"
            )
    )

    logits_all: Parameter = field(
            default_factory=lambda: Parameter(
                    key="logits_all",
                    default_value=False,
                    description="Return logits for all tokens (not just last)"
            )
    )

    embedding: Parameter = field(
            default_factory=lambda: Parameter(
                    key="embedding",
                    default_value=False,
                    description="Embedding mode only"
            )
    )

    offload_kqv: Parameter = field(
            default_factory=lambda: Parameter(
                    key="offload_kqv",
                    default_value=True,
                    description="Offload K, Q, V to GPU"
            )
    )

    last_n_tokens_size: Parameter = field(
            default_factory=lambda: Parameter(
                    key="last_n_tokens_size",
                    default_value=64,
                    description="Maximum tokens in last_n_tokens deque"
            )
    )

    lora_base: Parameter = field(
            default_factory=lambda: Parameter(
                    key="lora_base",
                    default_value=None,
                    description="Optional path to base model for LoRA"
            )
    )

    lora_path: Parameter = field(
            default_factory=lambda: Parameter(
                    key="lora_path",
                    default_value=None,
                    description="Path to LoRA file to apply to model"
            )
    )

    numa: Parameter = field(
            default_factory=lambda: Parameter(
                    key="numa",
                    default_value=False,
                    description="Enable NUMA support. (NOTE: Initial value is used "
                                "for the remainder of the program)"
            )
    )

    chat_format: Parameter = field(
            default_factory=lambda: Parameter(
                    key="chat_format",
                    default_value='llama-2',
                    description="Chat format for create_chat_completion"
            )
    )

    chat_handler: Parameter = field(
            default_factory=lambda: Parameter(
                    key="chat_handler",
                    default_value=None,
                    description="Optional chat handler for create_chat_completion"
            )
    )

    verbose: Parameter = field(
            default_factory=lambda: Parameter(
                    key="verbose",
                    default_value=True,
                    description="Print verbose output to stderr"
            )
    )


@dataclass
class LlamaCPPCompletionParameters(ParameterGroup):
    """
    A class that encapsulates all of the parameters for Llama.CPP completions.

    Attributes:
        suffix (Parameter): Optional suffix to append to generated text
        max_tokens (Parameter):  Maximum tokens to generate (unlimited if <= 0)
        temperature (Parameter):  Controls randomness of generation (higher = more randomness)
        top_p (Parameter):  Nucleus sampling to limit vocabulary (keeps top % of most probable tokens)
        min_p (Parameter):  Minimum probability threshold for tokens
        typical_p (Parameter):  Encourages generation of typical text
        logprobs (Parameter): Optional Number of log probabilities to return
        echo (Parameter):  Whether to include prompt in generated text
        stop (Parameter):  List of strings to stop generation when encountered
        frequency_penalty (Parameter):  Penalty for token frequency in prompt
        presence_penalty (Parameter):  Penalty for token presence in prompt
        repeat_penalty (Parameter):  Penalty for repeated tokens
        top_k (Parameter):  Top-K sampling to limit vocabulary (keeps top k most probable tokens)
        stream (Parameter):  Whether to generate text in streaming fashion
        seed (Parameter): Optional Random seed for reproducibility
        tfs_z (Parameter):  Tail-Free Sampling parameter
        mirostat_mode (Parameter):  Mirostat sampling mode
        mirostat_tau (Parameter):  Target cross-entropy (surprise) value
        mirostat_eta (Parameter):  Learning rate for mirostat sampling
        model (Parameter): Optional Name of the language model to use
        stopping_criteria (Parameter): Optional List of stopping criteria
        logits_processor (Parameter): Optional List of logits processors
        grammar (Parameter): Optional Grammar for constrained sampling
        logit_bias (Parameter): Optional A Logit bias to use
    """

    group_name: str = "Llama.CPP"
    group_type: str = "Completion"
    description: str = "Llama.CPP generate completion parameters"

    suffix: Parameter = field(
            default_factory=lambda: Parameter(
                    key="suffix",
                    default_value=None,
                    description="Optional suffix to append to generated text"
            )
    )

    max_tokens: Parameter = field(
            default_factory=lambda: Parameter(
                    key="max_tokens",
                    default_value=16,
                    description="Maximum tokens to generate (unlimited if <= 0)"
            )
    )

    temperature: Parameter = field(
            default_factory=lambda: Parameter(
                    key="temperature",
                    default_value=0.8,
                    description="Controls randomness of generation (higher = more "
                                "randomness)"
            )
    )

    top_p: Parameter = field(
            default_factory=lambda: Parameter(
                    key="top_p",
                    default_value=0.95,
                    description="Nucleus sampling to limit vocabulary (keeps top % "
                                "of most probable tokens)"
            )
    )

    min_p: Parameter = field(
            default_factory=lambda: Parameter(
                    key="min_p",
                    default_value=0.05,
                    description="Minimum probability threshold for tokens"
            )
    )

    typical_p: Parameter = field(
            default_factory=lambda: Parameter(
                    key="typical_p",
                    default_value=1.0,
                    description="Encourages generation of typical text"
            )
    )

    logprobs: Parameter = field(
            default_factory=lambda: Parameter(
                    key="logprobs",
                    default_value=None,
                    description="Number of log probabilities to return"
            )
    )

    echo: Parameter = field(
            default_factory=lambda: Parameter(
                    key="echo",
                    default_value=False,
                    description="Whether to include prompt in generated text"
            )
    )

    stop: Parameter = field(
            default_factory=lambda: Parameter(
                    key="stop",
                    default_value=[],
                    description="List of strings to stop generation when encountered"
            )
    )

    frequency_penalty: Parameter = field(
            default_factory=lambda: Parameter(
                    key="frequency_penalty",
                    default_value=0.0,
                    description="Penalty for token frequency in prompt"
            )
    )

    presence_penalty: Parameter = field(
            default_factory=lambda: Parameter(
                    key="presence_penalty",
                    default_value=0.0,
                    description="Penalty for token presence in prompt"
            )
    )

    repeat_penalty: Parameter = field(
            default_factory=lambda: Parameter(
                    key="repeat_penalty",
                    default_value=1.1,
                    description="Penalty for repeated tokens"
            )
    )

    top_k: Parameter = field(
            default_factory=lambda: Parameter(
                    key="top_k",
                    default_value=40,
                    description="Top-K sampling to limit vocabulary (keeps top k "
                                "most probable tokens)"
            )
    )

    stream: Parameter = field(
            default_factory=lambda: Parameter(
                    key="stream",
                    default_value=False,
                    description="Whether to generate text in streaming fashion"
            )
    )

    seed: Parameter = field(
            default_factory=lambda: Parameter(
                    key="seed",
                    default_value=None,
                    description="Random seed for reproducibility"
            )
    )

    tfs_z: Parameter = field(
            default_factory=lambda: Parameter(
                    key="tfs_z",
                    default_value=1.0,
                    description="Tail-Free Sampling parameter"
            )
    )

    mirostat_mode: Parameter = field(
            default_factory=lambda: Parameter(
                    key="mirostat_mode",
                    default_value=0,
                    description="Mirostat sampling mode"
            )
    )

    mirostat_tau: Parameter = field(
            default_factory=lambda: Parameter(
                    key="mirostat_tau",
                    default_value=5.0,
                    description="Target cross-entropy (surprise) value"
            )
    )

    mirostat_eta: Parameter = field(
            default_factory=lambda: Parameter(
                    key="mirostat_eta",
                    default_value=0.1,
                    description="Learning rate for mirostat sampling"
            )
    )

    model: Parameter = field(
            default_factory=lambda: Parameter(
                    key="model",
                    default_value=None,
                    description="Name of the language model to use"
            )
    )

    stopping_criteria: Parameter = field(
            default_factory=lambda: Parameter(
                    key="stopping_criteria",
                    default_value=None,
                    description="List of stopping criteria"
            )
    )

    logits_processor: Parameter = field(
            default_factory=lambda: Parameter(
                    key="logits_processor",
                    default_value=None,
                    description="List of logits processors"
            )
    )

    grammar: Parameter = field(
            default_factory=lambda: Parameter(
                    key="grammar",
                    default_value=None,
                    description="Grammar for constrained sampling"
            )
    )

    logit_bias: Parameter = field(
            default_factory=lambda: Parameter(
                    key="logit_bias",
                    default_value=None,
                    description="A Logit bias to use"
            )
    )
