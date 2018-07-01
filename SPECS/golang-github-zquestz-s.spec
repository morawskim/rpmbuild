#
# spec file for package golang-github-zquestz-s
#
# Copyright (c) 2018 Marcin Morawski <marcin@morawskim.pl>.
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

%global provider        github
%global provider_tld    com
%global project         zquestz
%global repo            s
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-github-zquestz-s
Version:        0.5.12
Release:        1
License:        MIT
Summary:        Open a web search in your terminal
Url:            https://github.com/zquestz/s
Group:          Development/Languages/Other
Source:         https://github.com//%{project}/%{repo}/archive/v%{version}.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang-github-FiloSottile-gvt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%{go_nostrip}
%{go_provides}

%description
Web search from the terminal. Just opens in your browser.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/X11/Terminals
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for s.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/X11/Terminals
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for s.

%prep
%setup -q -n %{repo}-%{version}
gvt restore

%build
%goprep %{import_path}
%gobuild

%install
%goinstall
%gosrc
%gofilelist
install -Dm 0644 autocomplete/%{repo}-completion.bash %{buildroot}/%{_datadir}/bash-completion/completions/%{repo}
install -Dm 0644 autocomplete/%{repo}.fish %{buildroot}/%{_datadir}/fish/vendor_completions.d/%{repo}.fish

%post

%postun

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md LICENSE
%_bindir/s

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%changelog
* Sun Jul 01 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release

