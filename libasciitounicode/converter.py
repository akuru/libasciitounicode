import yaml


class Font:
    def __init__(self, fontname, language, yaml_filepath=None):
        self.fontname = fontname
        self.language = language
        self.yaml_filepath = yaml_filepath

    def __repr__(self):
        return self.fontname + ' ' + self.language

    def __load_yaml__(self, yaml_filepath):
        return yaml.load(open(yaml_filepath))

    def from_yaml(self, yaml_filepath=None):
        yaml_filepath = self.yaml_filepath if yaml_filepath == None else yaml_filepath
        yaml_content = self.__load_yaml__(yaml_filepath)
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
