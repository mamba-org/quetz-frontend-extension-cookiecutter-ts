import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

/**
 * Initialization data for the {{ cookiecutter.extension_name }} extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: '{{ cookiecutter.extension_name }}:plugin',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('Quetz extension {{ cookiecutter.extension_name }} is activated!');
  }
};

export default plugin;
