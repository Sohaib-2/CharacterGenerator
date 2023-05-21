# Character Generator

The Character Generator is a simple application that allows users to generate fictional character profiles based on various attributes such as gender, age, appearance, personality traits, skills, and background. Users can also save generated characters and engage in dialogues with them.

## Features

- Generate random character profiles by selecting attributes such as gender, age, appearance, personality traits, skills, and background.
- Save generated characters for future reference.
- Engage in dialogues with saved characters to simulate interactive storytelling.

## Requirements

- Python 3.x
- Streamlit (install using `pip install streamlit`)
- Other dependencies mentioned in `requirements.txt`

## Usage

1. Install the required dependencies by running the command `pip install -r requirements.txt`.
2. Run the application by executing the command `streamlit run app.py`.
3. The application will open in your default web browser.
4. Select the desired page from the sidebar: "Generate Character" or "Dialogue".
5. On the "Generate Character" page, choose attributes for your character and click the "Generate Character" button. The generated character will be displayed, and you can save it for future reference.
6. On the "Dialogue" page, select a saved character from the dropdown list and start a dialogue with the character based on their description.

## File Structure

- `app.py`: The main application file that contains the Streamlit code for generating characters and dialogues.
- `functions.py`: Helper functions for generating characters and dialogues.
- `generated_characters.txt`: Text file to store the saved character descriptions.
- `requirements.txt`: List of dependencies required by the application.

## Contributions

Contributions are welcome! If you have any suggestions or improvements for the project, please feel free to open an issue or submit a pull request.