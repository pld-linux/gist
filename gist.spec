Summary:	Command-line interface for gists.github.com
Name:		gist
Version:	1.0.3
Release:	2
License:	MIT
Source0:	http://github.com/defunkt/gist/tarball/v%{version}
# Source0-md5:	e0b9eb913c46ad49e5d6072c420b2a17
Patch0:		stop-bashism.patch
Group:		Applications
URL:		http://github.com/defunkt/gist
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	git-core
Requires:	groff
Requires:	xclip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command-line interface for <gists.github.com>.

%prep
%setup -qc
mv defunkt-%{name}-*/* .
%patch0 -p1

# fix #!%{_bindir}/env ruby -> #!%{_bindir}/ruby:
%{__sed} -i -e '1s,^#!.*ruby,#!%{__ruby},' %{name}

awk '{if (p) print} /^__END__$/ {p = 1}' %{name} > %{name}.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown
%attr(755,root,root) %{_bindir}/gist
%{_mandir}/man1/%{name}.1*
