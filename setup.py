from setuptools import setup

setup(
    name='msa',
    version='1.0.0',
    description='Maven settings manager',
    url='https://github.com/Gunmer/maven-setting-manager',
    author='Gunmer',
    author_email='csosaur@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=['msa', 'msa.action', 'msa.util'],
    scripts=['bin/msa'],
    entry_points={'console_scripts': ['src=msn.command_line:main']}
)
