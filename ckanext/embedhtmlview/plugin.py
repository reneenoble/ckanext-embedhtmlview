import ckan.plugins as p
import ckan.plugins.toolkit as toolkit
ignore_empty = p.toolkit.get_validator('ignore_empty')

class EmbedhtmlviewPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IConfigurable, inherit=True)
    if p.toolkit.check_ckan_version('2.3'):
        p.implements(p.IResourceView, inherit=True)
    else:
    	p.implements(p.IResourcePreview, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'embedhtmlview')

    def configure(self, config):
        enabled = config.get('ckan.resource_proxy_enabled', False)
        self.proxy_is_enabled = enabled

    def can_preview(self, data_dict):
        if resource.get('on_same_domain') or self.proxy_is_enabled:
            return {'can_preview': True, 'quality': 2}
        else:
            return {'can_preview': True,
                    'fixable': 'Enable resource_proxy',
                    'quality': 2}
    def info(self): return {'name': 'embed_script_view', 
                            'title': 'Embed Script View', 
                            'always_available': True, 
                            'default_title': 'Embed Script View', 
                            'icon': 'picture',
                            'schema': {'script_contents': [ignore_empty, unicode]},
                            'iframed': False,
                            'always_available': True,
                            }

    def can_view(self, data_dict):
        return True

    #    def setup_template_variables(self, context, data_dict):
    #        if (self.proxy_is_enabled 
    #                and not data_dict['resource']['on_same_domain']):
    #            url = proxy.get_proxified_resource_url(data_dict)
    #            p.toolkit.c.resource['url'] = url

    def form_template(self, context, data_dict):
        return 'embed_form.html'
    def view_template(self, context, data_dict):
        return 'embed_view.html'
