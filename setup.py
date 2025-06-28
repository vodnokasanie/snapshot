from setuptools import setup, find_packages

setup(
    name="snapshot",
    version="0.1",
    description="A simple system monitoring CLI tool using psutil",
    author="Bulat Torgen",
    author_email="bulattorgen@gmail.com",
    packages=find_packages(),
    install_requires=[
        "psutil",
    ],
    entry_points={
        'console_scripts': [
            'snapshot = snapshot.sysmonitor:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
