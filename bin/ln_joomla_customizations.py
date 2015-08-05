#!/usr/bin/python3
#
# ln_joomla_customizations.py: links our customizations, so we can keep them separate from the main joomla code
# -------------------------------------------------------------------------------------------------------------
# This makes it easier to upgrade to new versions of joomla, and use selected extensions on multiple sites
#
import os
from os import chdir, getcwd, listdir
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
#  Links the language files used for localization
#
def lnLanguageFiles( extension ) :
	print( 'Linking language files for extension ' + extension + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + extension + '/language/en-GB'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/language/en-GB'
	languageFiles = listdir( rootedSourceDir )
	for langFile in languageFiles:
		rootedLanguageFile = rootedSourceDir + '/' + langFile
		if( isfile(rootedLanguageFile) ) :
			print( '\tlinking "' + rootedLanguageFile + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = 'cd ' + destinationDir + '; ln -fs ' + rootedLanguageFile + ' .; cd ' + htdocsDir 
		### print( 'lnCommand: ' + lnCommand )
			call( lnCommand, shell=True )
##
#  Links directories containing libraries ("vendor" code)
#
def lnLibrariesVendorDirs( extension ) :
	print( 'Linking libraries/vendor directories for extension ' + extension + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + extension + '/libraries/vendor'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/libraries/vendor'
	librariesVendors = listdir( rootedSourceDir )
	for librariesVendorDir in librariesVendors:
		rootedLibrariesVendorDir = rootedSourceDir + '/' + librariesVendorDir
		if( isdir(rootedLibrariesVendorDir) ) :
			print( '\tlinking "' + rootedLibrariesVendorDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = 'cd ' + destinationDir + '; ln -fs ' + rootedLibrariesVendorDir + ' .; cd ' + htdocsDir 
		### print( 'lnCommand: ' + lnCommand )
			call( lnCommand, shell=True )
##
#  Links directories used by modules
#
def lnModuleDirs( extension ) :
	print( 'Linking modules directories for extension ' + extension + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + extension + '/modules'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/modules'
	moduleDirs = listdir( rootedSourceDir )
	### print( 'lnModuleDirs test: rootedSourceDir = ' + rootedSourceDir )
	### print( 'lnModuleDirs test: destinationDir = ' + destinationDir )
	### print( 'moduleDirs:' )
	### print( moduleDirs )
	for modDir in moduleDirs:
		rootedModuleDir = rootedSourceDir + '/' + modDir
		if( isdir(rootedModuleDir) ) :
			print( '\tlinking "' + rootedModuleDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = 'cd ' + destinationDir + '; ln -fs ' + rootedModuleDir + ' .; cd ' + htdocsDir 
		### print( 'lnCommand: ' + lnCommand )
			call( lnCommand, shell=True )
##
#  Links directories used by templates
#
def lnTemplateDirs( extension ) :
	print( 'Linking templates directories for extension ' + extension + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + extension + '/templates'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/templates'
	templateDirs = listdir( rootedSourceDir )
	for tmplDir in templateDirs:
		rootedTemplateDir = rootedSourceDir + '/' + tmplDir
		if( isdir(rootedTemplateDir) ) :
			print( '\tlinking "' + rootedTemplateDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = 'cd ' + destinationDir + '; ln -fs ' + rootedTemplateDir + ' .; cd ' + htdocsDir 
			### print( 'lnCommand: ' + lnCommand )
			call( lnCommand, shell=True )
##
#  Driver function to call other functions to link specific types of extensions
#
def lnExtension( extension ) :
	print( 'Linking files in the ' + extension + ' extension...' )
	githubRepoDir = customizationsDir + '/'  + extension
	extensionSubdirs = listdir( githubRepoDir )
	extensionSubdirs.sort()
	for subdirectory in extensionSubdirs:
		if ( subdirectory == 'language' ) :
			lnLanguageFiles( extension )
		elif ( subdirectory == 'libraries' ) :
			lnLibrariesVendorDirs( extension )
		elif ( subdirectory == 'modules' ) :
			lnModuleDirs( extension )
		elif ( subdirectory == 'templates' ) :
			lnTemplateDirs( extension )

customizationsDir = 'customizations'
mainSiteDir = 'joomoowebsites.com'
htdocsDir = getcwd()
exitVal = 0

checkForDirectory( customizationsDir )   # exits if directory not present
checkForDirectory( mainSiteDir )         # exits if directory not present

customizations = listdir( customizationsDir )
customizations.sort()
print( 'Linking the following customizations to the appropriate directories in ' + mainSiteDir + ':' )
print( customizations )

for extension in customizations:
	lnExtension( extension )

exit( exitVal )
