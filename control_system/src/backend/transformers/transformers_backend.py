import torch
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM

from ...utils.logger import Logger


logger = Logger(__name__)


class TransformerBackend:
    """
    Backend for Transformer-based language models (Mamba, GPT-like, etc).

    Attributes:
        model: The loaded Transformer model.
        tokenizer: The associated tokenizer.
    """

    def __init__(
            self
    ):
        self.model = None
        self.tokenizer = None
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model_name_or_path = None

    def load_model(
            self,
            model_parameters: dict
    ):
        """Loads the model, tokenizer, and optionally applies a  chat format.

        Args:
            model_parameters:  Dict for standard model loading requirements.

        """

        try:
            model_name = model_parameters["name_or_path"]
            self.model_name_or_path = model_name
            logger.log(
                    "INFO",
                    f"Loading model {model_name}."
            )
        except KeyError as e:
            self.model_not_loaded()

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Handle transformers architecture with this workaround until it is added
        # to the transformers library
        if "ssm_cfg" in self.model.generation_parameters:
            from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel

            self.model = MambaLMHeadModel.from_pretrained(
                    model_name, device=self.device, dtype=torch.float16
            )
        # Load the model as usual.
        else:
            self.model = AutoModelForCausalLM.from_pretrained(model_name).to(
                    self.device
            )

    def chat_format_apply_template(
            self,
            override_chat_format=None
    ):
        """
        Applies a chat format to the tokenizer.

        Args:
            override_chat_format (optional=None): chat format to apply

        """

        if override_chat_format is not None:
            self.tokenizer.chat_template = AutoTokenizer.from_pretrained(
                    override_chat_format
            ).chat_template
        else:
            self.tokenizer.chat_template = AutoTokenizer.from_pretrained(
                    self.model_name_or_path
            ).chat_template

    @chat_format_apply_template
    async def generate(
            self,
            prompt: str,
            generation_parameters: dict,
            add_generation_prompt: bool = True
    ):
        """
        Generates a response using the loaded model.

        Args:
            add_generation_prompt (bool): Whether to add the generation prompt
                to the input.
            prompt (str): The user prompt for generation.
            generation_parameters (dict): Dict of generation parameters.

        Returns:
            str:  The generated response.
        """

        if not self.model:
            self.model_not_loaded()

        input_ids = self.tokenizer.apply_chat_template(
                prompt,
                return_tensors="pt",
                add_generation_prompt=add_generation_prompt
        ).to(self.model.device)

        output = self.model.generate(input_ids, **generation_parameters)
        decoded = self.tokenizer.batch_decode(output)
        return decoded

    def get_model_config(
            self
    ):
        """Gets core attributes from the loaded model's configuration.

        Returns:
            dict:  Relevant entries from AutoConfig.to_dict()
               "summary": (Optional) Short human-readable model description
        """

        if not self.model:
            self.model_not_loaded()

        config = AutoConfig.from_pretrained(self.model.config.name_or_path)
        model_info = config.to_dict()
        return model_info

    @staticmethod
    def model_not_loaded():
        """
        Raises a ValueError if the model is not loaded.
        """

        logger.log(
                "ERROR",
                "Model not loaded. Must call 'load_model' first."
        )
        raise ValueError("Model not loaded. Must call 'load_model' first.")
