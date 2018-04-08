from setuptools import setup, find_packages

setup(name='jeopardy_game',
      version='0.0.1',
      description='A jeopardy game',
      install_requires=['setuptools>=4.0.1'],
      url='https://github.com/HaywardPeirce/jeopardy-game',
      packages = find_packages(),
      py_modules = ['jeopardy_game.jeopardy'],
      include_package_data=True,
      zip_safe=False
     )