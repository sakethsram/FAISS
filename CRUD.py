import numpy as np
embeddings = {}

def create_embedding(j):    
    return np.array([ord(char) for char in j], dtype='float32')

def adding_embeddings(animals):
    for i in animals:
        j = animals[i]
        k = create_embedding(j)
        embeddings[i] = k
    return embeddings

def updating(a):
    if a in embeddings:
        return 0 
    else:
        k = create_embedding(a)
        embeddings[a] = k

def printing():
    for animal, embedding in embeddings.items():
        print(f"{animal}: {embedding}")

def embeddings_storage():
    np.savez('embeddings_storage.npz', **embeddings)    

def load_embeddings():
    data = np.load('embeddings_storage.npz', allow_pickle=True)
    loaded_emb = {key: data[key] for key in data}
    return loaded_emb
   
def ask_query(query):        
    t=load_embeddings()
    print("t:",t)
    a=t.get(query)
    print("a:",a)

    return a


def main():
    animals = {
        "Dog": "Bark",
        "Cat": "Meow",
        "Parrot": "Talk",
        "Cow": "Moo",
        "Lion": "Roar"
    }
    adding_embeddings(animals)  
    embeddings_storage()       
    printing()                  

    query = "Dog"
    #query = "how does dog talk"
    res = ask_query(query)
    print(f"Query result for '{query}': {res}")   


if __name__ == "__main__":
    main()
