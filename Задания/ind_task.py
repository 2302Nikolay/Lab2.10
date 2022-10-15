#!/usr/bin/env python3
# -*- coding: utf-8 -*

def print_prog_lang(**lang):
    st = "-" * 40
    print("Programming languages: \n")
    print(st)
    for field, lng in lang.items():
        print(f"{field}:", " "*(10-len(field)), '|', lng)
        print(st)


if __name__ == "__main__":
    print_prog_lang(
        Science=["C++", "Fortran", "Java"],
        AI=["Python", "Prolog", "LISP"],
        Gamedev="C#"
    )
