# Ivan Gontchar
# Belugas
# SoftDev
# K04 -- Python Random Selection & Dictionaries
# 2024-9-13
# Time Spent: 10
import random

krewes = {
    4: [
        'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
    ],
    5: [
        'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
        'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
        'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
        'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN'
    ]
}

value = random.choice(list(krewes.values()))
print(random.choice(value))
