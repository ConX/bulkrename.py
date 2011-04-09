#!/usr/bin/env python
# ==================================================
# Created by Xanthopoulos Constantinos
# Email: conx AT xanthopoulos DOT info.
# This script renames all the files in a directory
# using a certain pattern. 
# Use ./bulkrename.py --help for more information.
# ==================================================
import os,re,sys
from optparse import OptionParser


def getRenamedFilename(filename, prefix, suffix, digits, number):
	if re.search("__tmp$", filename):
		filename = filename[:-5]
	extension = re.match(".*([.].+)$", filename)
	if extension:
		extension = extension.group(1)
	else:
		extension = ""
	padded_num = '%0*d' % (digits, number)
	return prefix + padded_num + suffix + extension

def rename(directory, prefix, suffix, dryrun):
	file_list = os.listdir(directory)
	file_list.sort()
	digits = len(str(len(file_list)))
	
	number = 0
	for filename in file_list:
		if getRenamedFilename(filename, prefix, suffix, digits, number) in file_list:
			if not dryrun:
				rename(directory, prefix, "__tmp", dryrun)
				break
		number += 1
	
	file_list = os.listdir(directory)
	number = 0
	for filename in file_list:
		if not os.path.isdir(directory+filename):
			renamedfilename = getRenamedFilename(filename, prefix, suffix, digits, number)
			if renamedfilename in file_list:
				print "Cannot rename! %s already exists as a directory. Please rename it!" % renamedfilename

				sys.exit()
			print "Renaming %s -> %s" % (directory + filename, directory + renamedfilename)
			if not dryrun:
				os.rename(directory + filename, directory + renamedfilename)
			number += 1
		

if __name__ == "__main__":
	usage = "Usage: %prog [options] <directory>"
	parser = OptionParser(usage)
	parser.add_option("-p", "--prefix", default="", dest="prefix", help="Add the prefix string.")
	parser.add_option("-s", "--suffix", default="", dest="suffix", help="Add the suffix string.")
	parser.add_option("-d", "--dry-run", action="store_true", default=False,dest="dryrun", help="Run without actually renaming any files.")
	(options, args) = parser.parse_args()
	if not len(args):
		parser.print_help()
		sys.exit()
	directory = args[0]
	if directory[-1] != '/':
		directory += '/'
	rename(directory, options.prefix, options.suffix, options.dryrun)
