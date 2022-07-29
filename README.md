# pinyin-tone-converter

<p align="center">
    <a href="https://circleci.com/gh/Synkied/pinyin-tone-converter">
        <img src="https://circleci.com/gh/Synkied/pinyin-tone-converter.svg?style=svg" alt="TravisCI Build Status"/>
    </a>
</p>

Python library to convert pinyin with numbers to tone with marks. This library is based on https://github.com/chanind/pinyin-tone-converter

## Install

```python
pip install pinyin-tone-converter
```

## How to use

```python
from pinyin_tone_converter.pinyin_tone_converter import PinyinToneConverter
PinyinToneConverter().convert_text("lu4")

"lù"
```

Examples can be seen in tests.
