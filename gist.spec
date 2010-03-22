# TODO:
# - /usr/bin/gist:86: command not found: pbcopy
#   which: no pbcopy in (/usr/local/bin:/usr/bin:/bin:/home/users/z/bin)
# - cleanup? I have no experience with ruby.

%define		commit	2c90f46

Summary:	Command-line interface for gists.github.com
Name:		gist
Version:	1.0.3
Release:	0.1
License:	MIT
Source0:	http://github.com/defunkt/gist/tarball/v%{version}
# Source0-md5:	e0b9eb913c46ad49e5d6072c420b2a17
Group:		Development/Languages
URL:		http://github.com/defunkt/gist
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Command-line interface for gists.github.com.

%prep
%setup -q -n defunkt-%{name}-%{commit}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp gist $RPM_BUILD_ROOT%{_bindir}/gist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown
%attr(755,root,root) %{_bindir}/gist
