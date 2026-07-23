import os, json, re

gemini_k = os.environ['GEMINI_K']

with open('dist/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('__GEMINI_K__', gemini_k)

with open('guide-data.json', 'r', encoding='utf-8') as f:
    guide = f.read()

new_block = '/* __DATA_START__ */\nconst EMBEDDED_DATA = ' + guide + '\n/* __DATA_END__ */'
c = re.sub(r'/\* __DATA_START__ \*/.*?/\* __DATA_END__ \*/', new_block, c, flags=re.DOTALL)

with open('spell-data.json', 'r', encoding='utf-8') as f:
    spell = f.read()

new_spell_block = '/* __SPELL_START__ */\nconst SPELL_DATA = ' + spell + '\n/* __SPELL_END__ */'
c = re.sub(r'/\* __SPELL_START__ \*/.*?/\* __SPELL_END__ \*/', new_spell_block, c, flags=re.DOTALL)

with open('dist/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
