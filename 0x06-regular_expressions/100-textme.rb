#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)[1-9A-Za-z+]+ (?<=to:)[1-9A-Za-z+]+ (?=<flags:)[1-9:+-]+/).join(",")
