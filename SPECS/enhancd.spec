#
# spec file for package enhancd
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

%define commit b2dbdcd3dffb430b4ff4faf68ee81aa26c3b4dab

Name:           enhancd
Version:        20161231
Release:        3
License:        MIT
Summary:        A next-generation cd command with an interactive filter
Url:            https://github.com/b4b4r07/enhancd
Group:          Productivity/File utilitie
Source:         https://github.com/b4b4r07/enhancd/archive/%{commit}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
cd command is one of the frequently used commands.

Nevertheless, it is not so easy to handle unfortunately. A directory path given
as an argument to cd command must be a valid path that exists and is able to
resolve. In other words, you cannot pass a partial path such as "dir" (you are
in /home/lisa, dir is /home/lisa/work/dir) to cd command.

The new cd command called "enhancd" enhanced the flexibility and usability for
a user. enhancd will memorize all directories visited by a user and use it for
the pathname resolution. If the log of enhancd have more than one directory
path with the same name, enhancd will pass the candidate directories list to
the filter within the ENHANCD_FILTER environment variable in order to narrow it
down to one directory.

Thanks to this mechanism, the user can intuitively and easily change the
directory you want to go.

%prep
%setup -qn %{name}-%{commit}
%build

%install
%{__mkdir_p} %{buildroot}/%{_datarootdir}/%{name}/src

%{__install} -D -m0644 init.sh %{buildroot}/%{_datarootdir}/%{name}/init.sh
%__install -D -p -m 0644 doc/man/man1/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
cp -avr src/ %{buildroot}/%{_datarootdir}/%{name}/

%post

%postun

%files
%defattr(-,root,root)
%doc doc/ README.md
%doc %{_mandir}/man1/%{name}.1%{?ext_man}
%{_datarootdir}/%{name}/init.sh
%{_datarootdir}/%{name}/src/*

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 20161231-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sun Mar 05 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
