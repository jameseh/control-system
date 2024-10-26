import asyncio


class ModelHandler:

    def __init__(
            self
    ):
        self.backend = None
        self.model = None

        self.model_parameters = None
        self.generation_parameters = None
        self.generation_method = None

        self.use_timer = False
        self.eject_time = None
        self.last_used = None
        self.eject_task = None

    async def generate(
            self,
            prompt: str
    ):
        """Generates a response using the appropriate method."""

        model_parameters = self.model_parameters.get_parameters()
        generation_parameters = self.generation_parameters.get_parameters()

        if self.backend.host_ip:  # Network backend
            return await getattr(self.backend, self.generation_method)(
                    prompt, model_parameters, generation_parameters
            )
        else:  # Local backend
            if self.model is None:
                self.backend.load_model(model_parameters)

            # Start/reset timer if using it
            if self.use_timer:
                # Get eject time from parameters
                self.eject_time = self.model.get_eject_time()
                self.last_used = asyncio.get_event_loop().time()

            response = await getattr(self.backend, self.generation_method)(
                    prompt, generation_parameters
            )

            # Schedule model ejection if timer is active
            if self.use_timer and self.eject_task is None:
                self.eject_task = asyncio.create_task(
                        self.eject_model_after_delay(self.eject_time)
                )

            return response

    def eject_model(
            self
    ):
        """
           Ejects the model.
        """

        self.model = None

    async def eject_model_after_delay(
            self,
            delay: int
    ):
        """Ejects the model after the specified delay.

        Args:
            delay: The delay in seconds.
        """
        await asyncio.sleep(delay)
        if asyncio.get_event_loop().time() - self.last_used >= delay:
            self.eject_model()
