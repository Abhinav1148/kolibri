const path = require('path');
const fs = require('fs');
const mkdirp = require('mkdirp');
const HtmlWebpackPlugin = require('html-webpack-plugin');

function Plugin() {}

Plugin.prototype.apply = function(compiler) {
  if (compiler.hooks) {
    compiler.hooks.compilation.tap('HashiHashWriterPlugin', function(compilation) {
      if (compilation.errors.length > 0) {
        return;
      }

      HtmlWebpackPlugin.getHooks(compilation).afterEmit.tapAsync('HashiWritePlugin', (data, cb) => {
        var outputFilename = path.resolve(
          __dirname,
          '../../kolibri/core/content/build/hashi_filename'
        );
        mkdirp.sync(path.dirname(outputFilename));

        fs.writeFileSync(outputFilename, data.outputName);
        // Tell webpack to move on
        cb(null, data);
      });
    });
  }
};

// Note that the hashi iframe client doesn't currently support code splitting
// in the way that it is loaded, so don't do any code splitting just yet.

module.exports = {
  entry: path.resolve(__dirname, './src/iframe.js'),
  output: {
    filename: 'hashiframe-[contenthash].js',
    path: path.resolve(__dirname, '../../kolibri/core/content/static/hashi'),
  },
  mode: 'none',
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: {
          test: /(uuid|core-js)/,
          not: [/\.(esm\.js|mjs)$/],
        },
      },
    ],
  },
  plugins: [
    new Plugin(),
    new HtmlWebpackPlugin({
      filename: 'hashi-[contenthash].html',
      template: 'src/iframe.html',
    }),
  ],
};
