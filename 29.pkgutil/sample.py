# sample.py
import demopkg1

print("Imported demopkg1 from:", demopkg1.__file__)

import demopkg1.shared
print("demopkg1.shared says:", demopkg1.shared.shared_func())

try:
    import demopkg1.not_shared
    print("demopkg1.not_shared says:", demopkg1.not_shared.not_shared_func())
except ModuleNotFoundError as e:
    print("demopkg1.not_shared: Not found —", e)
