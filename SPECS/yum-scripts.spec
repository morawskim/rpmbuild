#
# spec file for package yum-scripts
#
# Copyright (c) 2017 Marcin Morawski <marcin@morawskim.pl>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/morawskim/rpmbuild/issues
#

Name:           yum-scripts
Version:        1.1.13
Release:        2
License:        GPL-2.0+
Summary:        Utilities based around the yum package manager
Url:            http://linux.duke.edu/yum/download/yum-utils/
Group:          System/Packages
Source:         https://github.com/henrysher/yum-utils/archive/yum-utils-%{version}.tar.gz
Patch:          yum-utils-1.1.6.patch
Patch1:         yum-utils-1.1.6-changelog.patch
Patch2:         yum-utils-1.1.10.patch
Conflicts:      yum-utils
BuildRequires:  python-devel
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version} > 1030
%py_requires
%endif

%description
yum-utils is a collection of utilities and examples for the yum package
manager. It includes utilities by different authors that make yum
easier and more powerful to use.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%prep
%setup -q -n yum-utils-yum-utils-%{version}
%patch
%patch1
%patch2

%build

%install
make DESTDIR=$RPM_BUILD_ROOT install
# not packaged plugin
rm $RPM_BUILD_ROOT/%{_mandir}/man8/yum-security.8
rm -v $RPM_BUILD_ROOT/usr/bin/yum-builddep \
   $RPM_BUILD_ROOT/usr/bin/yumdownloader \
   $RPM_BUILD_ROOT/usr/sbin/yum-complete-transaction \
   $RPM_BUILD_ROOT/usr/share/man/man1/yum-builddep.1 \
   $RPM_BUILD_ROOT/usr/share/man/man1/yum-changelog.1 \
   $RPM_BUILD_ROOT/usr/share/man/man1/yum-filter-data.1 \
   $RPM_BUILD_ROOT/usr/share/man/man1/yum-list-data.1 \
   $RPM_BUILD_ROOT/usr/share/man/man1/yum-verify.1 \
   $RPM_BUILD_ROOT/usr/share/man/man1/yumdownloader.1 \
   $RPM_BUILD_ROOT/usr/share/man/man5/yum-changelog.conf.5 \
   $RPM_BUILD_ROOT/usr/share/man/man8/yum-complete-transaction.8


%post

%postun

%files
%defattr(-,root,root)
%doc README
%{_bindir}/debuginfo-install
%{_bindir}/package-cleanup
%{_bindir}/repoclosure
%{_bindir}/repodiff
%{_bindir}/repomanage
%{_bindir}/repoquery
%{_bindir}/repotrack
%{_bindir}/reposync
%{_bindir}/repo-graph
%{_bindir}/repo-rss
%{_mandir}/man1/yum-utils.1.*
%{_mandir}/man1/package-cleanup.1.*
%{_mandir}/man1/repo-rss.1.*
%{_mandir}/man1/repoquery.1.*
%{_mandir}/man1/reposync.1.*

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Fri May 12 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
