"""
CP1404/CP5632 Practical - Roderick Mabo
Programming Language Program

"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [java, python, visual_basic]

    print('The dynamically typed languages are:')
    for language in languages:
        if language.is_dynamic():
            print(language.name)



main()

