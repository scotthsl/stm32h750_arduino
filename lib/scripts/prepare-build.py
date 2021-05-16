import shutil
import sys
from os.path import isdir, isfile, join
import os
from filecmp import dircmp
Import("env")

platform = env.PioPlatform()
board = env.BoardConfig()

print("++++++++++++++++++++++++++++++copy variant start++++++++++++++++++++++++++++++")
print("Prepare env for " + env.get("BOARD"))

frwk = env.get("PIOFRAMEWORK")
pkg = platform.frameworks[frwk[0]]["package"]

pkg_dir = platform.get_package_dir(pkg)

print("Package is " + pkg)
print("Location: " + pkg_dir)

proj_dir = env.get("PROJECT_DIR")
variant = board.get("build.variant")

# copy my variant dir to pio packages dir for every build
my_variant = join(proj_dir, "lib", pkg, "variants", variant)
if not os.path.isdir(my_variant):
  raise Exception("project variant directory is not exist!")
pkg_variant = join(pkg_dir, "variants", variant)

print("my variant dir: " + my_variant)
print("target variant dir: " + pkg_variant)

def sync_dir(src, dst):
  if os.path.isdir(dst):
    print("target variant is exist!")
    # if target variant dir is exist, check whether it has update
    dcmp = dircmp(src, dst)

    if len(dcmp.diff_files) > 0:
      print("Some files need to be updated:")
      for f in dcmp.diff_files:
        src_f = join(src, f)
        print(src_f)
        dst_f = join(dst, f)
        os.remove(dst_f)
        shutil.copy(src_f, dst)
    if len(dcmp.left_only) > 0:
      print("Some files need to be create:")
      for f in dcmp.left_only:
        f = join(src, f)
        print(f)
        shutil.copy(f, dst)
    if len(dcmp.right_only) > 0:
      print("Some files need to be removed:")
      for f in dcmp.right_only:
        f = join(dst, f)
        print(f)
        os.remove(f)
  else:
    print("target variant is not exist. will creat it!")
    # target is not exist, copy src to dst
    try:
      shutil.copytree(src, dst)
    except Exception as e:
      print("Failed to copy dir: " + str(e))
      raise

sync_dir(my_variant, pkg_variant)

print("++++++++++++++++++++++++++++++copy variant end++++++++++++++++++++++++++++++")