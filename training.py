import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load dataset
korean_drama = pd.read_csv("./korean_drama.csv")
df = korean_drama.copy()

# Handle missing values in the 'duration' column
impute = SimpleImputer(missing_values=np.nan, strategy="constant", 
                       fill_value=int(round(df["duration"].mean())))
df["duration"] = pd.DataFrame(impute.fit_transform(df[["duration"]]))

# Drop rows with missing 'synopsis'
df = df[df["synopsis"].notna()]

# Drop unnecessary columns
df = df.drop(columns=["kdrama_id", "director", "screenwriter", "aired_on", 
                      "start_dt", "end_dt", "org_net"])

# Encode categorical 'content_rt' column
encoder = LabelEncoder()
df["content_rt"] = encoder.fit_transform(df["content_rt"])

# Create combined metadata column
df["MetaData"] = (df["drama_name"] + " " + df["country"] + " " + 
                  df["type"] + " " + df["synopsis"])

# Convert metadata to TF-IDF features
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["MetaData"])

# Scale numerical features
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(
    df[["year", "tot_eps", "duration", "content_rt", "rank", "pop"]]
)

# Compute cosine similarity
cosine_sim = cosine_similarity(
    np.hstack([tfidf_matrix.toarray(), scaled_features])
)

# Create similarity DataFrame
cosine_sim_df = pd.DataFrame(
    cosine_sim, index=df["drama_name"], columns=df["drama_name"]
)

# Save similarity matrix to CSV
output_file = "cosine_similarity_matrix.csv"
cosine_sim_df.to_csv(output_file, index=True)

# Recommendation function
def recommend_movies(movie_title, cosine_sim_df, n_recommendations=2):
    """
    Recommends movies similar to the given title.
    
    Parameters:
        movie_title (str): Title of the movie to base recommendations on.
        cosine_sim_df (pd.DataFrame): DataFrame containing similarity scores.
        n_recommendations (int): Number of recommendations to return.
    
    Returns:
        list: List of recommended movie titles.
    """
    if movie_title not in cosine_sim_df.index:
        raise ValueError(f"'{movie_title}' not found in the dataset.")
    
    sim_movies = cosine_sim_df[movie_title].sort_values(ascending=False)[1:n_recommendations+1]
    return list(sim_movies.index)

# Interactive user input for recommendations
try:
    movie_to_recommend = input("Choose a series: ")
    recommendations = recommend_movies(movie_to_recommend, cosine_sim_df)
    print("Recommended series:")
    for rec in recommendations:
        print(f"- {rec}")
except ValueError as e:
    print(e)