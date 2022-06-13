import setuptools

with open('README.md', 'r') as readme:
    description = readme.read()

with open('requirements.txt', 'r') as reqfile:
    requirements = reqfile.readlines()

setuptools.setup(
    name='praetorian',
    version='0.2.0a',
    author='Luzhou Zhang',
    author_email='lzhang1337@gmail.com',
    packages=['praetorian'],
    description='Praetorian is a basic Sentry wrapper in Python.',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/ThaumielSparrow/praetorian',
    license='BSD-3-Clause',
    python_requires='>=3.6',
    requires=requirements,
    install_requires=[],
    keywords='cybersecurity pentesting payload meterpreter listener socket server',
    platforms=['any'],
)
