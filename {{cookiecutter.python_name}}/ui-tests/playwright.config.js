/**
 * Configuration for Playwright using default from @jupyterlab/galata
 */
const baseConfig = require('@jupyterlab/galata/lib/playwright-config');

module.exports = {
  ...baseConfig,
  webServer: {
    command: 'yarn start',
    url: 'http://127.0.0.1:8000',
    timeout: 120 * 1000,
    reuseExistingServer: !process.env.CI
  }
};
