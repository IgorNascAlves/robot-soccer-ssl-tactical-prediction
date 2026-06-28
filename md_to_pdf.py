import markdown
from weasyprint import HTML

md_file = 'docs/proposta_projeto.md'
pdf_file = 'docs/proposta_projeto.pdf'

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
    body {{
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 40px;
        color: #333;
    }}
    h1 {{
        color: #2c3e50;
        text-align: center;
        border-bottom: 2px solid #ecf0f1;
        padding-bottom: 10px;
    }}
    h2 {{
        color: #34495e;
        margin-top: 30px;
    }}
    p {{
        text-align: justify;
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
