import spacy
import pandas as pd

# Load spaCy NLP model
nlp = spacy.load('en_core_web_sm')

# Load both datasets
mind_map_data = pd.read_csv('dataset/mind_map_data.csv')

# Concatenate both datasets into one for idea suggestions
data = pd.concat([mind_map_data, concept_data])

# Clean data: remove rows where 'Idea' is NaN or not a string
data = data.dropna(subset=['Idea'])  # Drop rows with NaN values in 'Idea' column
data = data[data['Idea'].apply(lambda x: isinstance(x, str))]  # Keep rows where 'Idea' is a string

def suggest_related_ideas(user_input):
    # Process user input
    doc = nlp(user_input)
    user_tokens = set([token.lemma_.lower() for token in doc])

    suggestions = []
    for _, row in data.iterrows():
        idea = row['Idea']
        
        # Process the row idea only if it's a valid string
        idea_doc = nlp(idea)  
        idea_tokens = set([token.lemma_.lower() for token in idea_doc])  # Get lemmas of tokens

        # Check for overlap between input and idea tokens
        if len(user_tokens & idea_tokens) > 0:  
            suggestions.append(row['Related Idea'])

    return suggestions if suggestions else ["No suggestions found."]
