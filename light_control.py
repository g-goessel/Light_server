"""
Ce fichier sera appelé avec des paramètres par le serveur unified remote
"""

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-r','--red', type=int, help='tell server to change the red color')
parser.add_argument('-g','--green', type=int, help='tell server to change the green color')
parser.add_argument('-b','--blue', type=int,default=10, help='tell server to change the blue color')
parser.add_argument('-p','--power', type=bool, help='tell server to turn the lights on (1) or off (0)')
args = parser.parse_args()

f = open('/home/guillaume/git_folder/Light_server/comm_file','w')
liste=[]
for arg in args.__dict__ :
  if args.__dict__[arg]!=None:
      liste.append([arg,args.__dict__[arg]])
f.write(json.dumps(liste))
f.close
