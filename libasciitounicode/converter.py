import yaml


class Font:
    def __init__(self, fontname, language, filepath=None):
        self.fontname = fontname
        self.language = language
        self.filepath = filepath

    def __repr__(self):
        return self.fontname + ' ' + self.language

    def __load_yaml__(self, filepath):
        return yaml.load(open(filepath))

    def from_yaml(self, filepath=None):
        filepath = self.filepath if filepath == None else filepath
        yaml_content = self.__load_yaml__(filepath)
        # ToDo: When finalized, read "map", "combinations" and "singles" from schema.
        return {**yaml_content["map"]["combinations"], **yaml_content["map"]["singles"]}

    def from_predefined(self):
        # ToDo: once we finalize the YAML repo load the YAML content from that repo.
        # load(self.fontname, self.language)
        pass


def to_unicode(font, text):
    mappings = font.from_yaml()
    for asc, unic in mappings.items():
        text = text.replace(asc, unic)
    return text
