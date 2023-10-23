INTRO_TEMPLATE = """[[:完整规则|返回完整规则目录]]

====== 前言 ======

{content}

[[cr:1|第一章 - 游戏概念 Game Concepts]]
{{{{page>:规则和文档索引&nofooter}}}}"""

MAIN_TEMPLATE = """[[:完整规则|返回完整规则目录]] | {prev_next_chapter}
{content}

[[:完整规则|返回完整规则目录]] | {prev_next_chapter}

{{{{page>:规则和文档索引&nofooter}}}}"""

GLOSSARY_PINYIN_TEMPLATE = """[[:完整规则|返回完整规则目录]]
====== 词汇表（按拼音首字母排序） ======
<WRAP centeralign>
[[cr:glossarycn#字母|字母]] - [[cr:glossarycn#a|A]] - [[cr:glossarycn#b|B]] - [[cr:glossarycn#c|C]] - [[cr:glossarycn#d|D]] - [[cr:glossarycn#e|E]] - [[cr:glossarycn#f|F]] - [[cr:glossarycn#g|G]] - [[cr:glossarycn#h|H]] - [[cr:glossarycn#j|J]] - [[cr:glossarycn#k|K]] - [[cr:glossarycn#l|L]] - [[cr:glossarycn#m|M]] - [[cr:glossarycn#n|N]] - [[cr:glossarycn#o|O]] - [[cr:glossarycn#p|P]] - [[cr:glossarycn#q|Q]] - [[cr:glossarycn#r|R]] - [[cr:glossarycn#s|S]] - [[cr:glossarycn#t|T]] - [[cr:glossarycn#w|W]] - [[cr:glossarycn#x|X]] - [[cr:glossarycn#y|Y]] - [[cr:glossarycn#z|Z]]</WRAP>
----

{content}
----
{{{{page>:规则和文档索引&nofooter}}}}
"""

GLOSSARY_ALPHABET_TEMPLATE = """[[:完整规则|返回完整规则目录]]
====== 词汇表（按英文首字母排序） ======
<WRAP centeralign>
[[cr:glossary#a|A]] - [[cr:glossary#b|B]] - [[cr:glossary#c|C]] - [[cr:glossary#d|D]] - [[cr:glossary#e|E]] - [[cr:glossary#f|F]] - [[cr:glossary#g|G]] - [[cr:glossary#h|H]] - [[cr:glossary#i|I]] - [[cr:glossary#k|K]] - [[cr:glossary#l|L]] - [[cr:glossary#m|M]] - [[cr:glossary#n|N]] - [[cr:glossary#o|O]] - [[cr:glossary#p|P]] - [[cr:glossary#r|R]] - [[cr:glossary#s|S]] - [[cr:glossary#t|T]] - [[cr:glossary#u|U]] - [[cr:glossary#v|V]] - [[cr:glossary#w|W]] - [[cr:glossary#x|X]] - [[cr:glossary#y|Y]] - [[cr:glossary#z|Z]]</WRAP>
----

{content}
----
{{{{page>:规则和文档索引&nofooter}}}}
"""

CREDITS_TEMPLATE = """[[:完整规则|返回完整规则目录]]

====== 版权信息 ======
{content}
"""

CATALOG_TEMPLATE = """<nowiki>
这是目录页的主要部分。将这部分内容和catalog_instruction.txt组合成完整的目录页。
</nowiki>
===== 目录 =====
//{effective_time}//

[[CR:Intro|前言]]

{content}

词汇表 Glossary - [[CR:Glossary|按英文首字母排序]] | [[CR:Glossarycn|按拼音首字母排序]]

[[CR:credits|版权信息]]

  * [[CR:TranslatedTerms|暂译名称列表]]
  * [[cr:updates:index|CR更新摘要索引]]

{{{{page>规则和文档索引&nofooter}}}}"""