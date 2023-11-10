import helper
import networks_basic
import switching
import Subnet
import error

error.pfHops_error(1200*8, 1e-5, 5)
error.pfHops_good(1200*8, 1e-5, 5)

networks_basic.TCP(5, 100, 60, 16, timeout=9)

networks_basic.propagation_delay(5000e3, 1e8)

error.max_BER_hops(1250*8, 0.999, 9)

error.max_bits_hops(1-0.9999, 1e-7, 6)/8

Subnet.print_bin([255,255,192,0])

Subnet.subnet([128,96,134,15],[255,255,128,0])