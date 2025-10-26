import sass
import os

def build_sass():
    """
    Compiles the SASS files for the sphinxilator theme.
    """
    scss_dir = os.path.join(os.path.dirname(__file__), '..', 'themes', 'sphinxilator_theme', 'static', 'scss')
    css_dir = os.path.join(os.path.dirname(__file__), '..', 'themes', 'sphinxilator_theme', 'static', 'css')
    
    if not os.path.exists(css_dir):
        os.makedirs(css_dir)
        
    scss_file = os.path.join(scss_dir, 'photon.scss')
    css_file = os.path.join(css_dir, 'sphinxilator.css')
    
    with open(scss_file, 'r') as f_in, open(css_file, 'w') as f_out:
        css = sass.compile(string=f_in.read(), include_paths=[scss_dir])
        f_out.write(css)

if __name__ == '__main__':
    build_sass()
