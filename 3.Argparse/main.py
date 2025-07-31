import math
import argparse

parser=argparse.ArgumentParser(description='Calculate volume of a Cylinder')
parser.add_argument('-r','--radius',type=int,required=True,metavar='',help='Radius of Cylinder')
parser.add_argument('-H','--height',type=int,required=True,metavar='',help="Height of cylinder")
args=parser.parse_args()

def cylinder_volume(radius,height):
    vol=(math.pi)*(radius**2)*(height)
    return vol

if __name__=='__main__':
    print(cylinder_volume(args.radius,args.height))

#Below output will generated
"""
usage: main.py [-h] [-r] [-H]

Calculate volume of a Cylinder

options:
  -h, --help      show this help message and exit
  -r , --radius   Radius of Cylinder
  -H , --height   Height of cylinder

"""
