# F(bouyancy) = pfluid * volume_displaced * g
g = 9.81
import sys
pfluid = float(sys.argv[1])
volume_displace = float(sys.argv[2])

bouyancy = pfluid * volume_displace * g
import stdio
stdio.write(f"{bouyancy} N\n")