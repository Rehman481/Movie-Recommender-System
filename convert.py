import pickle
import numpy as np

print("Loading original files...")

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

print("Converting to numpy format...")

np.save("similarity.npy", similarity)

print("DONE! Saved as similarity.npy")