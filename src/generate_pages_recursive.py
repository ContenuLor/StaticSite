import os
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node
from pathlib import Path

# 2. Change your main function to use generate_pages_recursive instead of generate_page. 
# You should generate a page for every markdown file in the content directory and write the results to the public directory.
# 3. Run the new program and ensure that both pages on the site are generated correctly and you can navigate between them.

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # 1.1. Crawl every entry in the content directory
    #check all files in the content directory check if they are markdown files
    for item in os.listdir(path=dir_path_content):
        #if item is folder:
        if os.path.isdir(os.path.join(dir_path_content,item)):
            generate_pages_recursive(os.path.join(dir_path_content,item), template_path, os.path.join(dest_dir_path,item), basepath)
        if item.endswith(".md"):
            from_path = os.path.join(dir_path_content,item)
            
            temp_dest_path = os.path.join(dest_dir_path,item)
            html_dest_path = Path(temp_dest_path)
            dest_path = html_dest_path.with_suffix('.html')


            # 1.2. For each markdown file found, generate a new .html file using the same template.html. 
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

            #replacing the href and src attributes in the final_html with the basepath
            final_html = final_html.replace('href="/', f'href="{basepath}')
            final_html = final_html.replace('src="/', f'src="{basepath}')
            
            #Checking if the destination directory exists
            if os.path.exists(path=dest_dir_path) == False:
                #create the directory if it doesn't exist
                os.makedirs(dest_dir_path)

            # Write the new full HTML page to a file at dest_path.
            with open(dest_path, 'w') as f:
                f.write(final_html)
