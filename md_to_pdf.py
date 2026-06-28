import markdown
from weasyprint import HTML

md_file = 'docs/proposta_projeto.md'
pdf_file = 'docs/proposta_projeto_dark.pdf'

with open(md_file, 'r', encoding='utf-8') as f:
    text = f.read()

html = markdown.markdown(text)

# Add basic styling
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    @page {{ 
        margin: 1.2cm; 
        background-color: #121212;
    }}
    body {{
        font-family: Arial, sans-serif;
        line-height: 1.25;
        font-size: 10.5pt;
        background-color: #121212;
        color: #e0e0e0;
    }}
    h1 {{
        color: #ffffff;
        text-align: center;
        border-bottom: 2px solid #333333;
        padding-bottom: 5px;
        margin-bottom: 10px;
        font-size: 16pt;
    }}
    h2 {{
        color: #cccccc;
        margin-top: 15px;
        margin-bottom: 5px;
        font-size: 13pt;
    }}
    a {{
        color: #82aaff;
    }}
    p {{
        text-align: justify;
        margin-top: 5px;
        margin-bottom: 5px;
    }}
</style>
</head>
<body>
{html}
</body>
</html>
"""

HTML(string=html_content).write_pdf(pdf_file)
print("PDF created successfully!")
