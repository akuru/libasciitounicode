This is a simple python library to convert ASCII encodings to unicode.

# How to install.
``` python
pip install libasciitounicode
```

# Example usage.
import the Font class and to_unicode function.
```python
from libasciitounicode.converter import Font, to_unicode
```
Give the path to your yaml file containing mappings as the filepath.
```python
f = Font("abhaya", "sinhala", filepath="tests/fm_abhaya.yaml") 
unicode_text = to_unicode(f, ascii_text)
```
