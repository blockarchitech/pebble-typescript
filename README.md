# Pebble Typescript

A somewhat foolproof way to write Pebble apps with TypeScript.

## Usage

- Clone this repository
- Run `npm install` to install dependencies
- Edit `bundler.sh` to point to your `pebble` tool location.
  - If you installed the SDK locally, this is probably somewhere in ~/pebble-dev.
- Run `npm run build`
  - This will build your Pebble project, build your TypeScript files, and chuck the TS files into PBW.

You can also run `npm run clean`, which will remove all build artifacts as well as run `pebble build`.

## How it works

The Pebble SDK natively supports JavaScript, thru PebbleKit JS. This is great, however there's a few issues:

- The SDK uses an ancient JavaScript version, almost ES5 but missing some features.
- The SDK doesn't support TypeScript, which is a superset of JavaScript that adds types and other features.
- The SDK doesn't allow you to customize Webpack settings.
- The SDK doesn't allow you to use many popular npm packages.

This project aims to solve these issues by providing a way to write TypeScript code, and telling the Pebble SDK to _only_ build the C code. We then take the compiled C code, as well as our Webpack-compiled TypeScript code, and chuck it into a PBW file. However, this is not a perfect solution, and there are some caveats:

- This **only works on Android**[^1]. The iOS Pebble app does not support the modern versions of JavaScript that we use. This is a limitation of the Pebble app, and there's nothing we can do about it as we cannot update the Pebble app.

[^1]: FWIW, I've never actually tried. However, when others in the community have attempted to use modern JS on the iOS app, explosions occur. You could try to get around this by setting Webpack's target to ES5, however then you're missing out on newer JS features at the runtime.
