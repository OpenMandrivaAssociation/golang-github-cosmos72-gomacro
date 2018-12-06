%undefine _debugsource_packages

%global goipath github.com/cosmos72/gomacro
Version:        2.7

%global common_description %{expand:
gomacro is an almost complete Go interpreter, implemented in pure Go. It offers
both an interactive REPL and a scripting mode, and does not require a Go
toolchain at runtime (except in one very specific case: import of a third party
package at runtime).}

%gometa

Name:           %{goname}
Release:        4%{?dist}
Summary:        Interactive Go interpreter and debugger
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/cosmos72/gomacro/commit/b1b877762ce43edd5f3cce11f727bca599ab62b9
Patch0001:      0001-fix-34-do-not-assume-that-os.File-6th-method-is-Read.patch

%description
%{common_description}


%package -n gomacro
Summary:       %{summary}

%description -n gomacro
%{common_description}


%package devel
Summary:       %{summary}

BuildRequires: golang(github.com/peterh/liner)
BuildRequires: golang(golang.org/x/sync/syncmap)

%description devel
%{common_description}

This package contains library source intended for building other packages
which use import path with %{goipath} prefix.


%prep
%forgesetup
%patch0001 -p1


%build
%gobuildroot
%gobuild -o _bin/gomacro %{goipath}


%install
%goinstall
install -m 0755 -vd        %{buildroot}%{_bindir}
install -m 0755 -vp _bin/* %{buildroot}%{_bindir}/


%check
%gochecks


%files -n gomacro
%doc README.md
%license LICENSE
%{_bindir}/gomacro

%files devel -f devel.file-list
%license LICENSE


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.7-4
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 2.7-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.7-1
- First package for Fedora
