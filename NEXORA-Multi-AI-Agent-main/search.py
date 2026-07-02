from ddgs import DDGS


def web_search(query, max_results=5):

    results = []

    try:
        with DDGS(timeout=5) as ddgs:

            data = ddgs.text(
                query,
                max_results=max_results
            )

            for item in data:
                results.append(
                    {
                        "title": item.get("title"),
                        "link": item.get("href"),
                        "snippet": item.get("body")
                    }
                )

    except Exception as e:
        return [{
            "title": "Search Error",
            "link": "",
            "snippet": str(e)
        }]

    return results
