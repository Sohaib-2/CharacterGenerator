from functions import *
import openai

OPENAI_API_KEY = st.text_input("Your OPENAI_API_KEY:")
openai.api_key = OPENAI_API_KEY


GENDERS = ["Male", "Female"]
AGES = ["Child", "Teenager", "Young adult", "Adult", "Elderly"]
APPEARANCES = ["Athletic build", "Slim build", "Muscular build", "Curvy build","Tall and lean build",
               "Blonde hair", "Brunette hair", "Red hair", "Black hair",
               "Brown eyes", "Blue eyes", "Green eyes"]
PERSONALITY_TRAITS = [
    "Brave", "Witty", "Ambitious", "Caring", "Loyal", "Intelligent",
    "Creative", "Adventurous", "Confident", "Mysterious", "Charming",
    "Optimistic", "Compassionate", "Humble", "Perceptive", "Analytical",
    "Energetic", "Reliable", "Curious", "Assertive", "Patient", "Sincere",
    "Outgoing", "Calm", "Resourceful", "Empathetic", "Determined",
    "Honest", "Independent", "Wise"
]
SKILLS = [
    "Archery", "Cooking", "Data Analysis", "Virtual Reality", "Machine Learning",
    "Photography", "Graphic Design", "Public Speaking", "Parkour", "Quantum Physics",
    "Woodworking", "Yoga", "Skydiving", "Gardening", "Speed Reading", "Beekeeping",
    "Painting", "Psychology", "Skiing", "Carpentry", "Songwriting", "Chess",
    "Fashion Design", "Climbing", "Equestrianism", "Bodybuilding", "Sailing",
    "Bowling", "Poetry Writing", "Sudoku"
]

BACKGROUNDS = [
    "Noble lineage", "Raised in a small village", "Orphaned",
    "Trained by a master", "Exiled from their homeland", "Scholarly background",
    "Military background", "Street urchin", "Criminal past", "Merchant family",
    "Priest/Priestess", "Nomadic upbringing", "Royalty", "Performing artist",
    "Scientist/Inventor", "Foreign diplomat", "Explorer/Adventurer",
    "Healer/Medic", "Farmers/Laborer", "Outcast", "Slave/Indentured servant",
    "Politician", "Artisan/Craftsperson", "Spiritual leader", "Outlaw/Rebel"
]


def main():
    st.set_page_config(page_icon="🎭", page_title="Charm Craft")
    st.title("CharmCraft")

    page = st.sidebar.selectbox("Select page:", ["Generate Character", "Dialogue", "Generate Story"])

    if page == "Generate Character":
        st.header("Generate Character")

        selected_gender = st.selectbox("Select gender:", GENDERS)
        selected_age = st.selectbox("Select age:", AGES)
        selected_appearances = st.multiselect("Select appearance:", APPEARANCES)
        selected_personality_traits = st.multiselect("Select personality traits:", PERSONALITY_TRAITS)
        selected_skills = st.multiselect("Select skills:", SKILLS)
        selected_backgrounds = st.multiselect("Select background:", BACKGROUNDS)
        char_name = st.text_input("Name Your Character:")

        if st.button("Generate Character"):
            character = generate_character(selected_gender, char_name, selected_age, selected_appearances,
                                           selected_personality_traits, selected_skills, selected_backgrounds)
            st.subheader("Character Generated!")
            st.write(character)

            character_name = extract_character_name(character)
            if character_name:
                st.session_state.character_name = character_name
                st.session_state.character_description = character
                save_character(character)
                st.success("Character saved successfully!")
            else:
                st.error("Failed to extract character name from the generated description.")

    elif page == "Dialogue":
        st.header("Dialogue")
        try:
            characters = load_characters()
            char_names = [line.split()[0] for line in characters]
            if characters:
                selected_character = st.selectbox("Select character:", char_names)

                for character in characters:
                    if selected_character in character:
                        generate_dialogue(character)
                        break
        except FileNotFoundError:
            st.warning("No characters available for dialogue. Generate a character first.")
    elif page == "Generate Story":
        st.header("Story Generator")
        try:
            characters = load_characters()
            char_names = [line.split()[0] for line in characters]
            if characters:
                selected_character = st.selectbox("Select character:", char_names)

                for character in characters:
                    if selected_character in character:
                        if st.button("Generate Story"):
                            generate_story(character)
                        break
        except FileNotFoundError:
            st.warning("No characters available. Generate a character first.")


if __name__ == "__main__":
    main()
