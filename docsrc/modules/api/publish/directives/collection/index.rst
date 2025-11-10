publish.directives.collection
=============================

.. py:module:: publish.directives.collection


Classes
-------

.. autoapisummary::

   publish.directives.collection.CollectionDirective


Functions
---------

.. autoapisummary::

   publish.directives.collection.build_nav_links
   publish.directives.collection.setup


Module Contents
---------------

.. py:class:: CollectionDirective(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)

   Bases: :py:obj:`sphinx.util.docutils.SphinxDirective`


   A base class for Sphinx directives.

   This class provides helper methods for Sphinx directives.

   .. versionadded:: 1.8

   .. note:: The subclasses of this class might not work with docutils.
             This class is strongly coupled with Sphinx.


   .. py:attribute:: has_content
      :value: False


      May the directive have content?



   .. py:attribute:: option_spec

      Mapping of option names to validator functions.



   .. py:method:: run() -> list

      Process the collection directive, discover and sort documents,
      and render them using a Jinja2 template.



.. py:function:: build_nav_links(app, pagename: str, templatename: str, context: dict, doctree) -> None

   Build navigation links from document metadata and add them to the context.


.. py:function:: setup(app) -> dict

   Register the collection directive and connect the build_nav_links function.


