from libasciitounicode.converter import Font, to_unicode
from libasciitounicode.file_proc import Doc
import sys

file_location = sys.argv[1]

font = Font("abhaya", "sinhala", yaml_filepath="tests/fm_abhaya.yaml")
doc = Doc(file_location)
content = doc.get_content()

converted_text = to_unicode(font, *content)

print(converted_text)
