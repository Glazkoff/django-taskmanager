module.exports = {
  devServer: {
    hot: true,
    hotOnly: true,
    disableHostCheck: true,
    historyApiFallback: true,
    public: "0.0.0.0:8000",
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
      "Access-Control-Allow-Headers":
        "X-Requested-With, content-type, Authorization"
    },
    watchOptions: {
      poll: 1000,
      ignored: "/app/node_modules/"
    }
  },
  chainWebpack: (config) => {
    ["vue-modules", "vue", "normal-modules", "normal"].forEach((rule) => {
      config.module
        .rule("scss")
        .oneOf(rule)
        .use("resolve-url-loader")
        .loader("resolve-url-loader")
        .before("sass-loader")
        .end()
        .use("sass-loader")
        .loader("sass-loader")
        .tap((options) => ({ ...options, sourceMap: true }));
    });

    // const svgRule = config.module.rule("svg");
    // svgRule.uses.clear();
    // svgRule;
    // svgRule
    //   .oneOf("inline")
    //   .resourceQuery(/inline/)
    //   .use("babel-loader")
    //   .loader("babel-loader")
    //   .end()
    //   .use("vue-svg-loader")
    //   .loader("vue-svg-loader")
    //   .end()
    //   .end()
    //   .oneOf("external")
    //   .use("file-loader")
    //   .loader("file-loader")
    //   .options({
    //     name: () => {
    //       // (resourcePath, resourceQuery)
    //       // `resourcePath` - `/absolute/path/to/file.js`
    //       // `resourceQuery` - `?foo=bar`
    //       if (process.env.NODE_ENV === "development") {
    //         return "[path][name].[ext]";
    //       }
    //       return "[contenthash].[ext]";
    //     }
    //   });
  }
};
