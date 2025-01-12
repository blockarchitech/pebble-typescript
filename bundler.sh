#!/bin/bash

PEBBLE_TOOL_LOCATION="./pebble-wrapper.sh" # Change this to the path of your pebble-tool. Probably in ~/pebble-dev if SDK is locally installed
function build() {
    $PEBBLE_TOOL_LOCATION build
    npm run webpack

    mkdir -p tmp
    mv build/pebble.pbw tmp/oldpebble.zip
    unzip tmp/oldpebble.zip -d tmp
    rm tmp/oldpebble.zip
    cp dist/bundle.js tmp/pebble-js-app.js
    cp dist/bundle.js.map tmp/pebble-js-app.js.map
    (cd tmp && zip -o -r pebble.pbw *)
    cp tmp/pebble.pbw build/pebble.pbw
    rm -rf tmp
}

function clean() {
    $PEBBLE_TOOL_LOCATION clean
    rm -rf dist
    rm -rf tmp
}

if [ "$#" -gt 0 ]; then
    case "$1" in
        build)
            build
            ;;
        clean)
            clean
            ;;
        *)
            echo "Usage: $0 [build|clean]"
            ;;
    esac
else
    echo "Usage: $0 [build|clean]"
fi
