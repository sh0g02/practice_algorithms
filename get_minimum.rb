# frozen_string_literal: true

inputs = gets.split.map(&:to_i)

min_value = 200_000_000
inputs.each do |v|
  min_value = v if v < min_value
end

puts min_value
