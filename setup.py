from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='bomberpy',
    version="0.0.1",
    description='O clássico Bomberman',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/vitorito/bomberpy',
    author='João Victor O. Batista',
    author_email='victorolivbati@gmail.com',
    license='MIT',
    keywords=[
        'jogo',
        'game',
        'bomberman',
        'arcade',
        'ação'
    ],
    packages=find_packages(),
    install_requires=['pygame>=2.0'],
    entry_points={
        'console_scripts': [
            'bomberpy=bomberpy.__main__:main'
        ]
    },
    python_requires='>=3.6',
    include_package_data=True,
)
