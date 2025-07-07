# Recommendation-System-


# 🎞️ Movie Recommendation System – User‑Based Collaborative Filtering

This repository contains a minimal, fully‑worked example of building a user‑based collaborative filtering recommender in pure Pandas + NumPy.
It demonstrates how to:

1. Construct a user‑item ratings matrix


2. Compute cosine similarity between users


3. Aggregate scores to generate personalised movie recommendations



<div align="center">

Figure 1 – Cosine‑similarity between users (brighter = more similar).

</div>
---

🚀 Quick Start

# 1. Clone the repo & enter it
git clone https://github.com/your‑username/recommender-demo.git
cd recommender-demo

# 2. (Optional) Create a fresh virtual environment
python -m venv .venv
source .venv/bin/activate  # 🪟 Use .venv\\Scripts\\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the script
python recommendation\ system.py


---

# 🧐 How It Works

Phase	Description

- Data prep	Ratings are loaded into a  user × movie matrix (pivot_table).
- Similarity	A cosine‑similarity matrix is computed with:<br>\
- Scoring	For every movie a user hasn’t rated, we take a weighted average of ratings from the k most‑similar users.
- Ranking	The top‑N movies with the highest weighted scores are returned.



# 🖥️ Sample Output

Top recommendations for User 1.                - (No recommendations — either all movies are rated, or no similar ratings found)



📂 File Structure

.
├─ recommendation system.py   # The complete script
├─ similarity_heatmap.png     # Generated demo visualisation
└─ README.md                  # You’re reading it!



# 🔧 Requirements

- Python ≥ 3.8

- pandas

- numpy

- matplotlib



🤔 Extending the Demo

Replace dummy ratings with a real dataset (e.g. MovieLens)

Try item-based similarity or matrix factorisation (SVD, NMF)

Turn this logic into a function/class and serve with a REST API


# 📜 License

Released under the MIT License – see LICENSE for details.




