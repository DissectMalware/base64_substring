# About
Often malware analysts require to search through base64-encoded samples with a search term such as Application.Run. base64_substring helps them by enumerating all possible base64 encoding for a given search term and generating a yara rule that checks those possiblities.

# How to Run
Example: generating a yara rule that matches base64-encoded file containing *Application* term.
```
> python generate_yara_rule.py
> Please enter a rule name
  MyRule
> Please enter a text
  Application
```
  

# Further Reading
["Searching for Content in Base-64 Strings" by Lee Holmes](http://www.leeholmes.com/blog/2017/09/21/searching-for-content-in-base-64-strings/)
