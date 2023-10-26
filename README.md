#  OpenAI ChatGPT Resume & Cover Letter Pipeline

A robust integration pipeline harnessing the power of OpenAI's ChatGPT model to interactively 
handle and process queries. Designed with extensibility in mind, this project currently encapsulates
functionalities ranging from prompt creation to resume and cover letter tailoring to a specific 
job posting and company.

## Table of Contents
- [Directory Structure](#directorystructure)
- [Installation](#installation)

## Directory Structure
OPENAI_API_CV_PIPELINE/
│
├── data/                       # Example data
│   ├── eg_about_page.txt
│   ├── eg_job_description.txt
│   ├── eg_output.txt
│   ├── eg_prompt.txt
│   └── eg_resume.txt
│
├── openai_env/                 # Virtual environment
│   ├── Include/
│   ├── Lib/site-packages
│   ├── Scripts/
│   ├── share/
│   └── pyvenv.cfg
│
├── src/
│   ├── calculate_tokens.py
│   ├── connect_api.py
│   ├── create_prompt.py
│   ├── get_chatgpt_response.py
│   └── utils.py
│
├── .env                        # Global variables
├── .gitignore                  # Don't push to GitHub
├── demo_info.txt               # Outcome overview for POC
├── flag_avoidance.txt          # Avoid AI-generation detection algorithms
├── README.md 
└── requirements.txt


## Installation

```bash
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
