#
# spec file for package trans
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

Name:           translate-shell
Version:        0.9.4
Release:        1
License:        Unlicense
Summary:        Command-line translator
Url:            https://github.com/soimort/translate-shell
Source:         https://github.com/soimort/translate-shell/archive/v%{version}.tar.gz
Provides:       trans
Requires:       gawk
Suggests:       curl
Suggests:       less
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Translate Shell (formerly Google Translate CLI) is a command-line translator
powered by Google Translate (default), Bing Translator, Yandex.Translate and
Apertium. It gives you easy access to one of these translation engines in your
terminal.

%prep
%setup -n %{name}-%{version}

%build
make

%install
make install PREFIX=%{buildroot}/usr 

%post

%postun

%files
%defattr(-,root,root)
%doc WAIVER README.md LICENSE
%{_bindir}/trans
%{_mandir}/man1/trans.1.gz

%changelog
* Sun Jul 31 2016 Marcin Morawski <marcin@morawskim.pl>
-  initial packaging
