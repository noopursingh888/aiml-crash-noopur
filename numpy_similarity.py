import numpy as np

# --------------------------------
# Create NumPy Array
# --------------------------------

array = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(array)

# --------------------------------
# Boolean Masking
# --------------------------------

# Filter values greater than 25
mask = array > 25

filtered_array = array[mask]

print("\nBoolean Mask:")
print(mask)

print("\nFiltered Values:")
print(filtered_array)

# --------------------------------
# Broadcasting
# --------------------------------

# Add 5 to every element
broadcast_array = array + 5

print("\nBroadcasted Array:")
print(broadcast_array)

# --------------------------------
# Cosine Similarity Function
# --------------------------------

def cosine_similarity(vec1, vec2):

    dot_product = np.dot(vec1, vec2)

    norm_vec1 = np.linalg.norm(vec1)

    norm_vec2 = np.linalg.norm(vec2)

    similarity = dot_product / (norm_vec1 * norm_vec2)

    return similarity

# --------------------------------
# Test Vector Pair 1
# --------------------------------

vector1 = np.array([1, 2, 3])

vector2 = np.array([1, 2, 3])

similarity1 = cosine_similarity(vector1, vector2)

print("\nCosine Similarity (Pair 1):")
print(similarity1)

# --------------------------------
# Test Vector Pair 2
# --------------------------------

vector3 = np.array([1, 0, 1])

vector4 = np.array([0, 1, 0])

similarity2 = cosine_similarity(vector3, vector4)

print("\nCosine Similarity (Pair 2):")
print(similarity2)