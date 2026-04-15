import os

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

CODE_DIR = os.path.join(BASE_DIR, "output", "code")


def write_code(file_name, content):

    try:
        os.makedirs(CODE_DIR, exist_ok=True)

        if not file_name.endswith(".py"):
            file_name += ".py"

        file_path = os.path.join(CODE_DIR, file_name)

        with open(file_path, "w") as f:
            f.write(content)

        return {
            "status": "success",
            "message": f"Code written to '{file_name}'",
            "path": file_path
        }

    except Exception as e:
        return {"error": str(e)}