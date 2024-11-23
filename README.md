# Korean Drama Recommendation System
A Python-based Korean Drama Recommendation System that utilizes a precomputed cosine similarity matrix to recommend dramas similar to a given title. The system is enhanced with a Gradio web interface for an interactive experience, where users can input a drama title and receive tailored recommendations.

## Features
- Content-Based Recommendation: Uses metadata and numerical features to compute cosine similarity between dramas.
- Text Cleaning for Matching: Handles user input regardless of punctuation or case.
- Interactive Interface: Built with Gradio to provide an intuitive, real-time recommendation system.
- Customizable Outputs: Allows users to specify the number of recommendations.
- Robust Error Handling: Alerts users when a drama title is not found in the dataset.

## Technologies Used
- **Python**: Core programming language.
- **Gradio**: For building a user-friendly web interface.
- **Pandas**: For data manipulation and handling.
- **Scikit-learn**: For feature processing and similarity computations.
- **TF-IDF Vectorization**: To extract text-based features from drama metadata.
- **Cosine Similarity**: For determining the similarity between dramas.

## File Structure
  ```bash
  .
  ├── korean_drama.csv                  # Input dataset
  ├── cosine_similarity_matrix.csv      # Precomputed cosine similarity matrix
  ├── training.py                       # Code for generating similarity matrix
  ├── recom_drama.py                    # Gradio-based web application
  ├── requirements.txt                  # Python dependencies
  └── README.md                         # Documentation (this file)
 ```
## Setup and Usage
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- pip (Python package manager)
- gradio==5.6.0
- numpy==2.1.3
- pandas==2.2.3
- scikit_learn==1.5.2


### Installation
1. Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/your-username/korean-drama-recommendation.git
cd korean-drama-recommendation
```
2. Install the required Python libraries:
```bash
pip install -r requirements.txt
```
3. Prepare the Similarity Matrix
Run the main.py script to process the dataset and compute the cosine similarity matrix:
```bash
python training.py
```
This script reads korean_drama.csv, preprocesses the data, and saves the similarity matrix as cosine_similarity_matrix.csv.

4. Run the Gradio Application
Start the recommendation system using the Gradio interface:
```bash
python recom_drama.py
```
The application will launch in your default browser. Enter a drama title and the number of recommendations to get started!

## Using the Gradio Interface
1. Input the title of a Korean drama (e.g., Star Struck).
2. Specify the number of recommendations you want (default: 2).
3. View the recommended series in a tabular format.

## Dataset
The system uses a dataset of Korean dramas (korean_drama.csv), which includes metadata such as:

- Drama Name
- Synopsis
- Duration
- Number of Episodes
- Country of Origin
- Popularity Metrics
If you want to use a custom dataset, ensure it has similar columns to avoid errors.

##Customization
- Change the Number of Recommendations: Adjust the n_recommendations parameter in app.py.
- Integrate Additional Features: Modify main.py to include new metadata or numerical features for better recommendations.
- Deploy on Cloud: Use a cloud platform (e.g., AWS, Heroku) to make the application accessible online.

## Examples
### Input:
- Drama Title: Star Struck
- Number of Recommendations: 3

### Output:
|Series Title|
|------------|
|Love in the Moonlight|
|Crash Landing on You|
|The Glory|

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For questions or feedback, feel free to contact:

- **Name**: Muhammed Tariq
- **Email**: [your-email@example.com]
Enjoy discovering new Korean dramas! 🎥
