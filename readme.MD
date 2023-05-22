# Character Generator

The Character Generator is a simple application that allows users to generate fictional character profiles based on various attributes such as gender, age, appearance, personality traits, skills, and background. Users can also save generated characters, engage in dialogues with them, and now generate stories as well! 🎭📖✨

## Features

- Generate random character profiles by selecting attributes such as gender, age, appearance, personality traits, skills, and background. 🔄👤
- Save generated characters for future reference. 💾📚
- Engage in dialogues with saved characters to simulate interactive storytelling. 💬🗣️
- Generate stories based on the created characters. 📝📚✨

## Requirements

- Python 3.x
- Streamlit (install using `pip install streamlit`)
- Other dependencies mentioned in `requirements.txt`

## Usage

1. Install the required dependencies by running the command `pip install -r requirements.txt`.
2. Run the application by executing the command `streamlit run app.py`.
3. The application will open in your default web browser.
4. Select the desired page from the sidebar: "Generate Character," "Dialogue," or "Generate Story." 🖱️📋
5. On the "Generate Character" page, choose attributes for your character and click the "Generate Character" button. The generated character will be displayed, and you can save it for future reference.
6. On the "Dialogue" page, select a saved character from the dropdown list and start a dialogue with the character based on their description.
7. On the "Generate Story" page, select the characters you want to include in the story, set the story parameters, and click the "Generate Story" button. The generated story will be displayed.

## File Structure

- `app.py`: The main application file that contains the Streamlit code for generating characters, dialogues, and stories.
- `functions.py`: Helper functions for generating characters, dialogues, and stories.
- `generated_characters.txt`: Text file to store the saved character descriptions.
- `requirements.txt`: List of dependencies required by the application.

## Contributions

Contributions are welcome! If you have any suggestions or improvements for the project, please feel free to open an issue or submit a pull request. 🤝🎉
