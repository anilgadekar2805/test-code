import re

files = [
    'Anil.Gadekar.22.20240419000000',
    'Raj.Gade.22.20240419000000.NOK',
    'Alan.marks.DDPP.21202404'
]

pattern = re.compile(r'\.\d{17}(?=\D|$)')

trimmed_files = [pattern.sub('', file) for file in files]

print(trimmed_files)



import re

files = [
    'Anil.Gadekar.22.20240419000000',
    'Raj.Gade.22.20240419000000.NOK',
    'Alan.marks.DDPP.21202404'
]

pattern = re.compile(r'(\.\d{17}|\.NOK)(?=\D|$)')

trimmed_files = [pattern.sub('', file) for file in files]

print(trimmed_files)

