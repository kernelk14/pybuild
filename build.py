# -- We MUST always include this libbuild module.
import libbuild

def Usage():
    libbuild.usage("""The Test Usage
Please refer to the repo for more info.
          """)

def Build():
    Usage()
    libbuild.cmd("echo 'Hello!'")
    exit(0)
