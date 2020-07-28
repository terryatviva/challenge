/* eslint-disable */
const CompressionPlugin = require('compression-webpack-plugin');


/* eslint-enable */
module.exports = {
  publicPath: process.env.NODE_ENV === 'development' ? '/apps/vivanaturals/' : '',
  configureWebpack: {
    output: {
      filename: 'vivanaturals.js',
    },
  },
  devServer: {
	  port:8086
  },
  css: {
    extract: false,
  },
  filenameHashing: false,
  chainWebpack:
    (config) => {
      config.externals({
        vue: 'Vue',
        bootstrap: 'bootstrap',
      });
      config.optimization.splitChunks(false);
      config.plugin('gzip')
        .use(new CompressionPlugin({
          test: /\.js(\?.*)?$/i,
          filename: '[file].gz',
          algorithm: 'gzip',
        }));
    },
    pluginOptions: {
        i18n: {
          locale: 'en',
          fallbackLocale: 'en',
          localeDir: 'locales',
          enableInSFC: true
        }
    }
};
