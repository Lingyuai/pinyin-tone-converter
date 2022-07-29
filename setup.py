from setuptools import find_packages, setup

from pinyin_tone_converter import __version__ as version  # noqa  # isort:skip

DESCRIPTION = "Numbered pinyin to accented pinyin converter"
EXTRAS_DEV_TEST = [
    "coverage",
    "pytest>=3.10",
]

# Setting up
setup(
    name="pinyin-tone-converter",
    version=version,
    author="Lingyuai",
    author_email="developers@lingyuai.com",
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Lingyuai/pinyin-tone-converter",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    extras_require={
        "dev": EXTRAS_DEV_TEST,
        "dev-test": EXTRAS_DEV_TEST,
    },
    download_url=("https://github.com/Lingyuai/pinyin-tone-converter/archive/%s.tar.gz" % version),
    keywords=[
        "python",
        "pinyin",
        "pinyin-tone-converter",
        "tones",
        "numbered tones",
        "marked tones",
        "accented tones",
        "chinese",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
    ],
)
