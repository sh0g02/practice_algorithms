# frozen_string_literal: true

i = gets.to_i
inputs = gets.split.map(&:to_i)
exist = false

inputs.each do |_i|
  exist = _i == i
end

puts exist ? 'Yes' : 'No'
