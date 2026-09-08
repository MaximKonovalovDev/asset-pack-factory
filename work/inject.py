import os

base = open("C:/forge-scratch/kaggle-cook/cook-template.py").read()
pre = ("import subprocess, sys\n"
       "subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'hy3dgen', 'trimesh'])\n")
out = base.replace("TUNNEL_HERE", os.environ["FORGE_COOK_TUNNEL"]).replace(
    "TOKEN_HERE", os.environ["FORGE_GATEWAY_TOKEN"]).replace('"""Forge cook', pre + '"""Forge cook')
open("C:/forge-scratch/kaggle-cook/cook.py", "w").write(out)
print("injected, no secrets printed")
