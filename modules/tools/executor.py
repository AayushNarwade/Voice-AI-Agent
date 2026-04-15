from modules.tools.file_ops import create_file
from modules.tools.code_gen import write_code
from modules.tools.summarize import summarize_text

def execute_action(llm_output):

    intent = llm_output.get("intent")
    file_name = llm_output.get("file_name")
    content = llm_output.get("content")


    if intent == "create_file":
        if not file_name:
            return {"error": "File name missing"}
        return create_file(file_name)


    elif intent == "write_code":
        if not file_name or not content:
            return {"error": "Missing file name or content"}
        return write_code(file_name, content)


    elif intent == "summarize":
        return summarize_text(content)


    elif intent == "chat":
        return {
            "status": "success",
            "response": content
        }


    else:
        return {"error": "Unknown intent"}