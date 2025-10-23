
import argparse
import os
import importlib
from dotenv import load_dotenv
import google.generativeai as genai

# A dictionary to map function names to their modules
AVAILABLE_FUNCTIONS = {
    "get_local_time_and_date": "get_local_time",
    "get_upgradable_packages": "get_upgradable_packages",
    "get_geolocation": "get_geolocation",
}

def call_function(function_name, *args):
    """
    Dynamically calls a function from a module.
    """
    if function_name in AVAILABLE_FUNCTIONS:
        module_name = AVAILABLE_FUNCTIONS[function_name]
        try:
            module = importlib.import_module(module_name)
            function = getattr(module, function_name)
            return function(*args)
        except ImportError:
            return f"Error: Could not import module {module_name}."
        except AttributeError:
            return f"Error: Function {function_name} not found in module {module_name}."
    else:
        return f"Error: Function {function_name} not available."

def main():
    """
    Main function for the agent.
    """
    load_dotenv()
    parser = argparse.ArgumentParser(description="A CLI agent to call local functions using Gemini.")
    parser.add_argument("prompt", help="The natural language command to execute.")
    args = parser.parse_args()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file.")
        return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro-latest')

    # Create a prompt for the Gemini model
    prompt = f"You are an AI assistant that calls local functions based on user commands. The available functions are: {list(AVAILABLE_FUNCTIONS.keys())}. The user command is: '{args.prompt}'. Which function should you call? Respond with only the function name."

    response = model.generate_content(prompt)
    function_to_call = response.text.strip()

    if function_to_call in AVAILABLE_FUNCTIONS:
        result = call_function(function_to_call)
        print(result)
    else:
        print(f"Could not determine which function to call. Gemini's response: {response.text}")

if __name__ == "__main__":
    main()
