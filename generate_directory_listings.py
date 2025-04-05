import os
import json

def create_index_html(current_dir, parent_path=''):
    # Get all directories and files in the current directory
    items = os.listdir(current_dir)
    
    # Filter out hidden files and .git directory
    items = [item for item in items if not item.startswith('.') and item != 'index.html']
    
    # Separate directories and files
    directories = []
    files = []
    
    for item in items:
        full_path = os.path.join(current_dir, item)
        if os.path.isdir(full_path):
            directories.append(item)
        else:
            files.append(item)
    
    # Sort both lists
    directories.sort()
    files.sort()
    
    # Create the HTML content
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing - {os.path.basename(current_dir)}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #333;
            margin-bottom: 1rem;
            text-align: center;
        }}
        .breadcrumb {{
            margin-bottom: 2rem;
            text-align: center;
            color: #666;
        }}
        .breadcrumb a {{
            color: #0366d6;
            text-decoration: none;
        }}
        .breadcrumb a:hover {{
            text-decoration: underline;
        }}
        .directory-list {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 1rem;
        }}
        .list-section {{
            margin-bottom: 1.5rem;
        }}
        .list-section h2 {{
            color: #333;
            font-size: 1.2rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eee;
        }}
        .item {{
            display: flex;
            align-items: center;
            padding: 0.75rem;
            border-bottom: 1px solid #eee;
            transition: background-color 0.2s;
        }}
        .item:last-child {{
            border-bottom: none;
        }}
        .item:hover {{
            background-color: #f8f9fa;
        }}
        .icon {{
            margin-right: 1rem;
            color: #666;
        }}
        .name {{
            color: #0366d6;
            text-decoration: none;
            font-weight: 500;
        }}
        .name:hover {{
            text-decoration: underline;
        }}
        .search-box {{
            width: 100%;
            padding: 0.75rem;
            margin-bottom: 1rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }}
        .search-box:focus {{
            outline: none;
            border-color: #0366d6;
            box-shadow: 0 0 0 3px rgba(3,102,214,0.1);
        }}
    </style>
</head>
<body>
    <h1>{os.path.basename(current_dir)}</h1>
    <div class="breadcrumb">
        <a href="/">root</a>
        {parent_path}
    </div>
    <input type="text" class="search-box" placeholder="Search items..." id="searchInput">
    <div class="directory-list" id="directoryList">
        <div class="list-section">
            <h2>Directories</h2>
            {''.join(f'<div class="item"><span class="icon">📁</span><a href="./{dir}/" class="name">{dir}</a></div>' for dir in directories)}
        </div>
        <div class="list-section">
            <h2>Files</h2>
            {''.join(f'<div class="item"><span class="icon">📄</span><a href="./{file}" class="name">{file}</a></div>' for file in files)}
        </div>
    </div>

    <script>
        const searchInput = document.getElementById('searchInput');
        const items = document.querySelectorAll('.item');
        
        searchInput.addEventListener('input', (e) => {{
            const searchTerm = e.target.value.toLowerCase();
            
            items.forEach(item => {{
                const name = item.querySelector('.name').textContent.toLowerCase();
                if (name.includes(searchTerm)) {{
                    item.style.display = 'flex';
                }} else {{
                    item.style.display = 'none';
                }}
            }});
        }});
    </script>
</body>
</html>'''
    
    # Write the index.html file
    with open(os.path.join(current_dir, 'index.html'), 'w') as f:
        f.write(html_content)
    
    # Recursively process subdirectories
    for dir_name in directories:
        subdir = os.path.join(current_dir, dir_name)
        new_parent_path = f' / <a href="../">{os.path.basename(current_dir)}</a>'
        create_index_html(subdir, new_parent_path)

# Start from the current directory
base_dir = os.path.dirname(os.path.abspath(__file__))
create_index_html(base_dir) 