#def read_prompt(file_path):
    #with open(file_path, "r", encoding="utf-8") as input_file:
     #   prompt = input_file.read()
   # return prompt


#def main():
 #   prompt = read_prompt(r"C:\Users\Suvarna\OneDrive\Desktop\AI ML\text.txt")
  #  print("Prompt read from file:")
   # print(prompt)


#if __name__ == "__main__":
 #   main()

 
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq


def read_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as input_file:
        prompt = input_file.read()
    return prompt


def get_ai_response(prompt, client):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def save_response(response_text, file_path):
    output_data = {
        "response": response_text
    }

    with open(file_path, "w", encoding="utf-8") as output_file:
        json.dump(output_data, output_file, indent=4)


def main():
    project_folder = Path(__file__).parent

    load_dotenv(project_folder / ".env")

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY was not found in the .env file.")

    client = Groq(api_key=api_key)

    prompt = read_prompt(project_folder / "text.txt")

    print("Sending prompt to AI...")

    response_text = get_ai_response(prompt, client)

    save_response(response_text, project_folder / "response.json")

    print("AI response saved to response.json")


if __name__ == "__main__":
    main()
