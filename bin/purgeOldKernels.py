#!/usr/bin/python3
#
# purgeOldKernels.py: simple script (for now anyway) to save typing when purging old kernels
# ------------------------------------------------------------------------------------------
# There are automatic ways to do this (see first reference) but they sound a little risky to me.
# For now, I just want to do it manually, so I know what's happening, without doing a lot of typing.
# References:
#   https://help.ubuntu.com/community/Lubuntu/Documentation/RemoveOldKernels
#   http://elementaryos.stackexchange.com/questions/95/how-to-remove-old-kernel-versions
#
import sys      # for accessing command line arguments
from subprocess import call      # for running commands

##
# syntax: print this script's syntax statement
#
def syntax() :
	print( 'purgeOldKernels.py kernelVersion' )
	print( '  Purges the specified version of the kernel.' )

##
# Get the kernel version, which must be supplied via a command line argument
#
def getKernelVersion () :
	kernelVersion = ''
	if ( len(sys.argv) == 1 ) :
		syntax()
		print( 'No kernel version specified!' )
		print( 'Run "dpkg -l | grep linux-image" and supply the numeric part (e.g., 3.13.0-55).' )
		print( 'Exiting.' )
		exit( 1 )
	elif ( len(sys.argv) == 2 ) :
		kernelVersion = sys.argv[1]
	else :
		print( 'Too many arguments, try again.' )
		exit( 1 )
	return kernelVersion


kernelVersion = getKernelVersion()

print( 'Deleting kernel version ' + kernelVersion )

