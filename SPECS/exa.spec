#
# spec file for package exa
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

Name:           exa
Version:        0.8.0
Release:        1
License:        MIT
Summary:        Replacement for 'ls' written in Rust
Url:            https://the.exa.website/
Group:          Productivity/File utilitie
Source:         https://github.com/ogham/exa/archive/v%{version}.tar.gz
BuildRequires:  cmake libgit2-devel
BuildRequires:  rust >= 1.17.0
BuildRequires:  cargo >= 0.5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package bash-completion
Summary:        %{name} bash completion
Requires:       %{name} = %{version}
BuildArch:      noarch

%description bash-completion
%{name} bash completion

%description
exa is a modern replacement for ls. It uses colours for information by default,
helping you distinguish between many types of files, such as whether you are
the owner, or in the owning group. It also has extra features not present in
the original ls, such as viewing the Git status for a directory, or recursing
into directories with a tree view. exa is written in Rust, so it’s small, fast,
and portable.

%prep
%setup -q

%build
make build

%install
%__mkdir_p %{buildroot}/%{_bindir}
%__mkdir_p %{buildroot}/%{_sysconfdir}/bash_completion.d
%__mkdir_p %{buildroot}/%{_mandir}

make install DESTDIR=%{buildroot} PREFIX=%{_usr}
make install-bash-completions DESTDIR=%{buildroot} BASHDIR=%{_sysconfdir}/bash_completion.d
#make install zsh-completins DESTDIR=%{buildroot} ZSHDIR=%{_usr}/share/zsh/vendor-completions
#make install fish-completins DESTDIR=%{buildroot} FISHDIR=%{_usr}/share/fish/vendor_completions.d

%post

%postun

%files
%defattr(-,root,root)
%doc LICENCE README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%defattr(-,root,root)
%{_sysconfdir}/bash_completion.d/%{name}
