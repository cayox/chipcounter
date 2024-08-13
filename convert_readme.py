import markdown

markdown.markdownFromFile(
    input="README.md", output="index.html", extensions=["markdown.extensions.tables"]
)
