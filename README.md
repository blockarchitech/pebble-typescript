# Pebble Typescript

A somewhat foolproof way to write Pebble apps with PebbleKit JS using TypeScript.

## Usage

1. Clone this repository
2. Open `pebble.py`, and edit `PEBBLE_TOOL_LOCATION` to point to your Pebble Tool location. This can be a wrapper script, or point directly to the `pebble` executable.
3. Run `npm install`
4. Write your TypeScript code in `src/pkts/`
5. Run `npm run build`
6. Your compiled Pebble app will be in `build/pebble-ts.pbw`

To clean, simply run `npm run clean`. This will delete the webpack caches and run `pebble clean` as to not leave any pebble build artifacts behind.
