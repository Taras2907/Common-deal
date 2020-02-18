const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    // on Windows you might want to set publicPath: "http://127.0.0.1:8080/"
    publicPath: "https://common-deal.azurewebsites.net/",
    outputDir: './dist/',

    chainWebpack: config => {

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: './webpack-stats.json'}])

        config.output
            .filename('bundle.js')

        config.optimization
        	.splitChunks(false)

        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            // the first 3 lines of the following code have been added to the configuration
            .public('https://common-deal.azurewebsites.net/')
            .host('common-deal.azurewebsites.net')
            .port(443)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(true)
            .disableHostCheck(true)
            .headers({"Access-Control-Allow-Origin": ["\*"]})

    },

    // uncomment before executing 'npm run build'
    css: {
        extract: {
          filename: 'bundle.css',
          chunkFilename: 'bundle.css',
        },
    }

};