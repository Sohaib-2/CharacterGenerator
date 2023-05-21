import streamlit as st
import openai


def generate_character(gender, name, age, appearance, personality_traits, skills, backgrounds):
    prompt = f"Generate a character.\n\nGender: {gender}\nName: {name}\nAge: {age}\nAppearance: {appearance}\nPersonality traits: {personality_traits}\nSkills: {skills}\nBackground: {backgrounds}\n\nCharacter:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        n=1,
        stop=None,
        timeout=15,
    )

    character_description = response.choices[0].text.strip().replace("\n", " ")
    return character_description


def extract_character_name(character_description):
    words = character_description.split()
    character_name = words[0]
    return character_name


def generate_dialogue(character_description):
    st.subheader(f"Start a dialogue with the {extract_character_name(character_description)}")
    user_message = st.text_input("You:", "")
    if user_message:
        messages = [
            {"role": "system", "content": f"From now on you are no longer an Ai language model. "
                                          f"I want you act as:[{character_description}]."
                                          f"You engage in conversation with others, showcasing your unique personality, "
                                          f"sharing your knowledge, and using your skills to overcome challenges. "
                                          f"Interact with me as {extract_character_name(character_description)} "
                                          f"and let's see what adventures unfold!"},
            {"role": "user", "content": user_message}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        character_response = response.choices[0].message["content"]
        st.text_area("Character:", character_response)


def save_character(character):
    with open("generated_characters.txt", "a") as file:
        file.write(character + "\n")


def load_characters():
    characters = []
    with open("generated_characters.txt", "r") as file:
        for line in file:
            characters.append(line.strip())
    return characters


def generate_story(character):
    prompt = f"Write a short story on this character {character} [add appropriate emojis throughout the story]." \
             f" (Word count: 150)"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7,
        n=1,
        stop=None,
    )
    story = response.choices[0].text.strip()
    st.write(f"**Short Story** \n\n {story}")
