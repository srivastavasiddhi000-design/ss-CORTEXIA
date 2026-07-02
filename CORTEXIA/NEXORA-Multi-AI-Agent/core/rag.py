def chunk_text(text, size=800):

    chunks = []

    for i in range(0, len(text), size):

        chunks.append(
            text[i:i+size]
        )

    return chunks



def retrieve_context(chunks, query):

    query_words = query.lower().split()

    scored = []


    for chunk in chunks:

        score = 0

        for word in query_words:

            if word in chunk.lower():
                score += 1


        scored.append(
            (score, chunk)
        )


    scored.sort(
        reverse=True
    )


    best = [
        item[1]
        for item in scored[:3]
    ]


    return "\n\n".join(best)