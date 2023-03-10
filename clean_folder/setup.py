from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='01',
      description='Script for sorting files in folders by type',
      url='https://github.com/FlipThatLux/Homework_06.git',
      author='Flip',
      author_email='veseliymoryak@gmail.com',
      license='what',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder = clean_folder.clean']})