import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def plot_tsne(embeddings_tags):
    embeddings, tags = zip(*embeddings_tags)
    embeddings = [emb.cpu().detach().numpy() for emb in embeddings]
    tags = np.array(tags)
    
    tsne = TSNE(n_components=2, random_state=42)
    reduced_embeddings = tsne.fit_transform(embeddings)
    
    plt.figure(figsize=(10, 10))
    for tag in set(tags):
        idxs = np.where(tags == tag)
        plt.scatter(reduced_embeddings[idxs, 0], reduced_embeddings[idxs, 1], label=tag)
    
    plt.legend()
    plt.savefig('tsne.png')

# Example usage
import torch
p=torch.load('wepairs.pt')
plot_tsne(p)

