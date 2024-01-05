import re
import sys

post = sys.stdin.read()

re.compile(r'')
sql_keywords = len(re.findall(r"(select|from|where) ", post, flags=re.IGNORECASE))
backticked_code_blocks = len(re.findall(r"^```", post))
inline_code_snippets = len(re.findall(r"`", post)) // 2
indented_code_lines = len(re.findall(r"^    (SELECT|FROM|import|duckdb|library)", post))

print(f"sql keywords: {sql_keywords}")

if backticked_code_blocks == 0 and backticked_code_blocks == 0 and inline_code_snippets == 0 and sql_keywords > 0:
    exit(1)
