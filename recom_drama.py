import pandas as pd
from gradio import Interface, Dataframe
import string

# Load the similarity matrix and ensure the index is set
cosine_sim_df = pd.read_csv("./cosine_similarity_matrix.csv", index_col=0)

def clean_text(text):
    """
    Removes punctuation and converts text to lowercase for consistent matching.
    """
    return text.translate(str.maketrans("", "", string.punctuation)).lower()

def recommend_series(Drama, n_recommendations=2):
    """
    Recommend series similar to the input title, regardless of punctuation or case.

    Args:
        Drama (str): Input series title.
        n_recommendations (int): Number of recommendations to return.

    Returns:
        pd.DataFrame: Recommendations with series titles.
    """
    # Clean input title
    cleaned_drama = clean_text(Drama)
    
    # Clean the index for comparison
    cleaned_index = cosine_sim_df.index.map(clean_text)
    
    # Check if the cleaned title exists in the dataset
    if cleaned_drama not in cleaned_index.values:
        return pd.DataFrame({"Error": [f"Series '{Drama}' not found in dataset"]})
    
    # Get the original title that matches the cleaned input
    original_title = cosine_sim_df.index[cleaned_index == cleaned_drama][0]
    
    # Sort and get the top recommendations
    sim_drama = cosine_sim_df[original_title].sort_values(ascending=False)[1:n_recommendations+1]
    
    # Create a DataFrame for recommendations
    recommendations = pd.DataFrame({
        "Series Title": sim_drama.index
    })
    return recommendations

# Define Gradio interface
gradio_interface = Interface(
    fn=recommend_series,
    examples=[["Star Struck", 3], ["Queenmaker", 5]],  # Example inputs
    inputs=["text", "number"],  # Input: Series title and number of recommendations
    outputs=Dataframe(headers=["Series Title"]),  # Output: Table format
)

gradio_interface.launch()
