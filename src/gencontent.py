import os

from markdown_blocks import markdown_to_html_node
from pathlib import Path



def extract_title(md: str) -> str:
    lines = md.split("\n") # Takes the markdown file and splits it into lines so text output isn't one continuous line of text. #
    for line in lines:
        if line.startswith("# "): # If loop that is looking for the <h1>/<title> that is found at the first "#". #
            return line[2:] # [2:]Is the first position of the list that hold 1-6 of #. The first position is #, the <h1>/<title>. #
    raise ValueError("no title found") # Error is raised if the [2:] or <h> isn't what's being found. #



def generate_page(from_path: str, template_path: str, dest_path: Path) -> None:
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r") # This variable that uses the "open" method to open the desired path for reading. #
    markdown_content = from_file.read() # This variable takes file above & uses the read.() method to save it. #
    from_file.close() # Closes the file, not sure why, Boots wrote this one. #

    template_file = open(template_path, "r") # Same open process as the file opening variable above. #
    template = template_file.read() # Same reading process the path reading variable above. #
    template_file.close()

    node = markdown_to_html_node(markdown_content) # Making a node out of the markdown_content variable above. #
    html = node.to_html() # Converting the markdown node directly above into an html string. #

    title = extract_title(markdown_content) # Passes the markdown_content through the extract_title function
    template = template.replace("{{ Title }}", title) # This replaces the { Title } placeholder in the template title. #
    template = template.replace("{{ Content }}", html) # This replaces the { Content } placeholder in the template html. #

    dest_dir_path = os.path.dirname(dest_path) # Returns the directory name of the pathname path.
    if dest_dir_path != "": # Contigent if loop to create the directory in the event the directory doesn't exist. #
        os.makedirs(dest_dir_path, exist_ok=True) # How the directory is made. #
    to_file = open(dest_path, "w") # Opening the destination path in write mode. #
    to_file.write(template) # Applies the template variable from above that reads/saves the file. Then with .write(), it writes the file information into the destination path. #



def generate_pages_recursive(dir_path_content,template_path,dest_dir_path):
    for filename in os.listdir(dir_path_content): # For loop to crawl every entry in the content directory. The directory is first being listed. #
        from_path = os.path.join(dir_path_content, filename) # Creates a new path by joining the path from the content directory. #
        dest_path = os.path.join(dest_dir_path, filename) # Creates a new path by joining the path from the destination directory. #
        if os.path.isfile(from_path): # If loop to check if the from_path or content directory path is a file. #
            dest_path = Path(dest_path).with_suffix(".html") # If the content directory does contain the html file, it will create an html file for the destination path. #
            generate_page(from_path, template_path, dest_path) # Since the conditions are met, the generate_page function will be ran. #
        else:
            generate_pages_recursive(from_path, template_path, dest_path) # The function will keep calling itself, going one directory deeper until it bottoms out an actual file. #
