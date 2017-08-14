#
# spec file for package bash-snippets
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

Name:           bash-snippets
Version:        1.13.0
Release:        2
License:        MIT
Summary:        A collection of small bash scripts for heavy terminal users 
Url:            https://github.com/alexanderepstein/Bash-Snippets
Group:          Productivity/Other
Source:         https://github.com/alexanderepstein/Bash-Snippets/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A collection of small bash scripts for heavy terminal users with no
dependencies.

%prep
%setup -qn Bash-Snippets-%{version}

%build

%install
mkdir -p %{buildroot}/%{_bindir}
tools='currency stocks weather crypt movies taste short geo cheat ytview cloudup qrify siteciphers todo'

for tool in ${tools}
do
    chmod a+x $tool/$tool
    cp $tool/$tool %{buildroot}/%{_bindir}
done

%{__install} -Dp -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%post

%postun

%files
%defattr(-,root,root)
%doc changelog.md README.md LICENSE
%{_bindir}/cheat
%{_bindir}/cloudup
%{_bindir}/crypt
%{_bindir}/currency
%{_bindir}/geo
%{_bindir}/movies
%{_bindir}/qrify
%{_bindir}/short
%{_bindir}/siteciphers
%{_bindir}/stocks
%{_bindir}/taste
%{_bindir}/todo
%{_bindir}/weather
%{_bindir}/ytview
%{_mandir}/man1/%{name}.1.gz

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 1.13.0-2
- Rebuild for openSUSE 42.3

* Mon Jul 17 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
