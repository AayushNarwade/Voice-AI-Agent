import ollama
import json
import os



def load_prompt():
    # Go to project root (3 levels up)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    prompt_path = os.path.join(base_dir, "prompts", "intent_prompt.txt")

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()



def extract_json(response):
    start = response.find("{")
    end = response.rfind("}") + 1

    if start == -1 or end == -1:
        raise ValueError("No JSON found")

    return response[start:end]



def process_with_llm(user_text):

    prompt_template = load_prompt()
    final_prompt = prompt_template.replace("{text}", user_text)


    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": final_prompt}]
    )

    raw_output = response["message"]["content"]

    try:
        json_str = extract_json(raw_output)
        parsed = json.loads(json_str)

        return {
            "intent": parsed.get("intent"),
            "file_name": parsed.get("file_name"),
            "content": parsed.get("content")
        }

    except Exception as e:
        return {"error": f"Invalid JSON from LLM: {str(e)}"}