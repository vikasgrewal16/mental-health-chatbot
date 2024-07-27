
import logging
import json
import re

def setup_logging():
    """
    Set up basic logging configuration.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file: str) -> dict:
    """
    Load a JSON configuration file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        dict: Configuration data.
    """
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        logging.error(f"Configuration file {config_file} not found.")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from the file {config_file}.")
        return {}

def handle_error(error_message: str):
    """
    Return a standardized error message.

    Args:
        error_message (str): The error message to return.

    Returns:
        dict: Error response.
    """
    logging.error(error_message)
    return {"error": error_message}

def remove_special_characters(text: str) -> str:
    """
    Remove special characters from a text.

    Args:
        text (str): The input text.

    Returns:
        str: Cleaned text.
    """
    return re.sub(r'[^\w\s]', '', text)
