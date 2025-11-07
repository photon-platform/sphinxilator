import sass
import os

Compiles the SASS files for the publish theme.
"""
import os
import sass

scss_dir = os.path.join(os.path.dirname(__file__), '..', 'themes', 'publish_theme', 'static', 'scss')
css_dir = os.path.join(os.path.dirname(__file__), '..', 'themes', 'publish_theme', 'static', 'css')

if not os.path.exists(css_dir):
    os.makedirs(css_dir)

scss_file = os.path.join(scss_dir, 'photon.scss')
css_file = os.path.join(css_dir, 'publish.css')

with open(css_file, 'w') as f:
    f.write(sass.compile(filename=scss_file))

if __name__ == '__main__':
    build_sass()
