# 🎬 CineMatch — Movie Recommendation System

Discover your next favorite movie with **CineMatch**, a content-based movie recommendation web application built using Python and Streamlit.

CineMatch analyzes movie information such as genres, keywords, plot overviews, cast, and crew to recommend five similar movies based on the movie selected by the user.

## ✨ Features

- **Movie Recommendations:** Get five similar movie suggestions from a selected film.
- **Movie Posters:** View movie posters fetched from The Movie Database (TMDB).
- **Interactive Interface:** Choose movies using a dropdown and get recommendations with one click.
- **Content-Based Filtering:** Uses text preprocessing and cosine similarity to identify similar movies.
- **Responsive Web Interface:** A clean, minimal interface designed for an easy user experience.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application and user interface |
| Pandas | Data loading and manipulation |
| Scikit-learn | Text vectorization and similarity calculation |
| NLTK | Text stemming and preprocessing |
| NumPy | Numerical operations |
| Pickle | Saving and loading trained data |
| TMDB API | Fetching movie details and posters |

## ⚙️ How It Works

1. **Data Collection:** Movie metadata and credits are combined into a single dataset.
2. **Text Preprocessing:** Movie overviews, genres, keywords, cast, and crew are cleaned and combined into tags.
3. **Feature Extraction:** CountVectorizer converts the text tags into numerical vectors.
4. **Text Normalization:** Porter stemming reduces words to their root forms.
5. **Similarity Calculation:** Cosine similarity compares movies based on their feature vectors.
6. **Recommendation:** When a user selects a movie, CineMatch ranks similar movies and displays the top five recommendations with their posters.

## 📁 Project Structure

```text
cinematch-movie-recommender/
│
├── app.py
├── movie_dict.pkl
├── requirements.txt
├── .gitignore
├── .streamlit/
│   └── secrets.toml
│
└── README.md
```

**Note:** The similarity matrix may be stored as `similarity.pkl` or reconstructed from split files, depending on the final deployment configuration. Include the correct data files required by your working version of `app.py`.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Sudiksha29/cinematch-movie-recommender.git
cd cinematch-movie-recommender
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the TMDB API key

Create a file named `.streamlit/secrets.toml` and add:

```toml
TMDB_API_KEY = "your_tmdb_api_key"
```

Replace the placeholder with your own TMDB API key.

**Security:** Never commit your real API key or `secrets.toml` to a public GitHub repository.

### 5. Start the application

```bash
streamlit run app.py
```

Open the local URL shown in your terminal, usually `http://localhost:8501`.

## 🔑 API Configuration

CineMatch uses the TMDB API to retrieve movie information and poster paths.

The application reads the API key securely through Streamlit secrets:

```python
api_key = st.secrets["TMDB_API_KEY"]
```

For local development, configure `.streamlit/secrets.toml`. For Streamlit Community Cloud, add the key under the application's **Settings → Secrets** section.

## ☁️ Deployment

CineMatch can be deployed using Streamlit Community Cloud.

1. Push the project files to GitHub.
2. Visit https://share.streamlit.io/.
3. Sign in using your GitHub account.
4. Select **Create app** and choose your repository.
5. Set `app.py` as the application entry point.
6. Add your TMDB API key under the app's Secrets settings.
7. Deploy and test the live application.

Ensure that all required data files are available to the deployed application. Large similarity matrices may require a different storage or loading strategy to meet hosting limits.

## 🔮 Future Improvements

- Add movie genre and language filters.
- Display movie ratings, release years, and descriptions.
- Improve recommendation speed and memory efficiency.
- Add a watchlist and favorite movies feature.
- Enhance the interface for mobile devices.
- Explore hybrid recommendations using content and user ratings.

## 🎯 Project Objective

The objective of CineMatch is to demonstrate how machine learning techniques can be used to build a practical movie discovery application. The project combines natural language processing, vectorization, cosine similarity, API integration, and web application development.

## 👩‍💻 Author

**Sudiksha Ingale**

GitHub: https://github.com/Sudiksha29

---

*Built with Python, machine learning, and Streamlit.*
