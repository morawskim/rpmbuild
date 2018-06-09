#
# spec file for package mozilla-rr
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

Name:           rr
Version:        5.2.0
Release:        1
License:        MIT and BSD
Summary:        Lightweight tool for recording and replaying execution of applications (trees of processes and threads)
Url:            http://rr-project.org
Group:          Development/Debuggers
Source:         https://github.com/mozilla/%{name}/archive/%{version}.tar.gz
Patch0:         %{name}.change-path-to-bash.patch
BuildRequires:  python2-pexpect
BuildRequires:  cmake
BuildRequires:  gdb
BuildRequires:  ccache
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libstdc++-devel
BuildRequires:  zlib-devel
BuildRequires:  man-pages
BuildRequires:  capnproto
BuildRequires:  libcapnp-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
rr is a lightweight tool for recording and replaying execution of applications
(trees of processes and threads).  For more information, please visit

http://rr-project.org

%prep
%setup -q
%patch0

%build
mkdir build
pushd build
cmake -Ddisable32bit=ON -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}
popd

%install
pushd build
make install DESTDIR=%{buildroot} %{?_smp_mflags}
popd

%post

%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_libexecdir}/*
%{_bindir}/rr
%{_bindir}/rr_exec_stub*
%{_bindir}/rr_page*
%{_bindir}/signal-rr-recording.sh
%{_datarootdir}/rr/*.xml

%changelog
* Sat Jun 09 2018 Marcin Morawski <marcin@morawskim.pl>
-  Update to 5.2.0

* Mon Jun 04 2018 Marcin Morawski <marcin@morawskim.pl>
-  Require python2-pexpect

* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 4.4.0-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Wed Apr 19 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
