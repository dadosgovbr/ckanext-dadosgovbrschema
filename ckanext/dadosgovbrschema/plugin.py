import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

# Custom helper
from ckanext.dadosgovbrschema import helpers

class DadosgovbrschemaPlugin(plugins.SingletonPlugin):

    # IConfigurer
    # =======================================================
    plugins.implements(plugins.IConfigurer)
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'dadosgovbrschema')

    
    # Mapeamento das URLs
    # =======================================================
    plugins.implements(plugins.IRoutes)
    def scheming_get_types(self):
        return ['concurso', 'aplicativo', 'inventario']
    def before_map(self, map):
        # ckanext-scheming
        # New packages formats
        for package_type in self.scheming_get_types():
            map.connect('%s_new' % package_type, '/%s/new' % package_type,
                            controller='package', action='new')
            map.connect('/%s/{id}' % package_type,
                        controller='ckanext.dadosgovbrschema.controllers.scheming:SchemingPagesController',
                        action='read',
                        id='id')
            map.connect('/%ss' % package_type,
                        controller='ckanext.dadosgovbrschema.controllers.scheming:SchemingPagesController',
                        action='search')
        return map
    def after_map(self, map):
        return map

    # Registro dos helpers
    # =======================================================
    plugins.implements(plugins.ITemplateHelpers)
    def get_helpers(self):
        '''Register all functions

        '''

        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {
            # Scheming
            'dadosgovbrschema_get_schema_name': helpers.scheming.get_schema_name,
            'dadosgovbrschema_get_schema_title': helpers.scheming.get_schema_title
        }
        