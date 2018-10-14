from setuptools import setup, find_packages

setup(name="donkey_gym",
      version="0.1",
      url="https://github.com/tawnkramer/sdsandbox/src/donkey_gym",
      author="Tawn Kramer",
      license="MIT",
      packages=find_packages(),
      install_requires = ["gym", "numpy", 'pillow']
      )
