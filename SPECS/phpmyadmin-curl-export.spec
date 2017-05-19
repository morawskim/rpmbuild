#
# spec file for package phpmyadmin-curl-export
#
# Copyright (c) 2017 Marcin Morawski <marcin@morawskim.pl>
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

%global commit0 7fa7a96c16d0c438aaee3d4f58e0c972f3e38ce5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           phpmyadmin-curl-export
Version:        20160710
Release:        2
License:        GPL
Summary:        Connect to phpMyAdmin and export database to file
Url:            https://github.com/morawskim/phpmyadmin-curl-export
Source:         https://github.com/morawskim/phpmyadmin-curl-export/archive/%{shortcommit0}.tar.gz
Requires:       wget
Requires:       tar
Requires:       coreutils
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Connect to phpMyAdmin and export database to file.

%prep
%setup  -qn phpmyadmin-curl-export-%{commit0}

%build
exit 0

%install
%{__install} -D -p -m 0755 phpmyadmin-curl-export.sh %{buildroot}%{_bindir}/%{name}
%{__install} -D -p -m 0644 completions/phpmyadmin-curl-export.sh %{buildroot}/etc/bash_completion.d/%{name}.bash

%post
exit 0

%postun
exit 0

%files
%defattr(0755,root,root)
%doc README.md
%{_bindir}/%{name}
%attr(0644, root, root) /etc/bash_completion.d/%{name}.bash

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sun May 07 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
