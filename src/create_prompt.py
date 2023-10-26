"""
Script: OpenAI API Prompt Creater

Purpose:
    This script is designed as part of a Proof of Concept (POC) pilot project that aims
    to tailor resumes and cover letters for specific companies and job openings using
    the OpenAI API. 

    The primary function of this script is to take user input, such as specifics regarding 
    the job opening and company, and create a single coherent prompt that can then be used
    as input in an API call to OpenAI. 

Usage:
    The script is run interactively, in that it prompts the user for a string input.
    Upon receiving the input, it processes the string and combines it into a single prompt.
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# User input questions
user_input_questions = {
    "career": "What is your current profession or career field? ",
    "yrs_experience": "How many years of professional experience do you have? ",
    "job_posting_title": "What is the job position title you are interested in applying for? ",
    "job_description": "Please paste the entire job description into the terminal: ",
    "about_page": "Please paste the entire about page into the terminal: ",
    "resume": "Please paste your entire resume into the terminal: ",
    "eg_output": "Please paste an output example into the terminal: " # for calculating tokens
    }
# ChatGPT prompts
prompts = [
'''I have {yrs_experience} years of {career} experience from various projects and recently found a {job_posting_title} job posting on LinkedIn.
Your task:
    1. Review the job description, company's about page, and my resume.
    2. Craft a 1-page cover letter for the application, utilizing the provided texts.
    3. Tailor my resume to align more closely with the company and position, leveraging my experience and strengths.
    4. Return the data in a JSON format with keys "cover_leter" and  "resume", each with values of one string that contains the outputs of steps 2 and 3.
Shall we begin?
The following is the job posting:\n{job_description}
The following is the company's about page:\n{about_page}
The following is my current resume:\n{resume}\n
Complete now the above tasks 1-4.
{eg_output}'''
]

def get_user_inputs(questions_dict):
    """Prompt the user for input based on questions provided in a dictionary.
    Allows multiline inputs and doesn't accept empty inputs.
    
    Params:
        questions_dict (dict): Keys are variable names and values are questions.
    Returns:
        user_answers (dict): Keys are variable names and values are user inputs.
    """
    user_answers = {}

    for variable, question in questions_dict.items():
        print(question)
        print("     Enter 'END' on a new line when you are finished:")

        while True:
            user_input = ""
            while True:
                line = input()
                if line.strip().upper() == 'END':  # Using 'END' as a signal to finish the input
                    break
                user_input += line + "\n"

            user_input = user_input.strip()

            if user_input:  # Check if the input is non-empty
                user_answers[variable] = user_input
                break  # Exit the loop if a valid input is received
            print("Input cannot be empty. Please enter a valid response.")

    return user_answers

def remove_empty_lines(input_str):
    """Removes empty lines from a multi-line string.
    
    Params:
        input_str (str): The input string with possible empty or whitespace-only lines.
    Returns:
        str: A string with empty and whitespace-only lines removed
    """
    return '\n'.join(line for line in input_str.split('\n') if line.strip())

def remove_stopwords(text):
    """Remove stop words and non-ASCII characters from the input text.
    
    Params:
        text (str): The input string from which stop words and non-ASCII characters will be removed.
    Returns:
        filtered_text (str): A string with stop words and non-ASCII characters removed.
    """
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    # Removing non-ASCII characters
    words = [word.encode("ascii", "ignore").decode("ascii") for word in words]

    filtered_text = " ".join(word for word in words if word.lower() not in stop_words)
    return filtered_text

def create_prompt(questions_dict, prompts_list):
    """Create prompt (input) to use with ChatGPT.

    Params:
        questions_dict (dict): key - variable name; value - question used to get user input
        prompts_list (list of str): List of templates for the prompts
    Returns:
        prompt (str): Formatted prompt including user's inputs
    """
    # Get user input
    user_answers = get_user_inputs(questions_dict)

    # Update prompt with user input
    for prompt in prompts_list:
        try:
            prompt = prompt.format(**user_answers)
        except KeyError as e:
            print(f"Error: Missing value for placeholder {{{e.args[0]}}} in the prompt.")
            return None  # or you could return a default prompt or an error prompt

        # Remove empty lines of string
        return remove_stopwords(remove_empty_lines(prompt))

def main():
    """Function used to obtain finalized prompt in testing"""
    print("\n\nFinal Prompt:\n", create_prompt(user_input_questions, prompts))


if __name__== "__main__":
    main()
