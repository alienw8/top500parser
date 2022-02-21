from json import JSONEncoder


class DefaultEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def make_json(obj):
    return DefaultEncoder().encode(obj).replace('"None"', "null") \
        .replace(', "', ',"') \
        .replace('": ', '":') \
        .replace('["query', '"query') \
        .replace('"],"variables"', '","variables"')  # FIX IT
