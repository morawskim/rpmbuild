#
# spec file for package completion-ruby
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

%global commit0 f3e4345042b0cc48317e45b673dfd3d23904b9a7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           completion-ruby
Version:        20160428
Release:        1
License:        MIT license
Summary:        Bash completion for Ruby-related commands
Url:            https://github.com/mernen/completion-ruby
Source0:        https://github.com/mernen/completion-ruby/archive/%{shortcommit0}.tar.gz
Source1:        https://gist.githubusercontent.com/vigo/5008330/raw/3c36be89ab1107ac45a30a4ce17fc314b029a912/bunde_complete.sh
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
completion-ruby is a set of bash scripts offering command-line completion for various Ruby-related commands and tools.

%prep
%setup  -qn completion-ruby-%{commit0}
%{__install} -m 644 %{SOURCE1} bunde_complete.sh

%build
exit 0

%install
%{__install} -D -p -m 0644 bunde_complete.sh %{buildroot}/etc/bash_completion.d/bundle
%{__install} -D -p -m 0644 completion-gem %{buildroot}/etc/bash_completion.d/gem
%{__install} -D -p -m 0644 completion-jruby %{buildroot}/etc/bash_completion.d/jruby
%{__install} -D -p -m 0644 completion-rails %{buildroot}/etc/bash_completion.d/rails
%{__install} -D -p -m 0644 completion-rake %{buildroot}/etc/bash_completion.d/rake
%{__install} -D -p -m 0644 completion-ruby %{buildroot}/etc/bash_completion.d/ruby

%post
exit 0

%postun
exit 0

%files
%defattr(0644,root,root)
%doc README.markdown MIT-LICENSE
/etc/bash_completion.d/bundle
/etc/bash_completion.d/gem
/etc/bash_completion.d/jruby
/etc/bash_completion.d/rails
/etc/bash_completion.d/rake
/etc/bash_completion.d/ruby

%changelog
* Thu Apr 28 2016 Marcin Morawski <marcin@morawskim.pl>
- init release
