"""
This module handles the configuration and setup for the OpenAI API.

It uses the `dotenv` package to load environment variables from a `.env` file,
specifically to fetch the 'API_KEY' for the OpenAI API.

Globals:
    ai.api_key (str): The API key used for authenticating with the OpenAI API.

Imports:
    os: Provides a way of using operating system-dependent functionality.
    dotenv: Reads key-value pairs from a .env file and can set them as environment variables.
    openai: The official OpenAI library.

Example:
    To use this configuration in another script:

        import config_module_name  # replace 'config_module_name' with this module's name
        # Now the OpenAI API key is set and can be used with OpenAI's library functions.
"""
import os
from dotenv import load_dotenv
import openai as ai

load_dotenv()

# define global variables
ai.api_key = os.getenv('API_KEY')
