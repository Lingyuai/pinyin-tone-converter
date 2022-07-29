"""
Based on https://github.com/chanind/pinyin-tone-converter by David Chanin
and on PinyinConverter by David Chanin and Jen Liu @quizlet 2013
Inspired by http://stackoverflow.com/questions/1598856/convert-numbered-to-accentuated-pinyin/5607888#5607888
Authors: David Chanin and Jen Liu
"""

import re

pinyin_regex = r"(shuang|chuang|zhuang|xiang|qiong|shuai|niang|guang|sheng|kuang|shang|jiong|huang|jiang|shuan|xiong|zhang|zheng|zhong|zhuai|zhuan|qiang|chang|liang|chuan|cheng|chong|chuai|hang|peng|chuo|piao|pian|chua|ping|yang|pang|chui|chun|chen|chan|chou|chao|chai|zhun|mang|meng|weng|shai|shei|miao|zhui|mian|yong|ming|wang|zhuo|zhua|shao|yuan|bing|zhen|fang|feng|zhan|zhou|zhao|zhei|zhai|rang|suan|reng|song|seng|dang|deng|dong|xuan|sang|rong|duan|cuan|cong|ceng|cang|diao|ruan|dian|ding|shou|xing|zuan|jiao|zong|zeng|zang|jian|tang|teng|tong|bian|biao|shan|tuan|huan|xian|huai|tiao|tian|hong|xiao|heng|ying|jing|shen|beng|kuan|kuai|nang|neng|nong|juan|kong|nuan|keng|kang|shua|niao|guan|nian|ting|shuo|guai|ning|quan|qiao|shui|gong|geng|gang|qian|bang|lang|leng|long|qing|ling|luan|shun|lian|liao|zhi|lia|liu|qin|lun|lin|luo|lan|lou|qiu|gai|gei|gao|gou|gan|gen|lao|lei|lai|que|gua|guo|nin|gui|niu|nie|gun|qie|qia|jun|kai|kei|kao|kou|kan|ken|qun|nun|nuo|xia|kua|kuo|nen|kui|nan|nou|kun|jue|nao|nei|hai|hei|hao|hou|han|hen|nai|rou|xiu|jin|hua|huo|tie|hui|tun|tui|hun|tuo|tan|jiu|zai|zei|zao|zou|zan|zen|eng|tou|tao|tei|tai|zuo|zui|xin|zun|jie|jia|run|diu|cai|cao|cou|can|cen|die|dia|xue|rui|cuo|cui|dun|cun|cin|ruo|rua|dui|sai|sao|sou|san|sen|duo|den|dan|dou|suo|sui|dao|sun|dei|zha|zhe|dai|xun|ang|ong|wai|fen|fan|fou|fei|zhu|wei|wan|min|miu|mie|wen|men|lie|chi|cha|che|man|mou|mao|mei|mai|yao|you|yan|chu|pin|pie|yin|pen|pan|pou|pao|shi|sha|she|pei|pai|yue|bin|bie|yun|nüe|lve|shu|ben|ban|bao|bei|bai|lüe|nve|ren|ran|rao|xie|re|ri|si|su|se|ru|sa|cu|ce|ca|ji|ci|zi|zu|ze|za|hu|he|ha|ju|ku|ke|qi|ka|gu|ge|ga|li|lu|le|qu|la|ni|xi|nu|ne|na|ti|tu|te|ta|xu|di|du|de|bo|lv|ba|ai|ei|ao|ou|an|en|er|da|wu|wa|wo|fu|fo|fa|nv|mi|mu|yi|ya|ye|me|mo|ma|pi|pu|po|yu|pa|bi|nü|bu|lü|e|o|a)r?[1-5]"  # noqa

vowels = {"a*": 0, "e*": 1, "i*": 2, "o*": 3, "u*": 4, "ü*": 5, "A*": 6, "E*": 7, "I*": 8, "O*": 9, "U*": 10, "Ü*": 11}

pinyin = {
    1: ["ā", "ē", "ī", "ō", "ū", "ǖ", "Ā", "Ē", "Ī", "Ō", "Ū", "Ǖ"],
    2: ["á", "é", "í", "ó", "ú", "ǘ", "Á", "É", "Í", "Ó", "Ú", "Ǘ"],
    3: ["ǎ", "ě", "ǐ", "ǒ", "ǔ", "ǚ", "Ǎ", "Ě", "Ǐ", "Ǒ", "Ǔ", "Ǚ"],
    4: ["à", "è", "ì", "ò", "ù", "ǜ", "À", "È", "Ì", "Ò", "Ù", "Ǜ"],
    5: ["a", "e", "i", "o", "u", "ü", "A", "E", "I", "O", "U", "Ü"],
}


class PinyinToneConverter:
    def get_accent_map(self):
        stars = (
            "a*i a*o e*i ia* ia*o ie* io* iu* "
            "A*I A*O E*I IA* IA*O IE* IO* IU* "
            "o*u ua* ua*i ue* ui* uo* üe* "
            "O*U UA* UA*I UE* UI* UO* ÜE* "
            "A* E* I* O* U* Ü* "
            "a* e* i* o* u* ü*"
        )
        no_stars = stars.replace("*", "")
        stars_list = stars.split(" ")

        populated_accent_map = {}
        for idx, base in enumerate(no_stars.split(" ")):
            populated_accent_map[base] = stars_list[idx]

        return populated_accent_map

    def get_replacement(self, match: str):
        accent_map = self.get_accent_map()
        tone = int(match[-1])
        word = match[0:-1].replace("v", "ü").replace("V", "Ü")

        for base, vowel in accent_map.items():
            if base in word:
                vowel_char = re.search(r"(.\*)", vowel)
                vowel_char = vowel_char.group(0)
                if vowel:
                    vowel_num = vowels[vowel_char]
                    accented_vowel = pinyin[tone][vowel_num]
                    replaced_word = word.replace(base, vowel).replace(vowel_char, accented_vowel)
                    return replaced_word

        return match

    def convert_text(self, text_to_convert):
        converted_text = text_to_convert

        # Find words with a number behind them, and replace with callback fn.
        matches = re.finditer(pinyin_regex, text_to_convert, re.MULTILINE)
        if not matches:
            return converted_text

        for _, match in enumerate(matches, start=1):
            word_match = match.group()
            replacement = self.get_replacement(word_match)
            converted_text = converted_text.replace(word_match, replacement)

        return converted_text
