# Toon3D Dataset

## Directory Listing

This repository uses a custom directory listing system for GitHub Pages. The directory listings are generated using a Python script that creates `index.html` files in each directory.

### Regenerating Directory Listings

If you make changes to the directory structure (adding/removing files or folders), you'll need to regenerate the directory listings. To do this:

1. Make sure you have Python 3 installed
2. Run the following command from the root of the repository:
   ```bash
   python3 generate_directory_listings.py
   ```

This will:
- Create/update `index.html` files in all directories
- Generate a clean, modern directory listing interface
- Include search functionality and breadcrumb navigation
- Show both files and directories with appropriate icons

The generated directory listings will work with GitHub Pages and provide a consistent navigation experience throughout the repository.
