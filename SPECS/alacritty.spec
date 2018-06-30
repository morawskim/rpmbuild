#
# spec file for package alacritty
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

%define rev 015a6d4c03764608778d8aea80638fcc9704c2f3
Name:           alacritty
Version:        0.1.0
Release:        1
License:        Apache-2.0
Summary:        A GPU-accelerated terminal emulator
Url:            https://github.com/jwilm/alacritty/
Group:          System/X11/Terminals
Source:         https://github.com/jwilm/alacritty/archive/%{rev}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  rust
BuildRequires:  rust-std
BuildRequires:  xclip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Alacritty is a terminal emulator written in Rust that leverages the GPU for
rendering.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/X11/Terminals
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for alacritty. It includes support
for every argument that can currently be passed to alacritty.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/X11/Terminals
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for alacritty.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/X11/Terminals
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for alacritty.

%prep
%setup -q -n %{name}-%{rev}

%build
cargo build --release %{?_smp_mflags}

%install
cargo install --root=%{buildroot}/%{_prefix}

# rm duplicate license and useless toml file
rm -fr %{buildroot}%{_datadir}
rm  %{buildroot}%{_prefix}/.crates.toml

# install man page and completions
install -Dm 0644 %{name}.man %{buildroot}/%{_mandir}/man1/%{name}.1
install -Dm 0644 %{name}-completions.bash %{buildroot}/%{_datadir}/bash-completion/completions/%{name}
install -Dm 0644 %{name}-completions.fish %{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm 0644 %{name}-completions.zsh  %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE-APACHE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
* Thu Jun 28 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release

