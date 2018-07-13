from base64_substring import *
from itertools import chain

print("please enter a rule name:")
rule_name = input()

print("please enter a text:")

input_str = input()
bytearr_ascii = get_padded_ascii(input_str)
bytearr_unicode = get_padded_unicode(input_str)
	
substrings = chain(get_base64_substr(bytearr_ascii), get_base64_substr(bytearr_unicode, 2))

yara_template = """
rule {name}
{{
	strings:
		{rules}

	condition:
		1 of them
}}

"""
strings_section = ""

for index, substr in enumerate(substrings):
	strings_section += '$ = "{}"\n\t\t'.format(substr)
	
print(yara_template.format(name=rule_name, rules= strings_section))