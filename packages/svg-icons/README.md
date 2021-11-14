# UI System Icon (svg)

This package provides the UI System Icons as optimized plain svg assets.

## Installation

```bash
npm install @tai-ui/svg-icons
```

## Usage

webpack.js:
```js
module.exports = {
    resolve: {
        extensions: [".svg"],
    },
    module: {
        rules: [
            {
                test: /\.svg$/,
                use: [
                    {
                        loader: "svg-inline-loader",
                        options: {
                            removeSVGTagAttrs: false,
                        },
                    },
                ],
            }
        ]
    }
};
```

Then reference an icon on a page.

Using template literal:
```ts
import AddIcon from "@tai-ui/svg-icons/icons/add_20_filled.svg";

`<div>${AddIcon}</div>`
```

Or `require`:
```ts
var icon = require('@tai-ui/svg-icons/icons/add_20_filled.svg');
```