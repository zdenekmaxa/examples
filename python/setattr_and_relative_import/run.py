"""
run script of the example.

testmod uses relative import and this run script
needs to be run from above its directory:
        
        python -m setattr_and_relative_import.run
        
        python run.py reasuls in
        "ValueError: Attempted relative import in non-package"
"""

from testmod import func
func()
