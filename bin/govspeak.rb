#!/usr/bin/env ruby
require 'rubygems'
require 'govspeak'
require 'json'

if ARGV.length > 1 then
  attachments = JSON.parse(File.read(ARGV[1]))
else
  attachments = []
end

puts Govspeak::Document.new(File.read(ARGV[0]), attachments:attachments).to_html
