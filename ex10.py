# -*- coding: utf-8 -*-
# learn "escape sequences" 转义字符 \
tabby_cat = "\tI'm tabbled in." # \t代表制表符，为四个空格
persian_cat = "I'm split\non a line." # \n 代表换行
backslash_cat = "I'm \\ a \\ cat."  # 转义两个反斜杠

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# 使用 triple-single-quote和triple-double-quote ,效果一样
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# If you use \U or \u then you'll need to use a unicode string in u'\U0001F47E'.
# Put a u in front of the '' (single-quotes) or "" (double-quotes).
#    Escape	 What  it  does.
#    \\	                 Backslash (\)
#    \'	                 Single-quote (')
#    \"	                Double-quote (")
#    \a	                ASCII bell (BEL)
#    \b	                ASCII backspace (BS)
#    \f	                 ASCII formfeed (FF)
#    \n	                ASCII linefeed (LF)
#    \N{name}	 Character named name in the Unicode database (Unicode only)
#    \r	                Carriage Return (CR)
#    \t	                Horizontal Tab (TAB)
#    \uxxxx	        Character with 16-bit hex value xxxx (u'' string only)
#    \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (u'' string only)
#    \v	               ASCII vertical tab (VT)
#    \ooo	        Character with octal value ooo
#    \xhh	        Character with hex value hh
# Always remember this: %r is for debugging, %s is for displaying.
