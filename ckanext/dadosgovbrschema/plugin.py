import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

# Custom helper
from ckanext.dadosgovbrschema import helpers

class DadosgovbrschemaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'dadosgovbrschema')

    
    # Registro dos helpers
    # =======================================================
    def get_helpers(self):
        '''Register all functions

        '''
        
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {
            # Scheming
            'dadosgovbr_get_schema_name': helpers.scheming.get_schema_name,
            'dadosgovbr_get_schema_title': helpers.scheming.get_schema_title
        }
        