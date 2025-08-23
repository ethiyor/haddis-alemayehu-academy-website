import os
import re

files_to_fix = [
    'faculty.html',
    'facilities.html', 
    'alumni.html',
    'alumni-network.html',
    'alumni-achievements.html'
]

# The pattern we want to remove (the conflicting JS)
js_pattern = r'''    
    const menuToggle = document\.getElementById\('menu-toggle'\);
    const menu = document\.querySelector\('nav ul\.menu'\);

    menuToggle\.addEventListener\('click', \(\) => \{
      menu\.classList\.toggle\('active'\);
      menuToggle\.querySelector\('i'\)\.classList\.toggle\('fa-bars'\);
      menuToggle\.querySelector\('i'\)\.classList\.toggle\('fa-times'\);
    \}\);

    // Mobile dropdown functionality
    document\.addEventListener\('DOMContentLoaded', function\(\) \{
      const dropdowns = document\.querySelectorAll\('\.dropdown'\);
      
      dropdowns\.forEach\(dropdown => \{
        dropdown\.addEventListener\('click', function\(e\) \{
          if \(window\.innerWidth <= 768\) \{
            e\.preventDefault\(\);
            this\.classList\.toggle\('active'\);
          \}
        \}\);
      \}\);
    \}\);'''

for file in files_to_fix:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the JS pattern
        new_content = re.sub(js_pattern, '', content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {file}")
        else:
            print(f"No pattern found in {file}")
    else:
        print(f"File {file} not found")
