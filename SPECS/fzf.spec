#
# spec file for package fzf
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

Name:           fzf
Version:        0.17.3
Release:        3
License:        MIT
Summary:        A command-line fuzzy finder written in Go
Url:            https://github.com/junegunn/fzf
Group:          Applications/Productivity
Source:         https://github.com/junegunn/fzf/archive/%{version}.tar.gz
BuildRequires:  go
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package tmux
Summary:        fzf-tmux
Requires:       %{name} = %{version}
BuildArch:      noarch

%package bash-completion
Summary:        fzf bash completion
Requires:       %{name} = %{version}
BuildArch:      noarch

%package vim
Summary:        fzf vim plugin
Requires:       %{name} = %{version}
Group:          Productivity/Text/Editors
Requires:       vim
BuildArch:      noarch
%{!?vim_data_dir:%global vim_data_dir /usr/share/vim/%(readlink /usr/share/vim/current)}

%description tmux
fzf-tmux

%description bash-completion
fzf bash completion

%description vim
fzf vim plugin

%description
fzf is a general-purpose command-line fuzzy finder.

Pros

* No dependencies
* Blazingly fast
* The most comprehensive feature set
* Flexible layout using tmux panes
* Batteries included
* Vim/Neovim plugin, key bindings and fuzzy auto-completion

%prep
%setup -q

%build
make

%install
install -m 755 -D -p target/fzf-linux_amd64 %{buildroot}/%{_bindir}/%{name}
install -m 755 -D -p bin/%{name}-tmux %{buildroot}/%{_bindir}/%{name}-tmux
install -m 644 -D -p man/man1/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
install -m 644 -D -p man/man1/%{name}-tmux.1 %{buildroot}/%{_mandir}/man1/%{name}-tmux.1
install -m 755 -D -p shell/completion.bash %{buildroot}/%{_sysconfdir}/bash_completion.d/%{name}.sh
install -m 644 -D -p shell/key-bindings.bash %{buildroot}/%{_datadir}/%{name}/shell/key-bindings.bash
install -m 644 -D -p plugin/fzf.vim %{buildroot}/%{vim_data_dir}/plugin/%{name}.vim

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md LICENSE
%{_bindir}/fzf
%{_mandir}/man1/%{name}.1%{?ext_man}

%files tmux
%defattr(-,root,root)
%{_bindir}/fzf-tmux
%{_mandir}/man1/%{name}-tmux.1%{?ext_man}

%files bash-completion
%defattr(-,root,root)
%{_sysconfdir}/bash_completion.d/%{name}.sh
%{_datadir}/%{name}/shell/key-bindings.bash

%files vim
%defattr(-,root,root)
%{vim_data_dir}/plugin/%{name}.vim

%changelog
* Sat Feb 10 2018 Marcin Morawski <marcin@morawskim.pl>
-  Update to 0.17.3

* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 0.15.9-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sat Dec 24 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
