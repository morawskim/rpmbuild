#
# spec file for package bup
#
# Copyright (c) 2016 Marcin Morawski <marcin@morawskim.pl>
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

Name:           bup
Version:        0.27
Release:        2
Summary:        Backup program based on git
License:        LGPL-2.0
Group:          Productivity/Archiving/Backup
Url:            https://bup.github.io/
Source:         https://github.com/bup/bup/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel >= 2.5
BuildRequires:  python-fuse
BuildRequires:  python-xattr
BuildRequires:  python-pylibacl
BuildRequires:  python-tornado
BuildRequires:  perl-Time-HiRes
BuildRequires:  git-core >= 1.5.3.1
BuildRequires:  pandoc
Requires:       python >= 2.5
Requires:       git-core >= 1.5.3.1
Requires:       python-fuse
Requires:       python-xattr
Requires:       python-pylibacl
Requires:       python-tornado
Requires:       par2
%py_requires

%description
Very efficient backup system based on the git packfile format, 
providing fast incremental saves and global deduplication 
(among and within files, including virtual machine images).

%prep
%setup -q 
# rpmlint: fix incorrect-fsf-address
find . -type f | xargs sed -i -e 's:59 Temple Place\, Suite 330\, Boston\, MA  02111-1307  USA:51 Franklin Street\, Fifth Floor\, Boston\, MA 02110-1301 USA:g'
# fix docpath
sed -i -e "s|/share/doc/bup|/share/doc/packages/bup|g" Makefile */Makefile

%build
make %{?_smp_mflags} PYTHON=%{__python} 

%install
%if 0%{!?make_install:1} 
%define make_install make install 'DESTDIR=%{buildroot}' 
%endif 
%make_install PYTHON=%{__python}

%files
%defattr(-, root, root)
%doc README LICENSE
%{_bindir}/%{name}
%dir /usr/lib/%{name}/
%dir /usr/lib/%{name}/bup/
%dir /usr/lib/%{name}/cmd/
%dir /usr/lib/%{name}/web/
%dir /usr/lib/%{name}/web/static/
/usr/lib/%{name}/bup/*
/usr/lib/%{name}/cmd/*
/usr/lib/%{name}/web/*
/usr/lib/%{name}/web/static/*
%{_mandir}/man1/*

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2


