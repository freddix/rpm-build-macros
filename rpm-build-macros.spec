%define		rpm_macros_rev 1.702

Summary:	Freddix RPM build macros
Name:		rpm-build-macros
Version:	%{rpm_macros_rev}
Release:	1
License:	GPL
Group:		Base
Source0:	rpm.macros
Source1:	rpm-find-lang
Provides:	rpmbuild(macros) = %{rpm_macros_rev}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_rpmlibdir %{_prefix}/lib/rpm

%description
This package contains rpm build macros for Freddix.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_rpmlibdir},/etc/shrc.d}
cp %{SOURCE0} $RPM_BUILD_ROOT%{_rpmlibdir}/macros.build
install %{SOURCE1} $RPM_BUILD_ROOT%{_usrlibrpm}/find-lang.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_rpmlibdir}/macros.build
%attr(755,root,root) %{_rpmlibdir}/find-lang.sh

