from setuptools import setup, find_packages

setup(
    name = 'pitch',
    version = '0.1.0',
    description = 'A digital signal processing experiment on pitch tracking.',
    author = 'Zilong Liang',
    author_email = 'zlliang15@fudan.edu.cn',
    url = 'https://github.com/zlliang/pitch/',
    python_requires='>=3.6.0',
    install_requires=['numpy', 'matplotlib', 'audioread'],
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
