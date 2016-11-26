#! /usr/bin/env ruby

require_relative "ShopPositions"

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
  n = reader.next(TInt)
  reader.next()
  m = reader.next(TInt)
  reader.next()
  c = reader.next(TArray.new(TInt))

  result = ShopPositions.new().maxProfit(n, m, c)
  IO.write(ARGV[1], Writer.new.next(result, TInt).to_s)
end

init
main
