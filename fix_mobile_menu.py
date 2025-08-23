import os
import re

def fix_html_files():
    # Get all HTML files in the current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'footer.html']
    
    # Pattern to match the problematic JavaScript block
    pattern = r'''  
  const menuToggle = document\.getElementById\('menu-toggle'\);
  const menu = document\.querySelector\('nav ul\.menu'\);

  menuToggle\.addEventListener\('click', \(\) => \{
    menu\.classList\.toggle\('active'\);
    menuToggle\.querySelector\('i'\)\.classList\.toggle\('fa-bars'\);
    menuToggle\.querySelector\('i'\)\.classList\.toggle\('fa-times'\);
  \}\);

  // Mobile dropdown functionality
  document\.addEventListener\('DOMContentLoad(ed|ing)', function\(\) \{
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
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove the problematic JavaScript block
            new_content = re.sub(pattern, '', content, flags=re.DOTALL)
            
            # If content changed, write it back
            if new_content != content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed {html_file}")
            else:
                print(f"No changes needed for {html_file}")
                
        except Exception as e:
            print(f"Error processing {html_file}: {e}")

if __name__ == "__main__":
    fix_html_files()
