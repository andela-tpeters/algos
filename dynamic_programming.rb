$fib_cache = {}
def fib(n)
  if $fib_cache[n]
     return $fib_cache[n]
  end
  if n < 2
    return n
  end

  res = fib(n - 1) + fib(n - 2)
  $fib_cache[n] = res
  res
end


# puts fib(80)
