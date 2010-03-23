Summary:	Command-line interface for gists.github.com
Name:		gist
Version:	1.0.3
Release:	0.1
License:	MIT
Source0:	http://github.com/defunkt/gist/tarball/v%{version}
# Source0-md5:	e0b9eb913c46ad49e5d6072c420b2a17
Group:		Applications
URL:		http://github.com/defunkt/gist
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command-line interface for <gists.github.com>.

%prep
%setup -qc
mv defunkt-%{name}-*/* .

# fix #!/usr/bin/env ruby -> #!/usr/bin/ruby:
%{__sed} -i -e '1s,^#!.*ruby,#!%{__ruby},' %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown
%attr(755,root,root) %{_bindir}/gist
