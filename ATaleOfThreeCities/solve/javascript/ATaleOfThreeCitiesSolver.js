#! /usr/bin/env node

var fs = require("fs");
var path = require("path");
var tc = null;

function init() {
  var gettcHome = process.env.GETTC_HOME || path.join(process.env.HOME, ".gettc");
  var includeDir = path.join(gettcHome, "include", "javascript");
  tc = require(path.join(includeDir, "topcoder"));
}

function main() {
  try {
    var input = fs.readFileSync(process.argv[2], { encoding: "ascii" });
    var reader = new tc.Reader(input);
        var ax = reader.next('int[]'); reader.next();
    var ay = reader.next('int[]'); reader.next();
    var bx = reader.next('int[]'); reader.next();
    var by = reader.next('int[]'); reader.next();
    var cx = reader.next('int[]'); reader.next();
    var cy = reader.next('int[]');

    var ATaleOfThreeCities = require("./ATaleOfThreeCities");
    var result = ATaleOfThreeCities.connect(ax, ay, bx, by, cx, cy);

    var writer = new tc.Writer();
    writer.next(result, "double");
    fs.writeFileSync(process.argv[3], writer.toString(), { encoding: "ascii" });
  } catch (err) {
    console.log(err.toString());
    console.trace();
  }
}

init();
main();
