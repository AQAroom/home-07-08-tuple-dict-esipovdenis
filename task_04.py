v1_major = float(input())
v1_minor = float(input())
v1_patch = float(input())
v2_major = float(input())
v2_minor = float(input())
v2_patch = float(input())
version1 = (v1_major, v1_minor, v1_patch)
version2 = (v2_major, v2_minor, v2_patch)
if version1 == version2:
    print(0)
elif version1 > version2:
    print(1)
elif version1 < version2:
    print(2)
