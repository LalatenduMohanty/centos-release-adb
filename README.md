centos-release-adb
--------------------
Package contains following 

* It contains the public GPG key that is used for verification of the released RPMs
* YUM repository file for packages required for ADB (Atomic Devleoper Bundle)

Building the SRC RPM
--------------------
```
rpmbuild -bs --define "_sourcedir $PWD" --define "_srcrpmdir $PWD"  --define "dist .el7" centos-release-adb.spec
```
