import os
import sys

PEBBLE_TOOL_LOCATION = "./pebble-wrapper.sh"

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        os.system(PEBBLE_TOOL_LOCATION + ' build')

        binaries = [
            {'platform': 'aplite'},
            {'platform': 'basalt'},
            {'platform': 'chalk'},
            {'platform': 'diorite'},
        ]

        os.system('npm run webpack')
        os.system('cp dist/bundle.js build/pebble-js-app.js')
        os.system('cp dist/bundle.js.map build/pebble-js-app.js.map')

        zip_file = 'build/pebble-ts.pbw'
        zip_args = [
            'zip',
            '-j',
            zip_file,
            'build/pebble-js-app.js',
            'build/pebble-js-app.js.map',
            'build/appinfo.json',
        ]
        for binary in binaries:
            zip_args.append(binary['platform'])
        os.system(' '.join(zip_args))
    elif len(sys.argv) > 1 and sys.argv[1] == "clean":
        os.system(PEBBLE_TOOL_LOCATION + ' clean')
        os.system("rm -rf dist")
    else:
        print("Usage: python build.py [build|clean]")