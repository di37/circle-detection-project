# Config folder - `config`

This folder contains configuration constants used throughout the circular object detection project.

## Contents

- `__init__.py`: Exports all constants for easy import
- `constants.py`: Defines global constants and configuration variables

## Constants

The following constants are defined in `constants.py`. These are the global variables that will be used through out the project:

- `UPLOAD_DIR`: Directory to store uploaded images
  - Value: `"data/uploads"`

- `DATABASE_PATH`: Path to the SQLite database file
  - Value: `"data/processed/circular_objects.db"`

- `FORMAT`: Image format for saving processed images
  - Value: `"png"`

- `MODEL_ID`: Identifier for the machine learning model used
  - Value: `"microsoft/Florence-2-large"`

- `TASK_PROMPT`: Prompt used for the image captioning task
  - Value: `"<CAPTION_TO_PHRASE_GROUNDING>"`

- `TEXT_INPUT`: Input text for circle detection
  - Value: `"circle"`

## Usage

To use these constants in your code:

```python
from config import UPLOAD_DIR, DATABASE_PATH, MODEL_ID, FORMAT, TASK_PROMPT, TEXT_INPUT
```

## Modifying Constants

If you need to change any of these constants:

1. Edit the `constants.py` file
2. Be aware that changes may affect multiple parts of the project
3. Ensure that the new values are compatible with the rest of the codebase
4. Update any documentation or comments that reference the changed constants

## Notes

- Always use these constants instead of hardcoding values in your scripts. This makes it easier to maintain and update the project configuration.
- If adding new constants, make sure to export them in `__init__.py` for easy importing.