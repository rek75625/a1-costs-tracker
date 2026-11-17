import os 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

PROMPT = "What is meant by Quran o Hadith"


def call_groq(prompt: str):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
    )

    reply = completion.choices[0].message.content
    input_tokens = completion.usage.prompt_tokens
    output_tokens = completion.usage.completion_tokens

    # Groq pricing for openai/gpt-oss-120b: $0.15 / 1M input, $0.60 / 1M output
    cost = (input_tokens / 1_000_000) * 0.15 + (output_tokens / 1_000_000) * 0.60

    print("=== Provider 1: Groq (openai/gpt-oss-120b) ===")
    print(f"Reply:\n{reply}\n")
    print(f"Input Tokens:  {input_tokens}")
    print(f"Output Tokens: {output_tokens}")
    print(f"Cost:          ${cost:.6f} (Free tier - theoretical paid cost)\n")


# def call_gemini(prompt: str):
#     client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=prompt,
#     )

#     reply = response.text
#     input_tokens = response.usage_metadata.prompt_token_count
#     output_tokens = response.usage_metadata.candidates_token_count

#     # Gemini 2.5 Flash pricing: $0.30 / 1M input, $2.50 / 1M output
#     cost = (input_tokens / 1_000_000) * 0.30 + (output_tokens / 1_000_000) * 2.50

#     print("=== Provider 2: Google Gemini (gemini-2.5-flash) ===")
#     print(f"Reply:\n{reply}\n")
#     print(f"Input Tokens:  {input_tokens}")
#     print(f"Output Tokens: {output_tokens}")
#     print(f"Cost:          ${cost:.6f} (Free tier - theoretical paid cost)\n")


if __name__ == "__main__":
    call_groq(PROMPT)
    # call_gemini(PROMPT)
