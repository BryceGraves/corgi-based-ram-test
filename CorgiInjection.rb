require 'launchy'

def corgi_injection
  File.open("/home/gravebry/Code/CorgiBasedRamTest/CorgisToInject.txt", "r") do |f|
    f.each_line do |line|
      Launchy.open(line)
    end
  end
end

corgi_injection