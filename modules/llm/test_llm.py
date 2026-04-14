from llm import process_with_llm

# text = "Create a Python file with a retry function"

text = """
Artificial Intelligence (AI) is transforming industries by enabling machines to learn from data,
make decisions, and perform tasks that typically require human intelligence. It is widely used in
healthcare, finance, education, and automation. However, challenges such as data privacy,
ethical concerns, and job displacement remain important considerations.
"""

result = process_with_llm(text)

print("OUTPUT:")
print(result)