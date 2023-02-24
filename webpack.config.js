const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = ({ mode } = { mode: "production" }) => {
    console.log(`mode is: ${mode}`);

    return { 
            mode,
            entry: "./src/app.js",
            output: {
                publicPath: "/",
                path: path.resolve(__dirname, "build"),
                filename: "bundled.js"
            },
            module:{
                rules:[
                    {
                        test: /\.js$/,
                        exclude:/node_module/,
                        use:{
                            loader:'babel-loader'
                        }

                    }                    
                ]
            },
            plugins: [
                new HtmlWebpackPlugin({
                    template: "./public/index.html"
                }),
            ]
        }
};