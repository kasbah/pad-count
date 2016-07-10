import pickle

pickle_path = "rejected.pickle"

with open(pickle_path, "rb") as f:
    rejected = pickle.load(f)

rejected[4] = []

with open(pickle_path, "w") as f:
    pickle.dump(rejected, f)
