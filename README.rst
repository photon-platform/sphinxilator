sphinxilator
============


> all the tools and themes for publishing with Sphinx

sphinxilator is a consolidated repository designed to streamline and enhance
the Sphinx documentation framework across various projects. It integrates
custom components, themes, and configurations into a unified system,
facilitating easier management and deployment of documentation websites. This
repository includes a global configuration setup, allowing for dynamic
adjustments per project, and a robust integration of converted Grav themes
using Jinja templates. Additionally, sphinxilator extends Ablog to support
diverse content types like events and tasks, making it a versatile tool for any
Sphinx-based documentation needs.


Features
--------

- **Dynamic Configuration**: Utilizes a global `conf.py` that can be imported into local configurations for dynamic, project-specific settings.

- **Template Conversion**: Includes tools and guidelines for converting Grav Twig templates into Jinja, ensuring seamless integration with Sphinx.

- **Integrated Styles and Scripts**: Supports the incorporation of custom CSS and JavaScript from Grav themes into Sphinx projects, maintaining a consistent look and feel across documentation sites.

- **Enhanced Ablog**: Modifies Ablog to handle a wider array of content types, including events, tasks, and updates, alongside traditional blog posts.

- **Modular Design**: Designed to be flexible and modular, allowing for easy adaptations and extensions to meet the specific needs of various documentation projects.

- **Streamlined Project Integration**: Provides a structured approach for integrating `sphinxilator` into existing and new Sphinx projects, ensuring consistency and efficiency in documentation deployment.

- **Content Organization**: Includes a CLI tool to help organize content, especially for code documentation, by scanning the `src` directory and generating RST stubs for modules.


Installation
------------

You can install **sphinxilator** using pip:

.. code-block:: bash

   pip install photon-platform-sphinxilator

Usage
-----

After installation, you can use the ``sphinxilator`` command to manage your documentation projects:

.. code-block:: bash

   sphinxilator new  # create a new documentation project
   sphinxilator build  # build the documentation for a project
   sphinxilator deploy  # deploy the documentation to GitHub Pages
   sphinxilator organize  # organize content, especially for code documentation

Dependencies
------------

**sphinxilator** depends on the following Python packages:

.. todo:: TODO: read from pyproject.toml 

Contributing
------------

Contributions are welcome! Please see our [GitHub issues](https://github.com/photon-platform/sphinxilator/issues) for ways to contribute.

License
-------

**sphinxilator** is licensed under the MIT License. See the `LICENSE` file for more details.
