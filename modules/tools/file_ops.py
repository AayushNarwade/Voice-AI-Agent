import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

TEXT_DIR = os.path.join(BASE_DIR, "output", "text")


def create_file(file_name):

    try:
        os.makedirs(TEXT_DIR, exist_ok=True)

        file_path = os.path.join(TEXT_DIR, file_name)

        with open(file_path, "w") as f:
            pass

        return {
            "status": "success",
            "message": f"File '{file_name}' created successfully",
            "path": file_path
        }

    except Exception as e:
        return {"error": str(e)}