# frozen_string_literal: true

def func(i)
  # 再起関数呼び出しを報告する
  puts "func(#{i})を呼び出しました."

  # ベースケース
  return 0 if i.zero?

  result = i + func(i - 1)
  puts "#{i}までの和 = #{result}"
  return result
end

puts func(5)
