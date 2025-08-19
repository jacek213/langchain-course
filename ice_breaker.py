import os

if __name__ == "__main__":
    print("hello world")
    print(os.environ.get("OPENAI_API_KEY", "No API key found"))
