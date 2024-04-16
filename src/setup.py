from setuptools import setup, find_packages

setup(
    name='src',
    version='1.0.0',
    packages=find_packages(),
    author='Diego Araujo Giovanini',
    author_email='diego.giovanini4@gmail.com',
    description='Biblioteca desenvolvida especificamente para o modelo',
    #long_description='Uma descrição mais detalhada do seu pacote, se necessário.',
    #long_description_content_type='text/markdown',
    #url='https://github.com/seu_usuario/meu_pacote',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=[
        "pandas==2.2.1"
    ],
)
