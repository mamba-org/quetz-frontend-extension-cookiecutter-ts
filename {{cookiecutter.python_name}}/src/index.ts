import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';{% if cookiecutter.kind.lower() == 'theme' %}

import { IThemeManager } from '@jupyterlab/apputils';{% endif %}{% if cookiecutter.has_settings.lower().startswith('y') %}

import { ISettingRegistry } from '@jupyterlab/settingregistry';{% endif %}

/**
 * Initialization data for the {{ cookiecutter.extension_name }} extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: '{{ cookiecutter.extension_name }}:plugin',
  autoStart: true,{% if cookiecutter.kind.lower() == 'theme' %}
  requires: [IThemeManager],{% endif %}{% if cookiecutter.has_settings.lower().startswith('y') %}
  optional: [ISettingRegistry],{% endif %}
  activate: (app: JupyterFrontEnd{% if cookiecutter.kind.lower() == 'theme' %}, manager: IThemeManager{% endif %}{% if cookiecutter.has_settings.lower().startswith('y') %}, settingRegistry: ISettingRegistry | null{% endif %}) => {
    console.log('Quetz extension {{ cookiecutter.extension_name }} is activated!');{% if cookiecutter.kind.lower() == 'theme' %}
    const style = '{{ cookiecutter.extension_name }}/index.css';

    manager.register({
      name: '{{ cookiecutter.extension_name }}',
      isLight: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });{% endif %}{% if cookiecutter.has_settings.lower().startswith('y') %}

    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then(settings => {
          console.log('{{ cookiecutter.extension_name }} settings loaded:', settings.composite);
        })
        .catch(reason => {
          console.error('Failed to load settings for {{ cookiecutter.extension_name }}.', reason);
        });
    }{% endif %}
  }
};

export default plugin;
