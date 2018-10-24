# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:11:12 2018

@author: mfulghum
"""

from collections import Counter

ciphertext = 'JM BFD YNIHXFBM XSO MSA EYU LDYO BFHK IM VLHDUO H YI HICLDKKDO RDLM PDNN OSUD MSAL KSNABHSU TDM HK OLFJNOCXVLLH BFHK NHBBND EFYNNDUXD PYK USB BSS FYLO PYK HB'
print(ciphertext)
substitution = {
    'A':'u',
    'B':'t',
    'C':'p',
    'D':'e',
    'E':'c',
    'F':'h',
    'G':'G',
    'H':'i',
    'I':'m',
    'J':'b',
    'K':'s',
    'L':'r',
    'M':'y',
    'N':'l',
    'O':'d',
    'P':'w',
    'Q':'Q',
    'R':'v',
    'S':'o',
    'T':'k',
    'U':'n',
    'V':'f',
    'W':'W',
    'X':'g',
    'Y':'a',
    'Z':'Z',
    ' ':' '}
print(''.join([substitution[ch] for ch in ciphertext]))
