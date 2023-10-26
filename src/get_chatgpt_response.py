"""This module facilitates interactions with the GPT-3 model via OpenAI's API.

It uses utilities from `create_prompt` to craft custom prompts based on user input and queries
and then obtains a response from the GPT-3 model. The response can then be saved as a JSON file.

Functions:
    get_chatgpt_response(model, prompt, temperature=0, max_tokens=3000):
        Queries the GPT-3 model and fetches a response based on the provided prompt.

    main():
        Used in testing.

Globals:
    None.

Imports:
    os: Provides a way of using operating system-dependent functionality.
    openai: The official OpenAI library.
    create_prompt: Imports functions to handle the creation of prompts based on user interactions.
    utils: Contains utility functions, including saving dictionaries as JSON files.
"""
import os
import openai as ai
from create_prompt import create_prompt, user_input_questions, prompts
from utils import save_dict_as_json

def get_chatgpt_response(model, prompt, temperature=0, max_tokens=3000):
    """Queries the GPT-3 model to fetch a response based on the provided prompt.
    Utilizes ChatCompletion endpoint of the OpenAI API to get response from specified GPT-3 model.
    
    Params:
        model (str): The identifier for the GPT-3 model to be used (e.g., 'gpt-3.5-turbo-16k').
        prompt (str): The content message to send to the model.
        temperature (float, optional): Randomness in response. Defaults to 0.
        max_tokens (int, optional): Maximum number of tokens in response. Defaults to 3000.
    Returns:
        response (dict): A dictionary containing the model's response, among other metadata.
"""
    # get GPT-3 response
    response = ai.ChatCompletion.create(
        model = model,
        messages = [{"role": "user", "content": prompt}],
        temperature = temperature,
        max_tokens = max_tokens
    )
    return response

def main():
    """Function used in testing"""
    prompt = create_prompt(user_input_questions, prompts)
    model ='gpt-3.5-turbo-16k'
    response = get_chatgpt_response(model, prompt, temperature=0.3)

    # show response - two diff methods
    #print(response['choices'][0]['message']['content'])
    #print(response.choices[0].message["content"])

    # save response as JSON file
    file_path = os.path.join(os.getcwd(), "response.json")
    save_dict_as_json(response, file_path)

if __name__ == "__main__":
    main()
