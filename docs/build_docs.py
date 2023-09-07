import subprocess
import yaml 
import os

# this publishes some environment varialbes which we access in conf.py
# and runs the build command, the same way we did locally
def build_doc(version, language, tag):
    os.environ["current_version"] = version
    os.environ["current_language"] = language
    subprocess.run(["git", "checkout", tag])
    os.environ['SPHINXOPTS'] = "-D language='{}'".format(language)
    subprocess.run(["make" , "html"])    

# after the build we move the output or the html files
def move_dir(src, dst):
  subprocess.run(["mkdir", "-p", dst])
  subprocess.run("mv "+src+'* ' + dst, shell=True)

# just to not always run the entire build we push a build_all_docs
os.environ["build_all_docs"] = str(True)
# and the root path where the docs are available
os.environ["pages_root"] = "https://those1990.github.io/SphinxExample" 

# we treat the main branch a bit different because we want to have english latest as landing page
build_doc("latest", "en", "main")
move_dir("./_build/html/", "../pages/")
build_doc("latest", "de", "main")
move_dir("./_build/html/", "../pages/de/")

# we open our yaml file for all other versions
with open("versions.yaml", "r") as yaml_file:
  docs = yaml.safe_load(yaml_file)

# and run our build for each defined version and langauge
for version, details in docs.items():
  tag = details.get('tag', '')
  for language in details.get('languages', []): 
    build_doc(version, language, version)
    move_dir("./_build/html/", "../pages/"+version+'/'+language+'/')
