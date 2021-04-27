# frozen_string_literal: true

i = gets.to_i
inputs = gets.split.map(&:to_i)
found_id = -1 # 条件を満たすものがある場所

inputs.each_with_index do |v, k|
  if v == i
    found_id = k
    break
  end
end

puts found_id
