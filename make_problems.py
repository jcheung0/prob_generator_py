#!/usr/local/bin/python3
import sys
from jinja2 import Environment, FileSystemLoader,Template
import os
import json
import argparse
from pprint import pprint
PATH = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'lang_templates')),
    trim_blocks=False)


with open('lang_ext.json') as ext_file:
	language_ext = json.load(ext_file)

parser = argparse.ArgumentParser(description='build a problem set for each problem')
parser.add_argument('-n,--name',type=str,
                   help='name for file',required=True, dest="name")

parser.add_argument('-l,--language', help='sum the integers (default: find the max)',dest="lang",nargs="+")
parser.add_argument('-d, --dir',help='specify output directory', dest="directory")
parser.add_argument('-p, --project',help="make project directories", dest="project",nargs="+")

args = parser.parse_args()

def render_template(name,context):
	try:
		return TEMPLATE_ENVIRONMENT.get_template(name).render(context)
	except:
		pass


def create_form(name,language,directory="."):
	ext = language_ext[language]
	print ("creating {0}.{1}".format(name,ext))
	file = open("{0}/{1}.{2}".format(directory,name,ext),"w")
	data = {
		"name":name
	}
	template = render_template("template.{0}".format(ext),data)
	if(template):
		file.write(template)
	file.close()

		
def create_problems(name,language="all"):
	
	if(type(language) == list):
		for i in language:
			if (i in language_ext):
				ext = language_ext[i]
				if(ext):
					create_form(name,i)
				else:
					print("{0} doesn't exists".format(i))
			else:
				print("{0} doesn't exists".format(i))
	else:
		if(language == "all"):
			for i in language_ext:
				print(i)
				create_form(name,i)
		else:
			ext = language_ext[language]
			if(ext):
				create_form(name,language)
			else:
				print("{0} doesn't exists".format(language))

def create_project():
	pass

if __name__ == "__main__":
	name = args.name
	lang = args.lang
	project = args.project

	if(project is not None):
		pass

	if(lang is not None):
		create_problems(name,lang)
	else:
		create_problems(name)
