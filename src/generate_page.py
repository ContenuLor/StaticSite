from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path,template_path, dest_path):
    print (f'Generating page from {from_path} to {dest_path} using {template_path}')

    #store content in a variable
    with open(from_path, 'r') as f:
        content_text = f.read()

    #store template in a variable
    with open(template_path, 'r') as f:
        template_text = f.read()

    #Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    html_content = markdown_to_html_node(content_text)
    html_string = html_content.to_html()

    # Use the extract_title function to grab the title of the page.
    title = extract_title(content_text)

    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    final_html = template_text.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    
    # Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    with open(dest_path, 'w') as f:
        f.write(final_html)