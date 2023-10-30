"""
Script: OpenAI API Token Counter

Purpose:
    This script is designed as part of a Proof of Concept (POC) pilot project that aims
    to tailor resumes and cover letters for specific companies and job openings using
    the OpenAI API. One crucial aspect to manage while interacting with the OpenAI API
    is the number of tokens consumed during the API calls, as it directly impacts the
    cost and rate limits associated with the usage of the API.

    The primary function of this script is to take a string input, typically a prompt,
    and calculate the number of tokens that would be consumed if the string were used
    as a prompt in an API call to OpenAI. The token count is essential for estimating
    the cost and managing the usage of the OpenAI API effectively.

Usage:
    The script can be run interactively, where it will prompt the user for a string input.
    Upon receiving the input, it will process the string to determine the number of tokens
    and output the token count.

Example:
    Input: "Design a resume tailored for a software engineering position at Google."
    Output: "The input string contains X tokens."
"""
import tiktoken
from create_prompt import create_prompt, user_input_questions, prompts

def count_tokens(prompt_input, encoding):
    """
    Counts tokens in the input, which can be a string, list of strings, or list of dictionaries.

    Params:
        prompt_input (str or list or dict): The input to count tokens from.
        encoding (class): tiktoken.core.Encoding -- encoding for an OpenAI model
    Returns:
        num_tokens (int): The total count of tokens.
    """
    num_tokens = 0

    def tokenize_text(text, encoding):
        """ Tokenize a given text.
        
        Params:
            text (str): The text input to process.
            encoding (class): tiktoken.core.Encoding -- encoding for an OpenAI model
        Returns:
            (int): The number of tokens in the text.
        """
        # Tokenize the text
        tokens_int = encoding.encode(text)
        # View the corresponding token string for each integer token
        print("Token String-Integer Pairs:\n",
              [encoding.decode_single_token_bytes(token) for token in tokens_int])
        return len(tokens_int)

    # Check if prompt_input is string
    if isinstance(prompt_input, str):
        #print(f"Handled a string: {input}")        
        num_tokens += tokenize_text(prompt_input, encoding) + 3 # (+3): every reply is primed with <|start|>assistant<|message|>
        return num_tokens

    # Check if prompt_input is list
    if isinstance(prompt_input, list):
        # Check if the list contains strings
        if all(isinstance(i, str) for i in prompt_input):
            #print(f"Handled a list of strings: {input}")
            for text in prompt_input:
                num_tokens += tokenize_text(text, encoding)
            num_tokens += 3
            return num_tokens

        # Check if list contains dictionaries
        if (all(isinstance(i, dict) for i in prompt_input) and
            all(all(isinstance(val, str) for val in i.values()) for i in prompt_input)):
            #print(f"Handled a list of dictionaries of strings: {input}")

            num_tokens += 4  # (+4): every message follows <|start|>{role/name}\n{content}<|end|>\n
            for message in prompt_input:
                for key, value in message.items():
                    num_tokens += tokenize_text(prompt_input, encoding)
                num_tokens += 3
            return num_tokens

        if prompt_input is None:
            return print(prompt_input)
        return "Invalid input: List must contain either strings or dictionaries of strings."
    return "Invalid input type: Must be string, list of strings, or list of dictionaries."

def main(model_encoders):
    """
    Counts the number of tokens in a text | message to be sent to an OpenAI model using the API

    Params:
        model_encoders (list of str): List of specific OpenAI models to be used for encoding
    Returns:
        None
    """
    # Define prompt input
    prompt = create_prompt(user_input_questions, prompts)

    # Calculate tokens required by each model encoder
    for model_encoder in model_encoders:
        encoding = tiktoken.encoding_for_model(model_encoder)
        num_tokens = count_tokens(prompt, encoding)
        print(f"\n\nThis encoding takes a total of {num_tokens} tokens (model: {model_encoder})\n")
        assert encoding.decode(encoding.encode(prompt)) == prompt, "Error: failed input encoding."


if __name__ == "__main__":
    # OpenAI models available through the API
    model_encoders = ["gpt-4",                  # for gpt-4
                    "gpt-3.5-turbo",            # for gpt-3.5-turbo  
                    "text-embedding-ada-002"]   # for text-embedding-ada-002
    model_encoders = ["gpt-4"]  # shorter list for testing

    main(model_encoders)
