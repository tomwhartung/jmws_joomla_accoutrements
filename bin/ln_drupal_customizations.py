#!/usr/bin/python3
#
# ln_drupal_customizations.py: links our customizations, so we can keep them separate from the drupal code
# --------------------------------------------------------------------------------------------------------
#
import os
from os import chdir, getcwd, listdir, makedirs
from os.path import isfile, isdir, islink
from subprocess import call

##
#  Checks that the specified directory exists, exiting with an error message if it doesn't
#
def checkForDirectory( dirToCheck ) :
	if isdir( dirToCheck ) :
		print( 'Found a ' + dirToCheck + ' directory, cool.' )
	else:
		print( 'Expecting a "' + dirToCheck + '" directory, but it is not here.' )
		print( 'The current directory is: "' + htdocsDir + '"' )
		print( 'Change to a different directory, preferably one named "htdocs," and try again.' )
		exit( 1 )

##
#  Links directories containing jmws modules
#
def lnModulesDirs( customization ) :
	print( 'Linking sites/all/modules/jmws directories for customization ' + customization + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + customization + '/sites/all/modules/jmws'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/sites/all/modules/jmws'
	drupalJmwsModules = listdir( rootedSourceDir )
	print( 'lnModulesDirs: rootedSourceDir = ' + rootedSourceDir )
	print( 'lnModulesDirs: destinationDir = ' + destinationDir )
	print( 'lnModulesDirs: drupalJmwsModules = ', end="" )
	print( drupalJmwsModules )
	for moduleDir in drupalJmwsModules :
		rootedModuleDir = rootedSourceDir + '/' + moduleDir
		if( isdir(rootedModuleDir) ) :
			print( '\tlinking "' + rootedModuleDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = "    cd " + destinationDir + ";\n    ln -fs " + rootedModuleDir + " .;\n    cd " + htdocsDir 
			print( "lnCommand:\n" + lnCommand )
			call( lnCommand, shell=True )

##
#  Links directories containing jmws themes
#
def lnThemesDirs( customization ) :
	print( 'Linking sites/all/themes/jmws directories for customization ' + customization + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + customization + '/sites/all/themes/jmws'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/sites/all/themes/jmws'
	wpContentThemes = listdir( rootedSourceDir )
	print( 'lnThemesDirs: rootedSourceDir = ' + rootedSourceDir )
	print( 'lnThemesDirs: destinationDir = ' + destinationDir )
	print( 'lnThemesDirs: wpContentThemes = ', end="" )
	print( wpContentThemes )
	for themeDir in wpContentThemes :
		rootedThemeDir = rootedSourceDir + '/' + themeDir
		if( isdir(rootedThemeDir) ) :
			print( '\tlinking "' + rootedThemeDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = "    cd " + destinationDir + ";\n    ln -fs " + rootedThemeDir + " .;\n    cd " + htdocsDir 
			print( "lnCommand:\n" + lnCommand )
			call( lnCommand, shell=True )

##
#  Driver function to call other functions to link specific types of customizations
#
def lnCustomization( customization ) :
	print( 'Linking directories in the ' + customization + ' customization...' )
	customizationSitesAllDir = customizationsDir + '/'  + customization + '/sites/all'
	sitesAllModulesJmwsSubdirs = listdir( customizationSitesAllDir )
	sitesAllModulesJmwsSubdirs.sort()
	for subdirectory in sitesAllModulesJmwsSubdirs:
		if ( subdirectory == 'modules' ) :
			lnModulesDirs( customization )
		elif ( subdirectory == 'themes' ) :
			lnThemesDirs( customization )

customizationsDir = 'customizations'
mainSiteDir = 'tomhartung.com'
htdocsDir = getcwd()
exitVal = 0

checkForDirectory( customizationsDir )   # exits if directory not present
checkForDirectory( mainSiteDir )         # exits if directory not present

mainSitesAllDir = mainSiteDir + '/sites/all'
mainSitesAllModulesJmwsDir = mainSitesAllDir + '/modules/jmws'
mainSitesAllThemesJmwsDir = mainSitesAllDir + '/themes/jmws'

if isdir( mainSitesAllDir ) :
	if isdir( mainSitesAllModulesJmwsDir ) :
		print( 'Found a ' + mainSitesAllModulesJmwsDir + ' directory, cool!' )
	else :
		print( 'Warning: making the ' + mainSitesAllModulesJmwsDir + ' directory, because it was not found.' )
		os.makedirs( mainSitesAllModulesJmwsDir )
else :
	print( 'Error!' )
	print( 'Not seeing a ' + mainSitesAllDir + ' directory!' )
	print( 'This does not look like drupal code!' )
	print( 'Exiting!' )
	exit( 1 )

customizations = listdir( customizationsDir )
customizations.sort()
print( 'Linking the following customizations to the appropriate directories in ' + mainSiteDir + ':' )
print( customizations )

print( 'So far so good!' )

exit( exitVal )


for customization in customizations:
	lnCustomization( customization )

exit( exitVal )
