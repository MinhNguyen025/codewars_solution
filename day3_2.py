def domain_name(url):
    # Remove "http://" or "https://" if present
    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]

    # Remove "www." if present
    if url.startswith("www."):
        url = url[len("www."):]

    # Split by "/" to get the domain part
    parts = url.split("/")
    domain = parts[0]

    # Split by "." to get the domain name
    domain_parts = domain.split(".")
    return domain_parts[0]


