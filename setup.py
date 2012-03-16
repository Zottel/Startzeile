from distutils.core import setup

setup(
    name='Startzeile',
    version='0.0.1',
    author='Julius Roob',
    author_email='julius@juliusroob.de',
    packages=['startzeile', 'startzeile.test'],
    scripts=['bin/test.py','bin/run.py'],
    #url='',
    license='LICENSE.txt',
    description='A Simple Bookmarking service',
    long_description=open('README.txt').read(),
    install_requires=[
        #"Flask >= 0.6",
    ],
)
