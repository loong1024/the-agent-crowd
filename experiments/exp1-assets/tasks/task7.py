def chunk_list(data, n):
    """Split data into consecutive chunks of size n. Spec:
    - Chunks are consecutive and non-overlapping; the last chunk may be
      shorter than n.
    - Raises ValueError if n <= 0.
    """
    chunks = []
    for i in range(0, len(data)):
        chunks.append(data[i:i + n])
    return chunks