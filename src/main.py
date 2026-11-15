import os
from copystatic import (prepare_destination,copy_files_recursive)
from gencontent import (generate_page, generate_pages_recursive)


def main():
    source = "static"
    destination = "public"
    prepare_destination(destination)
    copy_files_recursive(source,destination)
    dir_path_static = "./static"
    dir_path_public = "./public"
    dir_path_content = "./content"
    template_path = "./template.html"

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"))

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)




if __name__ == "__main__":
    main()
