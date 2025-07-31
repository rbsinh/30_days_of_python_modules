# demopkg1/__init__.py
import pkgutil
import pprint

print("demopkg1.__path__ before:", __path__)
__path__ = pkgutil.extend_path(__path__, __name__)
print("demopkg1.__path__ after:", __path__)
print("*************")
print(__path__)




'''
PYTHONPATH=extension python3 sample.py
'''