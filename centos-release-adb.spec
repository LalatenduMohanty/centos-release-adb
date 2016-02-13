Summary: Release file for Atomic Developer Bundle (ADB) 
Name: centos-release-adb
Epoch: 0
Version: 1
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
Source0: RPM-GPG-KEY-CentOS-SIG-Atomic
Source1: CentOS-release-adb.repo
URL: http://wiki.centos.org/SpecialInterestGroup/Atomic

BuildArch: noarch

Provides: centos-release-adb
Requires: centos-release

BuildRoot: %{_tmppath}/%{name}-root

%description
Provided files required by release components for ADB

%prep
%setup -q -n %{name} -T -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
install -m 644 %SOURCE0 $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-release-adb.repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Atomic
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-release-adb.repo

%changelog

* Sat Feb 13 2016 Lalatendu Mohanty <lmohanty@redhat.com> - 1-1
- Basic setup with the gpg key
