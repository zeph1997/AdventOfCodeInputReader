from distutils.core import setup
from io import open

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

setup(
  name = 'AdventOfCodeInputReader',         
  packages = ['AdventOfCodeInputReader'],   
  version = '0.0.2',      
  license='MIT',        
  description = 'Package to retrieve input for Advent Of Code',   
  long_description=read('README.md'),
  long_description_content_type="text/markdown",
  author = 'Zeph Ng',                   
  author_email = 'zephngdev@gmail.com',      
  url = 'https://github.com/zeph1997/AdventOfCodeInputReader',   
  download_url = 'https://github.com/zeph1997/AdventOfCodeInputReader/archive/refs/tags/v0.0.2.tar.gz',    
  keywords = ['reader', 'advent', 'of', 'code', 'api'],   
  install_requires=['requests'],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)