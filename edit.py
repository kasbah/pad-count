import pickle

pickle_path = "rejected.pickle"

with open(pickle_path, "rb") as f:
    rejected = pickle.load(f)

rejected['global'] = filter(lambda s: s != '05867e58dde249645fb8a8e5ecb65a699dc5fff7', rejected['global'])


with open(pickle_path, "w") as f:
    pickle.dump(rejected, f)
