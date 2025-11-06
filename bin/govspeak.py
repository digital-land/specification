"""
Render Govspeak markdown

Provides markdown rendering with GOV.UK-specific extensions including:
- Call-to-action blocks ($CTA...$CTA)
- Information callouts (^...^)
- Warning callouts (%...%)
- Numbered steps (s1., s2., etc.)
- Email address links (<email@example.com>)
"""

import re
import markdown
from markdown.extensions.toc import TocExtension
from markdown.extensions.tables import TableExtension


def render_markdown(content):
    """
    Render markdown content to HTML with govspeak extensions.

    Args:
        content: Markdown content string

    Returns:
        Rendered HTML string with GOV.UK classes
    """
    # Extract CTA blocks and store them with placeholders
    cta_blocks = []
    cta_counter = [0]

    def extract_cta(match):
        cta_content = match.group(1).strip()
        # Use HTML comment as placeholder to avoid markdown processing
        placeholder = f"<!-- CTA-PLACEHOLDER-{cta_counter[0]} -->"
        cta_blocks.append(cta_content)
        cta_counter[0] += 1
        return placeholder

    content = re.sub(
        r"\$CTA\s*\n(.*?)\n\$CTA", extract_cta, content, flags=re.DOTALL | re.MULTILINE
    )

    # Convert govspeak information callouts (^...^)
    def convert_info(match):
        info_content = match.group(1).strip()
        return f'<div class="information-callout">\n<p>{info_content}</p>\n</div>'

    content = re.sub(r"\^(.*?)\^", convert_info, content, flags=re.DOTALL)

    # Convert govspeak warning callouts (%...%)
    def convert_warning(match):
        warning_content = match.group(1).strip()
        return f'<div class="warning-callout">\n<p>{warning_content}</p>\n</div>'

    content = re.sub(r"%(.*?)%", convert_warning, content, flags=re.DOTALL)

    # Convert govspeak steps to HTML
    def convert_steps(match):
        steps_text = match.group(0)
        lines = steps_text.strip().split("\n")
        html = '<ol class="govuk-list govuk-list--number steps">\n'
        for line in lines:
            step_match = re.match(r"s\d+\.\s+(.*)", line)
            if step_match:
                html += f'  <li>{step_match.group(1)}</li>\n'
        html += "</ol>"
        return html

    # Match govspeak step lists (s1., s2., s3., etc.)
    content = re.sub(
        r"(?:^s\d+\..*$\n?)+", convert_steps, content, flags=re.MULTILINE
    )

    # Convert email addresses in angle brackets to mailto links
    def convert_email(match):
        email = match.group(1)
        return f'<a href="mailto:{email}" class="govuk-link">{email}</a>'

    content = re.sub(
        r"<([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>",
        convert_email,
        content,
    )

    md = markdown.Markdown(
        extensions=[
            "extra",
            "nl2br",
            "sane_lists",
            TocExtension(permalink=False),
            TableExtension(),
        ]
    )
    html_content = md.convert(content)

    # Replace CTA placeholders with rendered markdown in CTA divs
    for i, cta_content in enumerate(cta_blocks):
        # Create a new markdown instance for CTA content
        md_cta = markdown.Markdown(
            extensions=[
                "extra",
                "nl2br",
                "sane_lists",
            ]
        )
        cta_html = md_cta.convert(cta_content)
        placeholder = f"<!-- CTA-PLACEHOLDER-{i} -->"
        cta_div = f'<div class="call-to-action">\n{cta_html}\n</div>'

        # Replace the HTML comment placeholder
        html_content = html_content.replace(placeholder, cta_div)

    return html_content
