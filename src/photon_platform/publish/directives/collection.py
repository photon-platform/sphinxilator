import os
from functools import partial
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives
from docutils import nodes
from sphinx.jinja2glue import SphinxFileSystemLoader
from jinja2 import Environment
from sphinx.addnodes import toctree

class CollectionDirective(SphinxDirective):
    has_content = False
    option_spec = {
        'type': directives.unchanged,
        'sort': directives.unchanged,
        'reverse': directives.flag,
        'template': directives.unchanged,
        'limit': directives.positive_int,
        'title': directives.unchanged,
    }

    def run(self) -> list:
        """
        Process the collection directive, discover and sort documents,
        and render them using a Jinja2 template.
        """
        env = self.env
        
        collection_type = self.options.get('type')
        sort_key = self.options.get('sort')
        reverse = 'reverse' in self.options
        template_name = self.options.get('template', '_macros/collection.html')
        limit = self.options.get('limit')
        title = self.options.get('title', 'Collection')

        # Discover files automatically
        current_dir = os.path.dirname(env.docname)
        docnames = []
        walk_path = os.path.join(env.srcdir, current_dir)
        for dirpath, _, filenames in os.walk(walk_path):
            for filename in filenames:
                if filename.endswith('.rst'):
                    full_path = os.path.join(dirpath, filename)
                    # Convert to docname format (relative to srcdir, no extension)
                    docname = os.path.splitext(os.path.relpath(full_path, env.srcdir))[0]
                    # Exclude the current document itself
                    if docname != env.docname:
                        docnames.append(docname)

        collection_items = []
        for docname in docnames:
            meta = env.metadata.get(docname, {})
            if not collection_type or meta.get('type') == collection_type:
                title_node = env.titles.get(docname)
                if title_node:
                    item = {
                        'title': title_node.astext(),
                        'docname': docname,
                    }
                    item.update(meta)
                    collection_items.append(item)

        if sort_key:
            collection_items.sort(key=lambda x: x.get(sort_key, 0), reverse=reverse)

        if limit:
            collection_items = collection_items[:limit]

        pathto = partial(self.env.app.builder.get_relative_uri, self.env.docname)
        context = {
            'collection': {
                'title': title,
                'articles': collection_items,
            },
            'pathto': pathto,
        }

        # Render the template
        jinja_env = self.env.app.builder.templates.environment
        template = jinja_env.get_template(template_name)
        html = template.render(context)
        
        # Create a hidden toctree
        toc = toctree()
        toc['glob'] = False
        toc['hidden'] = True
        toc['includefiles'] = docnames
        toc['entries'] = [(None, docname) for docname in docnames]
        
        return [nodes.raw('', html, format='html'), toc]

def build_nav_links(app, pagename: str, templatename: str, context: dict, doctree) -> None:
    """Build navigation links from document metadata and add them to the context."""
    header_nav_list = []
    footer_nav_list = []
    recent_logs = []
    for docname in app.env.found_docs:
        meta = app.env.metadata.get(docname, {})
        if meta.get('navigation') == 'header':
            title = app.env.titles.get(docname)
            if title:
                header_nav_list.append({
                    'docname': docname,
                    'title': title.astext(),
                    'order': meta.get('order', 0),
                })
        if meta.get('navigation') == 'footer':
            title = app.env.titles.get(docname)
            if title:
                footer_nav_list.append({
                    'docname': docname,
                    'title': title.astext(),
                    'order': meta.get('order', 0),
                })
        if meta.get('type') == 'log':
            title = app.env.titles.get(docname)
            if title:
                recent_logs.append({
                    'docname': docname,
                    'title': title.astext(),
                    'date': meta.get('date', ''),
                })

    # Sort the navigation list by the 'order' metadata field
    header_nav_list.sort(key=lambda x: x['order'])
    context['header_nav_list'] = header_nav_list

    # Sort the footer navigation list by the 'order' metadata field
    footer_nav_list.sort(key=lambda x: x['order'])
    context['footer_nav_list'] = footer_nav_list

    # Sort the recent logs list by date
    recent_logs.sort(key=lambda x: x['date'], reverse=True)
    context['recent_logs'] = recent_logs[:5]

def setup(app) -> dict:
    """Register the collection directive and connect the build_nav_links function."""
    app.add_directive("collection", CollectionDirective)
    app.connect('html-page-context', build_nav_links)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
