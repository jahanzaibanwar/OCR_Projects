# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from textblob import TextBlob

text = u"おはようございます。"
tb = TextBlob(text)
translated = tb.translate(to="en")
print(translated)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
