from setuptools import setup, find_packages

setup(name='libasciitounicode',
      version='0.1',
      url='https://github.com/keshan/libasciitounicode',
      license='MIT',
      author='CodeLanka',
      author_email='codelanka@googlegroups.com',
      description='Library to convert ASCII encodings to unicode',
      packages=find_packages(exclude=['tests']),
      install_requires=[
          'PyYAML',
          'python-docx',
      ],
      long_description=open('README.md').read(),
      zip_safe=False)
