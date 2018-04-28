def rgb_hex():
  invalid_msg="Invalid values entered."
  red=int(input("Please enter the value for RED: "))
  #green=int(input("Please enter the value for GREEN: "))
  #blue=int(input("Please enter the value for BLUE: "))
  if (red<0 or red>255):
    print(invalid_msg)
    return
  green=int(input("Please enter the value for GREEN: "))
  if green<0 or green >255:
    print(invalid_msg)
    return
  blue=int(input("Please enter the value for BLUE: "))
  if blue<0 or blue>255:
    print(invalid_msg)
    return
  val=(red<<16)+(green<<8)+blue
  print("Hex value is %s"%((hex(val)[2:])).upper())
def hex_rgb():
  hex_val=input("Enter a hexadecimal value: ")
  if len(hex_val)!=6:
    print(invalid_msg)
  else:
    hex_val=int(hex_val,16)
  two_hex_digits=2**8
  blue=hex_val % two_hex_digits
  hex_val=(hex_val>>8)
  green=hex_val % two_hex_digits
  hex_val=(hex_val>>8)
  red=hex_val % two_hex_digits
  print("The RGB values should be %d%d%d"%(red,green,blue))
def convert():
  while True:
    option=input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option=="1":
      print("RGB to Hex...")
      rgb_hex()
    elif option=="2":
      print("Hex to RGB...")
      hex_rgb()
    elif option=="X" or option=="x":
      break
    else:
      print("Error")
convert()
