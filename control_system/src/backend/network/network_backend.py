from wsgiref import headers

import httpx


class NetworkBackend:
    """
    A class used to represent a network backend.

    Methods:
        generate (staticmethod): generates a response from an LLM compliant
        completion endpoint.

    """

    async def generate(
            protocol: str,
            host_ip: str,
            port: int,
            endpoint: str,
            prompt: str,
            generation_params: dict,
            headers: dict = None
    ):
        """
        Generates a response from an LLM compliant completion endpoint.

        Args:
            protocol: (str) The protocol
            host_ip: (str) The IP address of the host.
            port: (int) The port of the host.
            endpoint: (str) The endpoint to query.
            prompt: (str) The prompt to send to the LLM.
            generation_params: (dict) The generation parameters to
               send to the LLM.
            headers: (dict) The headers to send to the endpoint.

        Returns:
            The response from the LLM.

        """

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                        f"{protocol}://{host_ip}:{port}{endpoint}",
                        json={"prompt": prompt, **generation_params},
                        headers=headers if headers else None
                )

                data = response.json()
                return data
        except Exception as e:
            return f"Error querying LLM: {str(e)}"
