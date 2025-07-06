import pandas as pd
import numpy as np

# Sample Ratings Data (UserID, MovieID, Rating)
ratings_data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4],
    'movie_id': [10, 20, 30, 10, 20, 10, 30, 40],
    'rating':   [4, 5, 3, 5, 3, 2, 4, 5]
}
df = pd.DataFrame(ratings_data)

# Create User-Item Matrix
user_movie_matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating')

# Fill NaN with 0 for similarity computation
filled_matrix = user_movie_matrix.fillna(0)

# Compute cosine similarity between users
def cosine_similarity(matrix):
    dot_product = np.dot(matrix, matrix.T)
    norm = np.linalg.norm(matrix, axis=1)
    similarity = dot_product / (norm[:, None] * norm[None, :])
    return similarity

similarity_matrix = cosine_similarity(filled_matrix.to_numpy())

# Convert similarity matrix to DataFrame for readability
similarity_df = pd.DataFrame(similarity_matrix, index=filled_matrix.index, columns=filled_matrix.index)

# Function to recommend movies to a user
def recommend_movies(user_id, top_n=2):
    if user_id not in filled_matrix.index:
        return f"User {user_id} not found."
    
    sim_scores = similarity_df[user_id].drop(user_id)
    similar_users = sim_scores.sort_values(ascending=False).index

    # Get movies not rated by user
    user_rated = user_movie_matrix.loc[user_id].dropna().index
    all_movies = set(user_movie_matrix.columns)
    unrated_movies = all_movies - set(user_rated)

    movie_scores = {}
    for movie in unrated_movies:
        total_score = 0
        sim_sum = 0
        for other_user in similar_users:
            rating = user_movie_matrix.loc[other_user].get(movie)
            if not np.isnan(rating):
                sim = similarity_df.loc[user_id, other_user]
                total_score += sim * rating
                sim_sum += sim
        if sim_sum > 0:
            movie_scores[movie] = total_score / sim_sum

    sorted_recommendations = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations[:top_n]

# 🔍 Test Recommendation for User 1
print("Top recommendations for User 1:")
print(recommend_movies(user_id=1))	