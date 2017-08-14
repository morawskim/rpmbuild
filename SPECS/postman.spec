#
# spec file for package postman
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

%define postman_root /usr/lib/postman
%define binname Postman

Name:           Postman
Version:        4.9.3
Release:        3
License:        Commercial
Summary:        Supercharge your API workflow with Postman
Url:            https://www.getpostman.com/
Group:          Productivity/Networking/Web/Utilities
Source:         Postman-linux-x64-4.9.3.tar.gz
BuildArch:      x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Postman is the complete toolchain for API developers, used by more than 3
million developers and 30,000 companies worldwide. Postman makes working with
APIs faster and easier by supporting developers at every stage of their
workflow, and is available for Mac OS X, Windows, Linux and Chrome users.

%prep
%setup -qn %{name}

%build

cat >%{name}.desktop <<EOF
[Desktop Entry]
Comment=%{summary}
Exec=%{postman_root}/%{binname}
Icon=%{postman_root}/resources/app/assets/icon.png
Name=%{name}
NoDisplay=false
StartupNotify=true
Terminal=0
TerminalOptions=
Type=Application
Categories=Development;IDE;
EOF

# Create the wrapper for /usr/bin
cat >%{name}.binwrapper <<EOF
#!/bin/sh
%{postman_root}/%{binname} $@
EOF

%install
%{__mkdir} -p %{buildroot}/%{postman_root} \
              %{buildroot}/%{_bindir}

%{__cp} -pr . %{buildroot}/%{postman_root}

%{__install} -p -m0755 %{name}.binwrapper \
                  %{buildroot}/%{_bindir}/%{name}

%{__install} -D -m0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# File resources/app/node_modules/node-simple-router/test/common/public/cgi-bin/hello.bas require
# /usr/local/bin/yabasic, so we remove test dir
%{__rm} -rf %{buildroot}/%{postman_root}/resources/app/node_modules/node-simple-router/test/

%post

%postun

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{postman_root}
%{postman_root}/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
