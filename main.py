import os
import time
from dotenv import load_dotenv
from groq import Groq
from google import genai
from google.genai import errors

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

    print(f"Reply:\n{reply}\n")
    print(f"Input Tokens:  {input_tokens}")
    print(f"Output Tokens: {output_tokens}")
    print(f"Cost:          ${cost:.6f} (Free tier - theoretical paid cost)\n")


def call_gemini(prompt: str, retries: int = 3):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
            )
            break
        except errors.ServerError as e:
            if e.code == 503 and attempt < retries - 1:
                wait_time = 2 ** attempt
                print(f"Gemini server busy (503). Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise

    reply = response.text
    usage = response.usage_metadata
    input_tokens = usage.prompt_token_count or 0
    candidate_tokens = usage.candidates_token_count or 0
    thinking_tokens = usage.thoughts_token_count or 0
    total_output_tokens = candidate_tokens + thinking_tokens

    # Gemini 3.8 Flash pricing (through Dec 31, 2026): $0.75 / 1M input, $3.75 / 1M output
    cost = (input_tokens / 1_000_000) * 0.75 + (total_output_tokens / 1_000_000) * 3.75

    print(f"Reply:\n{reply}\n")
    print(f"Input Tokens:    {input_tokens}")
    print(f"Output Tokens:   {candidate_tokens} (plus {thinking_tokens} thinking tokens)")
    print(f"Cost:            ${cost:.6f} (Free tier - theoretical paid cost)\n")


if __name__ == "__main__":
    call_groq(PROMPT)
    call_gemini(PROMPT)
