#
# spec file for package git-crypt
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

Name:           git-crypt
Version:        0.5.0
Release:        1
License:        GPL-3
Summary:        Transparent file encryption in git
Url:            https://www.agwa.name/projects/git-crypt/
Group:          Productivity/Security
Source:         https://www.agwa.name/projects/git-crypt/downloads/%{name}-%{version}.tar.gz
BuildRequires:  libressl-devel
Requires:       openssl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
git-crypt enables transparent encryption and decryption of files in a git
repository. Files which you choose to protect are encrypted when committed, and
decrypted when checked out. git-crypt lets you freely share a repository
containing a mix of public and private content. git-crypt gracefully degrades,
so developers without the secret key can still clone and commit to a repository
with encrypted files. This lets you store your secret material (such as keys or
passwords) in the same repository as your code, without requiring you to lock
down your entire repository.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_usr} %{?_smp_mflags}

%post

%postun

%files
%defattr(-,root,root)
%doc NEWS README COPYING doc/
%{_bindir}/%{name}

%changelog
* Sun Nov 19 2017 Marcin Morawski <marcin@morawskim.pl>
-  Change to libressl-devel

* Sat Nov 18 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
