def extract_title(markdown):
    lines = markdown.split('\n')

    for line in lines:
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
            return title
        else:
            raise Exception("No title found in the markdown content.")