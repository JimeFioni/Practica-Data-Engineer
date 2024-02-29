import os
from dotenv import load_dotenv
import openai
from parse import extract_json


sample_response = """Sure, here is the information in JSON format based on the skills, tools, languages, and aptitudes necessary for the job:

```json
{
  "Skills": [
    {"name": "Property Management"},
    {"name": "Facilities Management (FM) Operations"},
    {"name": "Financial Focus"},
    {"name": "Customer Care"},
    {"name": "Facilities Coordinator Activities"}
  ],
  "Tools": [],
  "Languages": [],
  "Aptitudes": []
}
```
"""


def prompt(description:str):

    load_dotenv()
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0301",
      messages=[
        {"role": "user", "content": f'{description}'}
      ]
    )

    return completion.choices[0].message

# list_of_models = [model for model in openai.Model.list().data]
# print(list_of_models)

# print(extract_json(sample_response))

print(prompt(sample_response))





