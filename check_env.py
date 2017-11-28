import sys

if sys.version_info < (3,5):
    print("ERROR: we recommend using at least Python 3.5 to run the tutorials. "
          "You are running version {0}. Please place a red flag on your "
          "computer or raise your hand for help."
          .format(".".join([str(x) for x in sys.version_info])))
    sys.exit(1)

packages = ['numpy', 'matplotlib', 'astropy', 'astroquery']
failed = []
for pkg in packages:
    try:
        __import__(pkg)
    except ImportError:
        failed.append(pkg)

if failed:
    print("ERROR: the following packages failed to import. You will need to "
          "install these in order to run the tutorials. Please place a red "
          "flag on your computer or raise your hand for help.")
    for pkg in failed:
        print(pkg)

    sys.exit(1)

print("Everything looks ok!")
