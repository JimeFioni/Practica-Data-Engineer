import re
import json
import openai
from typing import List

text_with_mixed_content = """
This is some text before JSON.
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
This is some text after JSON.
"""

def extract_json(text_with_json:str):
    json_pattern = r'\{.*\}'
	
    matches = re.search(json_pattern, text_with_mixed_content)

    if matches:
        json_str = matches.group()
        try:
            return json.loads(json_str)
        except:
            return json.loads("{}")
    else:
        return json.loads("{}")

def jsonify(data: dict | List[dict]) -> str:
    """
    Ignores serialization of dates and has nice formatting.
    """
    return json.dumps(data, indent=4, sort_keys=True, default=str)
