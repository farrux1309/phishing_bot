cache = {}

def get_cache(url, lang="uz"):
    key = f"{url}_{lang}"
    return cache.get(key)

def set_cache(url, result, lang="uz"):
    key = f"{url}_{lang}"
    cache[key] = result