#
# spec file for package cheat
#
# Copyright (c) 2016 Marcin Morawski <marcin@morawskim.pl>.
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

Name:           cheat
Version:        2.1.27
Release:        1
License:        MIT and GPL3
Summary:        Create and view interactive cheatsheets on the command-line
Url:            https://github.com/chrisallenlane/cheat
Group:          Applications/Productivity
Source:         https://github.com/chrisallenlane/cheat/archive/%{version}.tar.gz
BuildRequires:  python
BuildRequires:  python-setuptools
BuildArch:      noarch
Provides:       python-cheat = %{version}
Obsoletes:      python-cheat < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package bash-completion
Summary:        cheat bash completion
Requires:       %{name} = %{version}

%description
cheat allows you to create and view interactive cheatsheets on the
command-line. It was designed to help remind *nix system administrators of
options for commands that they use frequently, but not frequently enough to
remember.

%description bash-completion
cheat bash completion

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -D -m 0644 cheat/autocompletion/cheat.bash %{buildroot}/%{_sysconfdir}/bash_completion.d/%{name}.sh
%__install -D -p -m 0644 man1/cheat.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG README.md LICENSE
%doc %{_mandir}/man1/cheat.1%{?ext_man}
%{_bindir}/cheat
%{python_sitelib}/cheat
%{python_sitelib}/cheat-%{version}-py%{py_ver}.egg-info

%files bash-completion
%{_sysconfdir}/bash_completion.d/cheat.sh

%changelog
* Mon Feb 13 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
