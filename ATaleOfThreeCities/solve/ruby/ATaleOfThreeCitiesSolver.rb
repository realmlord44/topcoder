#! /usr/bin/env ruby

require_relative "ATaleOfThreeCities"

require "gettc/types"
include Gettc

def init
  gettc_home = File.expand_path(ENV["GETTC_HOME"] || File.join(ENV["HOME"], ".gettc"))
  $LOAD_PATH << File.join(gettc_home, "include", "ruby")
  require "topcoder"
  include TopCoder
end

def main
  reader = Reader.new(IO.read(ARGV[0]))
  ax = reader.next(TArray.new(TInt))
  reader.next()
  ay = reader.next(TArray.new(TInt))
  reader.next()
  bx = reader.next(TArray.new(TInt))
  reader.next()
  by = reader.next(TArray.new(TInt))
  reader.next()
  cx = reader.next(TArray.new(TInt))
  reader.next()
  cy = reader.next(TArray.new(TInt))

  result = ATaleOfThreeCities.new().connect(ax, ay, bx, by, cx, cy)
  IO.write(ARGV[1], Writer.new.next(result, TDouble).to_s)
end

init
main
