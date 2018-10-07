from libasciitounicode.converter import Font, to_unicode
import sys

sentence = sys.argv[1]

print(to_unicode(Font("abhaya", "sinhala", filepath="tests/fm_abhaya.yaml"), sentence))
