import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)


def merge_lists(
    unique_keys: List[str], *args: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    # Check if inputs are lists of dictionaries
    for idx, arg in enumerate(args):
        if not isinstance(arg, list) or not all(isinstance(item, dict) for item in arg):
            logging.error(f"Argument {idx+1} must be a list of dictionaries")
            raise ValueError(f"Argument {idx+1} must be a list of dictionaries")

    if not isinstance(unique_keys, list) or not all(
        isinstance(key, str) for key in unique_keys
    ):
        logging.error("unique_keys must be a list of strings")
        raise ValueError("unique_keys must be a list of strings")

    try:
        # Combine all the lists
        combined_lists = [item for lst in args for item in lst]
    except TypeError as e:
        logging.error(f"Function arguments must be lists of dictionaries: {e}")
        raise TypeError(f"Function arguments must be lists of dictionaries: {e}")

    # Use a dictionary to track unique elements based on a unique key
    unique_elements = {}
    for item in combined_lists:
        try:
            keys = tuple(item[key] for key in unique_keys)
        except KeyError as e:
            logging.error(f"Missing key in one of the dictionaries: {e}")
            raise KeyError(f"Missing key in one of the dictionaries: {e}")
        if keys not in unique_elements:
            unique_elements[keys] = item

    # Convert the unique elements back to a list
    combined = list(unique_elements.values())

    if combined is None:
        logging.error("The combined list is None")
        raise ValueError("The combined list is None")

    return combined
