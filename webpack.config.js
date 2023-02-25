const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = ({ mode } = { mode: "production" }) => {
    console.log(`mode is: ${mode}`);

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
    }
};