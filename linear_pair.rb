# frozen_string_literal: true

k = gets.to_i
a_list = gets.split.map(&:to_i)
b_list = gets.split.map(&:to_i)

min_value = 200_000_000

a_list.each do |a|
  b_list.each do |b|
    next if a + b < k

    min_value = a + b if a + b < min_value
  end
end

puts min_value
