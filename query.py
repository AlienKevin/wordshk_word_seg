import openai
from tqdm import tqdm

openai.api_key_path = "openai_api_key.txt"


def query(sentence: str) -> str:
    prompt = "Tokenize this Cantonese sentence into words separated by slashes and output nothing else:\n" + sentence

    response = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=[
            {"role": "user", "content": prompt},
        ],
    temperature=0,
    )

    return response.choices[0].message.content

with open("sentences.txt", "r") as f, open("tokenized_sentences.txt", "w+") as output:
    for line in tqdm(f.readlines()):
        output.write(query(line.strip()) + "\n")
        output.flush()
