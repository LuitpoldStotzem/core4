// vue.config.js
module.exports = {
  outputDir: 'dist',
  lintOnSave: true,
  baseUrl: process.env.NODE_ENV === 'production' ? './voting/dist' : './',
  devServer: {
    port: 3000
  },
  configureWebpack: {
    resolve: {
      alias: {
        'vue$': 'vue/dist/vue.esm.js'
      }
    }
  }
}
