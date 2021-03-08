import pickle
from sys import argv

def load_pickle_object(path_to_pickle):
    with open(path_to_pickle, 'rb') as file:
        object = pickle.load(file)
    return object

if __name__ == '__main__':
    path_to_pickle = argv[1]
    print(load_pickle(path_to_pickle))
