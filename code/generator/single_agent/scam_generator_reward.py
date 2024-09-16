import replicate
import streamlit as st
import pandas as pd
import re
from dotenv import load_dotenv
import os

load_dotenv()
replicate_api = os.getenv('REPLICATE_API_TOKEN')

# Function for generating LLaMA3 response
temperature = 0.8
top_p = 0.9
max_length = 2048
llm = "meta/meta-llama-3-70b-instruct"

def generate_llama_response():
    string_dialogue = '''Generate phone conversations with the following description:

    A phone conversation between a scammer (caller) attempting to perform reward scam such as free gift card on the receiver.
    Do not put any description other than the conversation. 
    
    # Note
    Do not put action such as (pauses) in the conversation. 
    
    Format the response as follows: 
    caller: [dialogue] 
    receiver: [dialogue]
    '''

    input = {
        "prompt": string_dialogue,
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "temperature":temperature, 
        "top_p":top_p, 
        "max_new_tokens":max_length, 
        "repetition_penalty":1
    }

    output = replicate.run(llm, input=input)

    return output

reward_scam_data = pd.DataFrame(columns=['dialogue', 'type', 'label'])

# Generate multiple responses and add them to the DataFrame
num_responses = 10
for i in range(num_responses):
    response = generate_llama_response()
    full_response = ''
    for item in response:
        full_response += item
    print(f"Response {i+1}:")
    print(full_response)
    reward_scam_data = reward_scam_data._append({'dialogue': full_response, 'type': 'reward', 'label': 1}, ignore_index=True)

# # Function to format the cell value
def format_cell(cell):
    return ' '.join(str(cell).split('\n'))

# # Apply the formatting function to each cell in the DataFrame
reward_scam_data = reward_scam_data.map(format_cell)

# # Save the DataFrame to a CSV file
reward_scam_data.to_csv('../data/reward_scam_responses_10.csv', index=False)