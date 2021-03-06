from setuptools import setup

setup(
   name='jikanpy',
   version='2.3.2',
   description='Python wrapper for the Jikan API',
   author='Andrew Conant, Abhinav Kasamsetty',
   packages=['jikanpy'],
   install_requires=['requests', 'aiohttp'],
)
