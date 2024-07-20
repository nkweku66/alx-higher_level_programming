#!/usr/bin/bash
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str = str.split(" ")
str = str[5:8]
str = " ".join(str) + " with python"
print(str)
