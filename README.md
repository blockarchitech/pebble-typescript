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

- As of current, the PebbleKit library has no type definitions. The keen-eyed will notice that the `pebble.d.ts` file simply maps `Pebble` to `any`. This is not ideal, but it's better than nothing. (which, is what you'd get otherwise)
- This **only works on Android**. The iOS Pebble app does not support the modern versions of JavaScript that we use. This is a limitation of the Pebble app, and there's nothing we can do about it as we cannot update the Pebble app.
